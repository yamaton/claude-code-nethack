#!/usr/bin/env python3
"""
NetHack wrapper for programmatic interaction using pexpect.
Allows Claude to play NetHack by controlling the game programmatically.
"""

import pexpect
import re
import time
import sys
from typing import Optional, List, Dict, Any


class NetHackWrapper:
    def __init__(self):
        self.process = None
        self.last_screen = ""
        self.game_started = False
        
    def start_game(self, character_name: str = "Claude", 
                   profession: str = "tourist", race: str = "human", 
                   new_game: bool = False) -> bool:
        """Start a new NetHack game with specified character."""
        try:
            # Start nethack with options to skip some prompts
            cmd = f"nethack -u {character_name} -p {profession} -r {race}"
            self.process = pexpect.spawn(cmd, timeout=10)
            self.process.logfile_read = sys.stdout.buffer
            
            # Handle different startup scenarios
            index = self.process.expect([
                "Restoring save file",
                "Shall I pick",
                "@",
                pexpect.TIMEOUT
            ], timeout=15)
            
            if index == 0:  # Restoring save file
                print("Found existing save file, continuing...")
                self.process.expect("--More--", timeout=10)
                self.process.sendline(" ")  # Continue
                self.process.expect("@", timeout=15)
                self.game_started = True
                self.capture_screen()
                return True
                
            elif index == 1:  # Character selection
                self.process.sendline("y")  # Auto-pick character
                self.process.expect("@", timeout=15)
                self.game_started = True
                self.capture_screen()
                return True
                
            elif index == 2:  # Already in game
                self.game_started = True
                self.capture_screen()
                return True
                
            else:  # Timeout
                print("Timeout starting NetHack")
                return False
            
        except pexpect.exceptions.TIMEOUT:
            print("Timeout starting NetHack")
            return False
        except Exception as e:
            print(f"Error starting NetHack: {e}")
            return False
    
    def capture_screen(self) -> str:
        """Capture the current game screen."""
        if not self.process:
            return ""
        
        # Send a no-op command to refresh screen
        self.process.send(" ")  # Space usually does nothing
        try:
            self.process.expect("@", timeout=2)
        except:
            pass
            
        # Get the screen content
        screen = self.process.before.decode('utf-8', errors='ignore')
        self.last_screen = screen
        return screen
    
    def get_clean_screen(self) -> str:
        """Get a cleaned version of the game screen without ANSI codes."""
        import re
        screen = self.capture_screen()
        # Remove ANSI escape sequences
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        clean_screen = ansi_escape.sub('', screen)
        return clean_screen
    
    def display_game_state(self) -> str:
        """Display the current game state in a readable format."""
        screen = self.get_clean_screen()
        lines = screen.split('\n')
        
        # Find the status line (usually at bottom)
        status_line = ""
        game_board = []
        
        for i, line in enumerate(lines):
            if "Claude the" in line or "St:" in line:
                status_line = line.strip()
            elif len(line.strip()) > 0 and not line.startswith("Unknown command"):
                game_board.append(line)
        
        # Format output
        result = "=== NETHACK GAME STATE ===\n"
        if status_line:
            result += f"Status: {status_line}\n"
        result += "\nGame Board:\n"
        for line in game_board[-20:]:  # Show last 20 lines
            result += line + "\n"
        result += "========================\n"
        
        return result
    
    def send_command(self, command: str) -> str:
        """Send a command to NetHack and return the response."""
        if not self.process or not self.game_started:
            return "Game not started"
        
        try:
            self.process.send(command)
            time.sleep(0.1)  # Small delay for game to process
            
            # Try to capture response
            try:
                self.process.expect("@", timeout=3)
            except pexpect.exceptions.TIMEOUT:
                # Sometimes @ isn't visible, just continue
                pass
                
            response = self.capture_screen()
            return response
            
        except Exception as e:
            return f"Error sending command: {e}"
    
    def look_around(self) -> str:
        """Look around the current area."""
        return self.send_command(":")
    
    def move(self, direction: str) -> str:
        """Move in a direction (h,j,k,l or arrow keys)."""
        direction_map = {
            "north": "k", "up": "k",
            "south": "j", "down": "j", 
            "east": "l", "right": "l",
            "west": "h", "left": "h",
            "northeast": "u", "northwest": "y",
            "southeast": "n", "southwest": "b"
        }
        
        cmd = direction_map.get(direction.lower(), direction)
        return self.send_command(cmd)
    
    def get_inventory(self) -> str:
        """Display inventory."""
        return self.send_command("i")
    
    def search(self) -> str:
        """Search for hidden doors/traps."""
        return self.send_command("s")
    
    def rest(self) -> str:
        """Rest/wait."""
        return self.send_command(".")
    
    def save_and_quit(self) -> str:
        """Save the game and quit."""
        self.send_command("S")
        return "Game saved"
    
    def quit_without_saving(self) -> str:
        """Quit without saving."""
        self.send_command("\x03")  # Ctrl-C
        return "Quit without saving"
    
    def get_help(self) -> str:
        """Get NetHack help."""
        return self.send_command("?")
    
    def close(self):
        """Close the NetHack process."""
        if self.process:
            try:
                self.process.terminate()
            except:
                self.process.kill()
            self.process = None
        self.game_started = False


def main():
    """Simple test of the wrapper."""
    wrapper = NetHackWrapper()
    
    print("Starting NetHack...")
    if not wrapper.start_game():
        print("Failed to start game")
        return
    
    print("\nGame started! Initial screen:")
    print(wrapper.capture_screen())
    
    print("\n--- Available commands ---")
    print("move <direction>  - Move (north/south/east/west/etc)")
    print("look            - Look around")
    print("inventory       - Show inventory") 
    print("search          - Search area")
    print("rest            - Rest/wait")
    print("help            - NetHack help")
    print("status          - Show clean game state")
    print("screen          - Show raw screen")
    print("quit            - Quit game")
    print("raw <cmd>       - Send raw command")
    
    try:
        while True:
            cmd = input("\n> ").strip().lower()
            
            if cmd == "quit":
                wrapper.save_and_quit()
                break
            elif cmd == "look":
                print(wrapper.look_around())
            elif cmd.startswith("move "):
                direction = cmd[5:]
                print(wrapper.move(direction))
            elif cmd == "inventory":
                print(wrapper.get_inventory())
            elif cmd == "search":
                print(wrapper.search())
            elif cmd == "rest":
                print(wrapper.rest())
            elif cmd == "help":
                print(wrapper.get_help())
            elif cmd.startswith("raw "):
                raw_cmd = cmd[4:]
                print(wrapper.send_command(raw_cmd))
            elif cmd == "screen":
                print(wrapper.capture_screen())
            elif cmd == "status":
                print(wrapper.display_game_state())
            else:
                print("Unknown command. Type 'help' for NetHack help or 'quit' to exit.")
                
    except KeyboardInterrupt:
        print("\nQuitting...")
    finally:
        wrapper.close()


if __name__ == "__main__":
    main()