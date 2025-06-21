#!/usr/bin/env python3
"""
Extract 3x3 grid around the player character from NetHack output.
Usage: ./run | python3 grid_extract.py <player_char>
Example: ./run | python3 grid_extract.py @
"""

import sys

def find_player_position(lines, player_char):
    """Find the row and column position of the specified player character."""
    for row_idx, line in enumerate(lines):
        col_idx = line.find(player_char)
        if col_idx != -1:
            return row_idx, col_idx
    return None, None

def extract_3x3_grid(lines, player_row, player_col):
    """Extract 3x3 grid centered on player position."""
    grid = {}
    directions = {
        'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
        'W':  (0, -1),  'P': (0, 0),  'E':  (0, 1),
        'SW': (1, -1),  'S': (1, 0),  'SE': (1, 1)
    }

    for direction, (row_offset, col_offset) in directions.items():
        target_row = player_row + row_offset
        target_col = player_col + col_offset

        if (0 <= target_row < len(lines) and
            0 <= target_col < len(lines[target_row])):
            grid[direction] = lines[target_row][target_col]
        else:
            grid[direction] = '?'  # Out of bounds marker

    return grid

def main():
    if len(sys.argv) != 2:
        print("Usage: ./run | python3 grid_extract.py <player_char>")
        print("Example: ./run | python3 grid_extract.py @")
        sys.exit(1)

    player_char = sys.argv[1]

    input_text = sys.stdin.read()
    lines = input_text.split('\n')

    player_row, player_col = find_player_position(lines, player_char)

    if player_row is None:
        print(f"Error: Could not find player character '{player_char}' in the input")
        sys.exit(1)

    grid = extract_3x3_grid(lines, player_row, player_col)

    print(f"3x3 Grid around player ({player_char}):")
    print(f"NW:'{grid['NW']}' | N:'{grid['N']}' | NE:'{grid['NE']}'")
    print(f"W:'{grid['W']}'  | P:'{grid['P']}' | E:'{grid['E']}'")
    print(f"SW:'{grid['SW']}' | S:'{grid['S']}' | SE:'{grid['SE']}'")

if __name__ == "__main__":
    main()