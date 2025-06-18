# NetHack Gameplay Guide: Viewing History and Status

This guide explains how to monitor Claude's NetHack gameplay progress and current game status.

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

## 2. Viewing Current Game Status

### Quick Status Check
To see Claude's current position and game state:

```bash
uv run python -c "
from claude_interface import start_game
interface = start_game()
if interface:
    interface.view_state()
    interface.save_and_exit()
"
```

### Detailed Game Information
For comprehensive current status including character stats:

```bash
uv run python -c "
from claude_interface import start_game
interface = start_game()
if interface:
    print('=== CURRENT GAME STATUS ===')
    interface.view_state()
    print('\n=== CHARACTER INFO ===')
    print('Health, gold, and level info visible in status bar')
    interface.save_and_exit()
"
```

### Available Interface Commands
Claude uses a simple interface with these key methods:

| Command | Purpose |
|---------|---------|
| `interface.view_state()` | Display current game screen |
| `interface.send_move('command')` | Send a command to NetHack |
| `interface.save_and_exit()` | Save progress and close game |

### Game Status Elements

When viewing the game screen, look for these key indicators:

- **`@`** - Claude's current position
- **`f`** - Rex (Claude's pet companion)
- **`<`** - Stairs up
- **`>`** - Stairs down (mission objective!)
- **`+`** - Closed doors
- **`-`** - Open doors
- **`#`** - Corridor passages
- **`$`** - Gold/treasure
- **`%`** - Corpses from defeated enemies
- **`:`** - Food items

### Status Bar Information
The bottom of the screen shows:
- **Character name**: "Claude the Rambler"
- **Health**: HP current/max (e.g., "HP:10(10)")
- **Gold**: Current gold amount (e.g., "$:241")
- **Experience**: Current level (e.g., "Xp:1")
- **Dungeon Level**: Current floor (e.g., "Dlvl:1")

## 3. Monitoring Progress Toward Level 2

### Mission Status
Check if Claude has reached the objective:

```bash
grep -i "level 2\|stairs down\|dlvl:2" nethack_strategy.md
```

### Current Challenges
See what obstacles Claude is currently facing:

```bash
grep -A 5 -i "challenge\|problem\|next step" nethack_strategy.md
```

## 4. Interactive Monitoring

### Watch Live Gameplay
To observe Claude making moves in real-time, you can run the interface and see the screen updates as commands are sent.

### Save File Location
NetHack automatically saves progress. The save file persists between sessions, allowing Claude to continue from where they left off.

---

*This guide helps you stay informed about Claude's NetHack adventure as they work toward reaching Dungeon Level 2!*