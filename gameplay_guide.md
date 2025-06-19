# NetHack Gameplay Guide: Using the tmux Interface

This guide explains how to monitor and interact with Claude's NetHack gameplay using the new `./run` script interface.

## 1. Viewing Gameplay History

### Strategy Scrapbook
Claude maintains a comprehensive strategy document that tracks all gameplay decisions and findings:

```bash
cat nethack_strategy.md
```

This markdown file contains:
- **Mission objectives** and current progress
- **Character status** and stats
- **Exploration log** with detailed move-by-move history
- **Strategic findings** and observations
- **Map discoveries** and room layouts
- **Combat encounters** and outcomes
- **Technical notes** about gameplay mechanics

### Recent Activity
To see the most recent gameplay session updates:

```bash
tail -20 nethack_strategy.md
```

### Git History (if available)
If the directory is under git version control, you can see the progression:

```bash
git log --oneline
git show HEAD  # Latest changes
```

## 2. Using the ./run Script Interface

### Current Game Status
To see Claude's current position and game state without sending any commands:

```bash
tmux capture-pane -p -e -t claude
```

### Movement Commands
Send movement commands to Claude:

```bash
./run j         # Move south
./run k         # Move north
./run h         # Move west
./run l         # Move east
./run 5j        # Move south 5 times
./run y b y     # Move northeast, southwest, northeast (diagonal movements)
```

### Command Examples
Send various commands and special keys:

```bash
./run '#quit'   # Quit game command
./run '#kick' Enter  # Kick command followed by Enter
./run Escape    # Cancel current action/menu (special key)
```

### Session Management Commands

| Command | Purpose |
|---------|---------|
| `./run --init` | Start fresh game (kills existing session) |
| `./run --cleanup` | Kill the tmux session completely |
| `./run [command]` | Send command and view current state |

## 3. Game Status Elements

When viewing the game screen, look for these key indicators:

- **`@`** - Claude's current position
- **`d`** - Slinky (Claude's pet dog)
- **`<`** - Stairs up
- **`>`** - Stairs down (mission objective!)
- **`+`** - Closed doors
- **`|`** - Open doorways
- **`#`** - Corridor passages
- **`$`** - Gold/treasure
- **`%`** - Corpses from defeated enemies
- **`:`** - Food items
- **`?`** - Scrolls

### Status Bar Information
The bottom of the screen shows:
- **Character name**: "Claude the Stripling" (Valkyrie)
- **Health**: HP current/max (e.g., "HP:16(16)")
- **Gold**: Current gold amount (e.g., "$:0")
- **Experience**: Current level (e.g., "Xp:1")
- **Dungeon Level**: Current floor (e.g., "Dlvl:1")

## 4. Common NetHack Commands via ./run

### Item Interaction
```bash
./run ','       # Pick up items
./run 'd'       # Drop items
./run 'i'       # View inventory
./run 'r'       # Read scroll
./run 'w'       # Wield weapon
```

### Exploration
```bash
./run 's'       # Search for hidden doors/traps
./run 'o'       # Open doors
./run '#kick'   # Kick doors/objects
./run '>'       # Go down stairs
./run '<'       # Go up stairs
```

### Information
```bash
./run '?'       # Help menu
./run '/'       # What is this symbol
./run ':'       # Look around
./run ';'       # Show discoveries
```

## 5. Monitoring Progress Toward Level 2

### Mission Status
Check if Claude has reached the objective:

```bash
grep -i "level 2\|stairs down\|dlvl:2" nethack_strategy.md
```

### Current Session Status
View the active tmux session:

```bash
tmux list-sessions | grep claude
```

### Interactive Monitoring
To watch Claude's moves in real-time, you can run commands and see immediate results. Each `./run` command shows the updated game state.

---

*This guide helps you interact with and monitor Claude's NetHack adventure using the new tmux-based interface!*