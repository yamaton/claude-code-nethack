# NetHack Strategy Scrapbook

## Mission Objective
Reach Dungeon Level 2 and save progress

## Current Game Status
- **Character**: Claude the Valkyrie (Human Valkyrie) - **NEW CLASS CHOICE**
- **Current Level**: Dungeon Level 1
- **Health**: Starting fresh with new character
- **Gold**: Starting fresh
- **Pet**: Starting fresh
- **Location**: Will start from beginning with new character

## Game State Analysis
From last observation:
- Character (@) is in a room with pet nearby
- Multiple doors visible ('+' symbols)
- Need to explore to find stairs down ('>')
- Standard NetHack room-and-corridor dungeon layout

## Strategy Notes

### Core Strategy
1. **Systematic Exploration**: Explore each room methodically
2. **Door Management**: Open doors to access new areas
3. **Stair Location**: Find stairs down ('>') to reach level 2
4. **Safety First**: Avoid unnecessary risks, retreat if needed
5. **Pet Management**: Keep pet alive and useful

### Movement Commands
- `h j k l` - Cardinal directions (left, down, up, right)
- `y u b n` - Diagonal directions
- `o` - Open doors (requires direction)
- `.` - Wait/rest
- `s` - Search for hidden doors/traps

### Advanced Movement Tips
- **Multi-step commands**: Can chain multiple moves by sending commands in sequence
- **Running**: Use `Shift + direction` or `g + direction` to run until something interesting
- **Go-to movement**: Use `_` (underscore) to specify coordinates and auto-travel
- **Repeat commands**: Use number prefix (e.g., `5j` = move south 5 times, `10s` = search 10 times)
- **Fast exploration**: `Ctrl + direction` for fast movement until blocked
- **Door breaking**: Use `#kick` repeatedly to break resistant doors
- **Combat commands**: Move toward enemies to attack, pets help automatically

### Key Observations
- NetHack requires directional input for door opening
- Save functionality works with 'S' command
- Screen capture shows clear ASCII representation
- Game responds well to single character commands

## Exploration Log

### Move 1 (Previous Session)
- **Action**: Opened door to the east
- **Command**: `o` followed by `l` (east direction)
- **Result**: Successfully opened door, revealed corridor
- **Status**: Game saved successfully

### Session 2: Strategic Exploration
- **Turn 1**: Attempted to open door south - "The door resists!" (door was locked/stuck)
- **Turn 2**: Moved south anyway, swapped places with Rex
- **Turn 3**: Waited to observe area
- **Turn 4**: Explored west
- **Turn 5**: Explored east
- **Turn 6**: Searched for hidden doors
- **Observation**: Currently in a small room, need to find alternative routes

### Session 3: Major Breakthrough - Large Dungeon Discovery
- **Western Door**: Successfully opened resistant door using repeated attempts
- **Combat**: Encountered and defeated jackal with Rex's help
- **Health**: Healed from 8 HP back to 10 HP (Rex ate corpse)
- **New Areas**: Discovered extensive corridor system beyond starting room
- **Treasure Room**: Found large room with gold, successfully collected
- **Eastern Door**: Opened second door revealing more corridors
- **Map Expansion**: Dungeon is much larger than initially thought

### Key Findings
- **Kicking Strategy**: Resistant doors can be opened with multiple kick attempts (`#kick`)
- **Pet Combat**: Rex actively helps fight enemies and can eat corpses for healing
- **Complex Layout**: Dungeon has interconnected rooms, corridors, and multiple exits
- **Treasure Discovery**: Large rooms contain valuable items
- **Extensive Network**: Eastern corridors connect to additional unexplored areas

## Current Challenges
1. **Stair Location**: Haven't found stairs down (>) to level 2 yet in explored areas
2. **Eastern Corridors**: Need to systematically explore the eastern passage network
3. **Hidden Features**: May need to search more areas for concealed stairs
4. **Complex Navigation**: Large dungeon requires careful mapping to avoid getting lost

## Next Steps Strategy
1. **Systematic Eastern Exploration**: Map out all eastern corridor connections
2. **Room-by-Room Search**: Check every discovered room for stairs down
3. **Hidden Passage Detection**: Use search command in promising locations
4. **Unfinished Areas**: Return to any incompletely explored sections
5. **Strategic Patience**: This level is large - stairs down are somewhere to be found

**Legend:**
- `@` = Current position (in northern corridor system)
- `<` = Stairs up (start area)
- `$` = Gold collected
- `%` = Enemy corpses
- `#` = Corridors
- `-` = Open doors
- `>` = Stairs down (TARGET - not yet found)

## Latest Discovery
Successfully reached NEW NORTHERN AREA via eastern corridor network! This is a major breakthrough - the dungeon extends much further north than initially mapped. Current position is in northern corridor system where stairs down (>) might be located.

### Session 4: MAJOR BREAKTHROUGH - Hidden Passage Discovery & Combat Death
- **Critical Observation**: User spotted discontinuous north wall in treasure room (`---------.------`)
- **Hidden Passage**: The `.` in the wall pattern indicated an opening I had completely missed!
- **New Area Access**: Successfully accessed completely unexplored area beyond north wall
- **Enemy Encounter**: Found active goblin (`o`) in new area - first new enemy type encountered
- **Combat Learning**: Engaged in melee combat using tin opener weapon
- **Critical Mistake**: Rushed into combat without assessing danger level
- **Death**: Character died (HP: 10→7→5→1→0) due to inadequate combat preparation
- **Food Discovery**: Found food items (`:`) in the new area
- **Boulder/Rock**: Spotted `o` symbol (rock/boulder) in addition to goblin

