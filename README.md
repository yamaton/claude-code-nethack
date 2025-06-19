# Claude Code NetHack Project

This project enables Claude Code to autonomously play NetHack through a tmux-based interface, with comprehensive strategy tracking and gameplay documentation.

## Overview

NetHack is a classic roguelike dungeon crawler that requires strategic thinking, exploration, and tactical combat decisions. This project provides Claude Code with:

- **Persistent game sessions** via tmux for uninterrupted gameplay
- **Strategic documentation** with real-time decision tracking
- **Clean command interface** for sending game inputs and capturing output
- **Learning progression** that improves gameplay over multiple sessions

## Project Components

### Core Interface
- **`./run`** - Main script for NetHack interaction and session management
  - Manages persistent tmux sessions
  - Sends commands with configurable delays
  - Captures clean ASCII output without escape sequences
  - Supports session cleanup and initialization

### Documentation
- **`nethack_strategy.md`** - Comprehensive strategy scrapbook
  - Mission objectives and progress tracking
  - Detailed exploration logs with move-by-move analysis
  - Combat encounters and tactical lessons learned
  - Map discoveries and dungeon layout documentation
  - Character development and class optimization notes

- **`gameplay_guide.md`** - User interface reference
  - Command syntax and usage examples
  - Game element identification guide
  - Session monitoring and management instructions
  - NetHack mechanics explained for observers

## Current Mission

**Objective**: Navigate Claude (Human Valkyrie) from Dungeon Level 1 to Level 2

**Progress**:
- Successfully explored majority of Level 1 dungeon
- Discovered hidden passages and complex room networks
- Learned advanced combat mechanics through trial and error
- Currently positioned in western room searching for stairs down

## Key Features

### Intelligent Gameplay
- **Strategic character selection**: Evolved from Tourist to Valkyrie for better combat effectiveness
- **Systematic exploration**: Room-by-room mapping with pattern recognition
- **Combat learning**: Tactical improvements based on previous encounters
- **Hidden feature discovery**: Wall pattern analysis to find secret passages

### Technical Implementation
- **Session persistence**: Games survive between command sessions
- **Clean output**: Monochrome ASCII without terminal escape sequences
- **Command batching**: Multiple moves can be sent sequentially
- **Error handling**: Robust session management with cleanup options

### Documentation Excellence
- **Real-time strategy updates**: Every significant decision documented
- **Technical insights**: NetHack mechanics learned through experimentation
- **Progress tracking**: Clear mission status and next steps
- **Learning evolution**: Shows genuine improvement in gameplay understanding

## Quickstart for Claude Code

### What to Tell Claude Code
When starting a new session, users should say:
```
Continue playing NetHack. Check documents in this project, then proceed with the mission to reach Level 2.
```


### Getting Started
1. **Initialize game**: `./run --init` to start fresh session
2. **Check current state**: `./run` (no arguments) to see game screen
3. **Review strategy**: Read `nethack_strategy.md` for current mission status and learned tactics
4. **Basic movement**: Use `./run h j k l` for west/south/north/east movement
5. **Door interaction**: Use `./run o` + direction to open doors (`+` symbols)
6. **Search areas**: Use `./run s` to find hidden doors/passages
7. **Mission goal**: Find stairs down (`>`) to reach Level 2

### Essential Commands for Gameplay
```bash
./run                   # View current state
./run h j k l           # Cardinal movement (west/south/north/east)
./run y u b n           # Diagonal movement
./run o h               # Open door to the west
./run s                 # Search for hidden features
./run ,                 # Pick up items
./run >                 # Go down stairs (when found)
```

### Strategy Reference
- Current character: Claude the Valkyrie (Human) - combat-effective class
- Pet: Slinky (dog) - helps in combat, eats corpses
- Mission: Systematic exploration to find stairs down (`>`)
- Key lesson: Look for wall discontinuities (`.` in `---` patterns) for hidden passages

## Usage

### Session Management
```bash
./run --init            # Start fresh game session
./run --cleanup         # End current session
```

### Monitoring Progress
```bash
# Display game in progress with read-only mode
tmux attach-session -t claude-nethack -r
```

## Project Evolution

This project demonstrates AI learning through gameplay:

1. **Initial Phase**: Basic movement and door opening
2. **Exploration Phase**: Systematic room mapping and corridor navigation
3. **Combat Phase**: Enemy encounters leading to character optimization
4. **Advanced Phase**: Hidden passage discovery and complex navigation
5. **Current Phase**: Strategic room-by-room search for mission completion

The documentation shows genuine learning progression, with Claude Code adapting strategies based on gameplay outcomes and developing increasingly sophisticated approaches to NetHack's challenges.

---

*A demonstration of AI autonomous gameplay with comprehensive strategy documentation and technical implementation.*