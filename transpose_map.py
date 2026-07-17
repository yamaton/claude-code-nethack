#!/usr/bin/env python3
"""Format NetHack screen output for LLM consumption.

Processes raw tmux capture output into:
1. Map area (left 80 columns) with blank lines squeezed
2. Neighborhood of @ (5x5 grid + labeled 3x3)
3. Overlay text (inventory, menus from right of column 80)
"""

import re
import sys

MAP_WIDTH = 80

GAP_RE = re.compile(r" {2,}")

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


def split_output(lines):
    """Split each line into map area (left) and overlay text (right).

    NetHack's dungeon map never extends past MAP_WIDTH, so anything beyond
    it is a menu/status overlay. Popup boxes are sometimes positioned a few
    columns before MAP_WIDTH, though, so a straight cut there can slice a
    menu word in half (e.g. "Coins" -> "Co" + "ins"). Instead, split at the
    start of the rightmost run of 2+ spaces that ends at or before
    MAP_WIDTH, which is the actual gap between map content and the overlay.

    Returns (map_area_lines, overlay_lines) where overlay_lines contains
    only non-empty text found beyond the split point.
    """
    map_area = []
    overlay = []
    for line in lines:
        split_at = MAP_WIDTH
        if len(line) > MAP_WIDTH:
            gap_ends = [m.end() for m in GAP_RE.finditer(line) if m.end() <= MAP_WIDTH]
            if gap_ends:
                split_at = max(gap_ends)
        map_area.append(line[:split_at].rstrip())
        right = line[split_at:].strip()
        if right:
            overlay.append(right)
    return map_area, overlay


def squeeze_blanks(lines):
    """Collapse consecutive blank lines into a single blank line."""
    result = []
    prev_blank = False
    for line in lines:
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        result.append(line)
        prev_blank = is_blank
    return result


def extract_map(lines):
    """Return the contiguous map region as a list of strings."""
    first = None
    last = None
    for i, line in enumerate(lines):
        if is_status_line(line):
            continue
        if is_map_line(line):
            if first is None:
                first = i
            last = i
    if first is None:
        return []
    return lines[first : last + 1]


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
    print("--- Neighborhood of @ ---")
    for dr in range(-2, 3):
        cells = " ".join(cell_at(map_lines, pr + dr, pc + dc) for dc in range(-2, 3))
        if dr == 0:
            print(f"W {cells} E")
        else:
            print(f"  {cells}")
    labels = [
        ("NW", -1, -1), ("N", -1, 0), ("NE", -1, 1),
        ("W", 0, -1), ("E", 0, 1),
        ("SW", 1, -1), ("S", 1, 0), ("SE", 1, 1),
    ]
    print(" ".join(f"{d}={cell_at(map_lines, pr+dr, pc+dc)}" for d, dr, dc in labels))


def main():
    raw_lines = sys.stdin.read().splitlines()
    map_area, overlay = split_output(raw_lines)

    # 1. Print map area with squeezed blank lines
    for line in squeeze_blanks(map_area):
        print(line)

    # 2. Neighborhood (only when @ is visible)
    extracted = extract_map(map_area)
    if extracted and find_player(extracted):
        print_neighborhood(extracted)

    # 3. Overlay text (inventory, menus, etc.)
    if overlay:
        print("--- Text Panel ---")
        for line in overlay:
            print(line)


if __name__ == "__main__":
    main()