## New Combat & Survival Insights

### Combat Mechanics Learned
- **Tourist Weapon System**: Tourist class uses weak "tin opener" as starting weapon (POOR CHOICE!)
- **Valkyrie Advantage**: Human Valkyrie class has much better combat capabilities and weapons
- **Attack Method**: Moving toward enemies initiates automatic melee combat
- **Combat Messages**:
  - "You begin bashing monsters with your tin opener" (Tourist only)
  - "You miss the goblin" (attacks can fail)
  - "The goblin hits!" (enemies counter-attack)
- **Health Management**: HP drops rapidly in combat with weak weapons (lost 3 HP per goblin hit as Tourist)
- **Death Condition**: Character dies when HP reaches 0
- **Class Selection Impact**: Character class significantly affects combat effectiveness

### Critical Strategic Lessons
1. **Visual Map Reading**: Pay extreme attention to wall patterns and discontinuities
2. **Health Assessment**: Never engage combat below 6-8 HP without healing
3. **Combat Preparation**: Assess enemy strength before rushing in
4. **Save Strategy**: Should save before entering dangerous new areas
5. **Retreat Option**: Should have retreated when HP dropped to 5
6. **Area Scanning**: Search new areas for threats before full exploration
7. **Class Selection**: Choose combat-effective classes for dangerous exploration

### Valkyrie Class Advantages (NEW CHARACTER CHOICE)
- **Superior Combat**: Valkyries are warrior class with much better fighting ability
- **Better Weapons**: Start with proper weapons instead of weak "tin opener"
- **Higher HP**: Typically have more hit points than Tourists
- **Combat Skills**: Natural fighting abilities and weapon proficiencies
- **Survivability**: Much better chance against early-game enemies like goblins
- **Exploration Safety**: Can handle unexpected encounters more effectively
- **Why Switch**: Tourist class proved inadequate for combat encounters

### Hidden Area Discovery Method
- **Wall Pattern Analysis**: Look for `.` symbols interrupting `---` wall patterns
- **Visual Inspection**: Treasure room north wall showed `---------.------` pattern
- **Access Method**: Move directly toward the discontinuous wall section
- **New Area Significance**: Hidden areas likely contain important features (stairs down!)

## Updated Current Challenges
1. **NEW CHARACTER**: Start fresh with Human Valkyrie (much better combat class)
2. **Rapid Navigation**: Use map knowledge to quickly reach the hidden area
3. **Combat Advantage**: Valkyrie should handle goblin much more effectively
4. **Area Exploration**: Systematically explore the goblin area for stairs down (>)
5. **Strategic Approach**: Apply learned lessons with better character class

## Updated Map Knowledge
```
Starting Area:          Large Treasure Room:     Eastern Corridors:     Hidden Northern Area:
-----                   ---------                ### (explored)         (NEWLY DISCOVERED!)
|<...:                  |.......|                ###                    ---------.------
|...|                   |....$..|-##             ###                    |.......o......|  <- GOBLIN AREA!
   .  #   |..%|         |.......|                ###                    |............:.|  <- FOOD HERE
   ####-...|            |......@|                ###                    |..............|
   # #-----             ---------                ###                    ----------------
   #                            ^                ###
 ###                     HIDDEN OPENING!        ###
```

**New Legend Additions:**
- `o` = Enemies (goblin) OR rocks/boulders
- `:` = Food items
- `---------.------` = Wall with hidden opening (look for `.` in wall patterns!)

## Session 5: MAJOR BREAKTHROUGH - Interface Improvements & Large Western Room Discovery

### Advanced Navigation Techniques Learned
- **Door Symbol Recognition**:
  - `-` in walls = open door (horizontal)
  - `|` in walls = open door (vertical)
  - `+` = closed door (requires opening with `o` command)
- **Wall Opening Pattern Analysis**:
  - `-----.---` indicates opening is one step south-west from current position
  - Must move diagonally to access wall openings (not just cardinal directions)
  - Opening position corresponds to `.` symbol in wall pattern

### Major Exploration Success
- **Western Room Discovery**: Found and opened closed door `+` leading to large western room
- **Systematic Corridor Mapping**: Successfully mapped complex interconnected corridor system
- **Strategic Door Opening**: Used `o h` command to open western door, revealing major new area
- **Room Access Method**: Proper positioning to enter rooms through doorways

### Combat Experience with Valkyrie
- **Newt Encounter**: Successfully handled newt combat (enemy was disguised as `:` food symbol)
- **Pet Combat Assistance**: Slinky (pet dog) actively helps in combat and eats corpses
- **Valkyrie Effectiveness**: Much better combat performance than Tourist class

### Updated Navigation Commands
- **Room Entry**: Position at exact door location before moving through
- **Diagonal Movement**: Use `b` (south-west), `y` (north-west), etc. for diagonal access to wall openings
- **Door Operations**: `o` + direction to open closed doors (`+`)
- **Pet Coordination**: `swap places` messages indicate successful pet movement

### Current Status: Ready for Stairs Discovery
- **Location**: Inside large western room (prime location for stairs down)
- **Mission Progress**: Systematically explored majority of dungeon level 1
- **Next Step**: Search western room floor-by-floor for stairs down (`>`) to level 2
- **Key Achievement**: Clean interface + advanced navigation = much more efficient exploration

**Legend Updates:**
- `+` = Closed doors (requires opening)
- `-` and `|` = Open doors in walls
- `####` = Complex corridor networks
- `-----.---` = Wall with opening (move diagonally to `.` position)

---
*Last Updated: After Interface Improvements & Western Room Discovery*