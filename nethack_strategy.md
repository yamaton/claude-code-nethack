# NetHack Strategy Scrapbook

*A comprehensive learning log and knowledge base for Claude Code NetHack gameplay. This document serves two purposes: (1) tracking progress and discoveries in current sessions, and (2) accumulating general NetHack knowledge for future Claude sessions.*

## Current Mission Objective
Reach Dungeon Level 2 and save progress

## How to Use This Scrapbook
- **Current Session Info**: Updates for active gameplay progress
- **General Knowledge**: Timeless NetHack mechanics and strategies  
- **Learning Log**: What works, what doesn't, lessons learned
- **Future Reference**: Insights for subsequent Claude sessions

# CURRENT SESSION STATUS

## Active Game State (Current Valkyrie Run)
- **Character**: Claude the Valkyrie (Human Valkyrie, Lawful)  
- **Level**: Dungeon Level 1
- **Health**: 16/16 HP (full health)
- **Gold**: 7 pieces
- **Pet**: Rex (kitten/cat)
- **Equipment**: Scroll labeled ELAM EBOW
- **Location**: Western corridor system, exploring for stairs down

## Current Dungeon Layout (This Run Only)
- **Starting Room**: Contains fountain (F) and stairs up (<)
- **Corridor System**: Extensive ### passage networks, interconnected
- **Rooms Found**: Southwestern room with walls (------), collected 7 gold
- **Combat History**: Defeated newt, sewer rat, grid bug successfully
- **Items Found**: Multiple scrolls (Rex keeps finding and dropping them)
- **Objective**: Find stairs down (>) - location unknown in this specific layout

## Immediate Next Steps
1. Continue systematic exploration of unexplored corridor branches
2. Search each room thoroughly for stairs down (>)
3. Use search command (`s`) to find potential hidden passages
4. Check any areas missed in initial exploration

---

# GENERAL NETHACK KNOWLEDGE BASE

*Timeless insights applicable to all NetHack sessions*

## Character Classes & Selection

### Valkyrie Class (RECOMMENDED)
- **Combat**: Excellent fighting ability, proper weapons from start
- **HP**: Higher hit points than other classes (16 starting HP)
- **Stats**: Strong (17 Str), good constitution, decent dexterity
- **Survivability**: Can handle early-game enemies effectively
- **Why Choose**: Much better than Tourist for dungeon exploration

### Tourist Class (NOT RECOMMENDED)
- **Weakness**: Starts with "tin opener" weapon (very weak)
- **Low Combat**: Poor fighting ability, loses HP quickly in combat
- **Experience**: Previous Tourist character died to goblin due to inadequate weapons

## Movement & Navigation

### Basic Commands
- `h j k l` - Cardinal directions (west/south/north/east)
- `y u b n` - Diagonal directions
- `o` + direction - Open doors (requires direction)
- `.` - Wait/rest
- `s` - Search for hidden doors/traps
- `,` - Pick up items

### Advanced Navigation
- **Multi-step**: Chain commands like `./run h j k l` for sequential moves
- **Door Operations**: Position at door before using `o` + direction
- **Room Entry**: Must be at exact door location to enter rooms
- **Diagonal Access**: Use diagonals for wall openings and corners

## Combat System

### Combat Mechanics
- **Attack Method**: Move toward enemies to initiate automatic melee combat
- **Pet Assistance**: Pets actively help fight and eat corpses for healing
- **Health Management**: Monitor HP carefully, retreat when low
- **Combat Messages**: Pay attention to hit/miss messages

### Enemy Types Encountered
- **Newt**: Weak enemy, easily defeated by Valkyrie
- **Sewer Rat**: Moderate threat, can bite for damage
- **Grid Bug**: Minor enemy, manageable with Valkyrie

## Dungeon Exploration

### Core Strategy
1. **Systematic Approach**: Explore every accessible area methodically
2. **Room-by-Room**: Check each room thoroughly for stairs down (>)
3. **Corridor Mapping**: Follow all ### passages to completion
4. **Hidden Features**: Use search command in promising locations

### Critical Insight: Random Layouts
- **Key Fact**: Each NetHack game generates completely different dungeon layouts
- **Implication**: Previous session maps and room locations do NOT apply
- **Strategy**: Always explore systematically without layout assumptions

## Hidden Passage Discovery

### Visual Pattern Recognition
- **Wall Discontinuities**: Look for `.` symbols in `---` wall patterns
- **Search Command**: Use `s` against walls and in corners
- **Room Perimeters**: Examine all room walls carefully
- **Diagonal Movement**: Access wall openings with diagonal commands

## Item Management

### Items & Symbols
- `$` = Gold pieces (collect for score/purchases)
- `?` = Scrolls (various magical effects)
- `F` = Fountain (in starting room)
- `<` = Stairs up (return to previous level)
- `>` = Stairs down (TARGET - leads to next level)
- `:` = Food items
- `%` = Corpses (pet food)

### Pet Behavior
- **Combat Help**: Pets assist in fighting enemies
- **Item Finding**: Pets often find and drop scrolls
- **Corpse Eating**: Pets eat corpses, sometimes healing player
- **Coordination**: Use "swap places" when pet blocks movement

## Interface & Technical

### Game Interface
- **Clean Display**: ASCII representation without escape sequences
- **Save Function**: Use 'S' command to save progress
- **Command Input**: Single character commands work best
- **Error Handling**: Commands fail gracefully with informative messages

---

# CURRENT SESSION LEARNING LOG

*Insights and discoveries from the active Valkyrie session*

## Session Progress Summary
- **Character**: Successfully created Claude the Valkyrie with excellent stats
- **Exploration**: Mapped extensive corridor system with multiple room connections
- **Combat**: Defeated newt, sewer rat, and grid bug - Valkyrie proves very effective
- **Items**: Collected 7 gold pieces and scroll labeled ELAM EBOW
- **Challenge**: Still searching for stairs down (>) to reach Level 2

## Key Discoveries This Session
1. **Valkyrie Effectiveness**: Much superior combat compared to previous Tourist class
2. **Dungeon Complexity**: This layout has extensive interconnected corridors
3. **Pet Utility**: Rex actively finds items and assists in combat
4. **Room Distribution**: Multiple rooms accessible via ### corridor networks
5. **Search Pattern**: Systematic exploration reveals more areas than expected

## What's Working Well
- **Combat Strategy**: Valkyrie handles all enemies encountered easily
- **Movement**: Understanding door mechanics and room entry
- **Exploration**: Methodical corridor mapping revealing large dungeon
- **Pet Management**: Rex cooperation in combat and exploration

## Current Challenges
- **Stairs Location**: Haven't found stairs down (>) yet in explored areas
- **Dungeon Size**: Layout is larger and more complex than anticipated
- **Systematic Coverage**: Need to ensure no areas missed in exploration

## Lessons Learned (For Future Claude Sessions)
1. **Class Selection**: Always choose Valkyrie over Tourist for better combat
2. **Systematic Exploration**: Follow every corridor to completion before concluding
3. **Pet Value**: Rex is extremely helpful - let pet assist actively
4. **Search Frequency**: Use search command (`s`) more often, especially in rooms
5. **Random Layouts**: Never assume previous dungeon maps apply to new games

---

*Last Updated: Current Valkyrie Session - Structured as learning scrapbook for future Claude sessions*