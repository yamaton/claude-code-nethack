# Claude Code Plays NetHack

## Mission
Explore the dungeon, descend levels, survive. Current goal: reach Dungeon Level 2+.

## How to Play

### Running the Game
- `./run --init` — start a fresh game (kills existing session)
- `./run` — view current game state (no input sent)
- `./run h j k l` — send commands (west/south/north/east)
- `./run --cleanup` — kill the tmux session

During `--init`, you must manually select the character:
pick `v` (Valkyrie), `h` (human), `l` (lawful), `y` (confirm).
The `-p valkyrie` flag in the script does NOT work reliably.

### Output Format
`./run` prints two things:
1. **Original map** — standard NetHack ASCII display + status bar
2. **Transposed map** — the map rotated 90 degrees (see below)

### Reading the Transposed Map
LLMs read text left-to-right within a row far better than they read vertically across rows. The transposed map swaps rows and columns so that:
- **Left-to-right** in each transposed row = **North-to-South** in the original
- **Top-to-bottom** across transposed rows = **West-to-East** in the original

To identify the 8-cell neighborhood of `@`:
- **W and E**: read directly from the original map (same row as `@`)
- **N and S**: read from the transposed map (same row as `@`, left=N, right=S)
- **Diagonals**: cross-reference adjacent rows in the transposed map at the N/S offsets

### Key Commands
- `h j k l` — move W/S/N/E
- `y u b n` — move NW/NE/SW/SE
- `o` + direction — open a door
- `s` — search for hidden doors/passages (repeat multiple times)
- `,` — pick up item
- `>` — descend stairs (must be standing on `>`)
- `S` — save and quit
- `.` — wait one turn
- `i` — inventory
- `/` — look at things (opens a submenu, see below)
- `Space` — dismiss "--More--" prompts
- `Escape` — cancel a command

### The `/` (Look) Command
Use `./run '/' <option>` to query the map. Options:
- `o` — nearby objects (e.g. `./run '/' o`)
- `O` — all objects shown on map
- `m` — nearby monsters
- `M` — all monsters shown on map
- `i` — something you're carrying
- `?` — identify a symbol by typing it

Output shows items/monsters with their map coordinates. Dismiss with `Space`.
Use this regularly for situational awareness instead of building custom tools.

### Map Symbols
- `@` — player (Claude)
- `d` / `f` — pet (dog / cat)
- `.` — floor
- `#` — corridor
- `-` — horizontal wall
- `\|` — vertical wall (NOTE: escape as `\|` in markdown tables!)
- `+` — closed door
- `<` — stairs up
- `>` — stairs down (descend target)
- `$` — gold
- `?` — scroll
- `!` — potion
- `)` — weapon
- `[` — armor
- `%` — corpse / food

## Gameplay Knowledge

### Character: Always Pick Valkyrie
- Excellent starting stats (18+ Str, 18 Con, 16 HP)
- Strong melee combat from the start
- Tourist is terrible — weak weapon, low survivability

### Dungeon Exploration
- Every game has a randomly generated layout; never assume previous maps apply
- Explore systematically: clear each room, follow every corridor
- Use `s` (search) repeatedly near walls to find hidden doors/passages
- Look for wall discontinuities (`.` symbols breaking `---` patterns)
- Small starting rooms often have hidden exits — search all walls

### Combat
- Move into enemies to attack (automatic melee)
- Pets help fight and eat corpses
- Monitor HP; retreat when low
- Early enemies (newt, sewer rat, grid bug) are easy for Valkyrie

### Formatting Pitfall
When writing markdown tables that contain the pipe character `|`, always escape it as `\|`. Otherwise the table rendering breaks and the cell appears empty.
