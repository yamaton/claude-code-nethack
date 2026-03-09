#!/usr/bin/env python3
"""Extract the map region from NetHack screen output and print its transpose.

In the original map: left-right = West-East, top-bottom = North-South.
In the transposed map: left-right = North-South, top-bottom = West-East.

This helps LLMs recognize vertical (N/S) neighbors by placing them
on the same row, where token-level adjacency makes recognition easy.
"""

import sys

MAP_WIDTH = 80


STATUS_MARKERS = ["Dlvl:", "HP:", "Pw:", "AC:", "Xp:"]


def is_status_line(line):
    return any(m in line for m in STATUS_MARKERS)


def is_map_line(line):
    """Heuristic: map lines contain wall, corridor, or dungeon feature characters."""
    s = line.strip()
    if not s:
        return False
    has_wall = "|" in s or ("--" in s and not s.startswith("--More"))
    has_corridor = "#" in s
    has_player = "@" in s
    has_stairs = ">" in s or "<" in s
    return has_wall or has_corridor or has_player or has_stairs


def extract_map(lines):
    """Return the contiguous map region as a list of strings.

    Lines are clipped to MAP_WIDTH characters to exclude any overlay text
    (inventory, menus) that NetHack renders to the right of the map area.
    """
    first = None
    last = None
    for i, line in enumerate(lines):
        if is_status_line(line):
            continue
        if is_map_line(line[:MAP_WIDTH]):
            if first is None:
                first = i
            last = i
    if first is None:
        return []
    return [line[:MAP_WIDTH].rstrip() for line in lines[first : last + 1]]


WALL_SWAP = str.maketrans("|-", "-|")


def transpose(map_lines):
    """Transpose a list of strings (swap rows and columns).

    Wall characters are swapped (| <-> -) so their visual orientation
    stays consistent after the rotation.
    """
    if not map_lines:
        return []
    max_len = max(len(line) for line in map_lines)
    padded = [line.ljust(max_len) for line in map_lines]
    result = []
    for col in range(max_len):
        row = "".join(padded[r][col] for r in range(len(padded)))
        result.append(row.rstrip().translate(WALL_SWAP))
    # Trim empty lines from ends
    while result and not result[-1].strip():
        result.pop()
    while result and not result[0].strip():
        result.pop(0)
    return result


def find_player(map_lines):
    """Find the (row, col) position of @ in the map, or None."""
    for r, line in enumerate(map_lines):
        c = line.find("@")
        if c != -1:
            return r, c
    return None


def cell_at(map_lines, r, c):
    """Get the character at (r, c), or space if out of bounds."""
    if 0 <= r < len(map_lines) and 0 <= c < len(map_lines[r]):
        return map_lines[r][c]
    return " "


def print_neighborhood(map_lines):
    """Print a 5x5 grid around @ and label the 8 adjacent cells."""
    pos = find_player(map_lines)
    if pos is None:
        return
    pr, pc = pos
    # 5x5 visual grid
    print("--- Neighborhood of @ ---")
    for dr in range(-2, 3):
        cells = " ".join(cell_at(map_lines, pr + dr, pc + dc) for dc in range(-2, 3))
        if dr == 0:
            print(f"W {cells} E")
        else:
            print(f"  {cells}")
    # Labeled 3x3
    labels = [
        ("NW", -1, -1), ("N", -1, 0), ("NE", -1, 1),
        ("W", 0, -1), ("E", 0, 1),
        ("SW", 1, -1), ("S", 1, 0), ("SE", 1, 1),
    ]
    print(" ".join(f"{d}={cell_at(map_lines, pr+dr, pc+dc)}" for d, dr, dc in labels))


def main():
    lines = sys.stdin.read().splitlines()
    map_lines = extract_map(lines)
    pos = find_player(map_lines) if map_lines else None
    if not map_lines or pos is None:
        return
    transposed = transpose(map_lines)
    if transposed:
        print("--- Transposed Map (left-right = N-S, top-bottom = W-E) ---")
        for line in transposed:
            print(line)
    print_neighborhood(map_lines)


if __name__ == "__main__":
    main()
