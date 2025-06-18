#!/usr/bin/env python3
"""
Simple interface for Claude to play NetHack - provides game access only.
Claude makes all strategic decisions based on analysis.
"""

from nethack_wrapper import NetHackWrapper
import time
import sys

class ClaudeNetHackInterface:
    def __init__(self):
        self.wrapper = NetHackWrapper()
        self.game_active = False
    
    def start_session(self):
        """Start NetHack session"""
        if self.wrapper.start_game():
            self.game_active = True
            print("=== NETHACK SESSION STARTED ===")
            print("Game ready for Claude's strategic decisions")
            return True
        return False
    
    def send_move(self, command):
        """Send a single command to NetHack"""
        if not self.game_active:
            print("Game not active!")
            return
        
        print(f"Sending command: {command}")
        self.wrapper.send_command(command)
        time.sleep(0.5)
    
    def view_state(self):
        """View current game state"""
        screen = self.wrapper.capture_screen()
        print("=== CURRENT GAME STATE ===")
        print(screen)
        return screen
    
    def save_and_exit(self):
        """Save progress and close game"""
        print("Saving progress...")
        self.wrapper.save_and_quit()
        self.wrapper.close()
        self.game_active = False
        print("Game saved and closed.")

# Interface for Claude to use
def start_game():
    """Start NetHack for Claude to play"""
    interface = ClaudeNetHackInterface()
    if interface.start_session():
        return interface
    return None

if __name__ == "__main__":
    print("NetHack Interface for Claude")
    print("Use: interface = start_game()")
    print("Then: interface.send_move('command')")
    print("View: interface.view_state()")
    print("Save: interface.save_and_exit()")