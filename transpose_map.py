#!/usr/bin/env python3
"""Extract the map region from NetHack screen output and print its transpose.

In the original map: left-right = West-East, top-bottom = North-South.
In the transposed map: left-right = North-South, top-bottom = West-East.

This helps LLMs recognize vertical (N/S) neighbors by placing them
on the same row, where token-level adjacency makes recognition easy.
"""

import sys


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


def transpose(map_lines):
    """Transpose a list of strings (swap rows and columns)."""
    if not map_lines:
        return []
    max_len = max(len(line) for line in map_lines)
    padded = [line.ljust(max_len) for line in map_lines]
    result = []
    for col in range(max_len):
        row = "".join(padded[r][col] for r in range(len(padded)))
        result.append(row.rstrip())
    # Trim empty lines from ends
    while result and not result[-1].strip():
        result.pop()
    while result and not result[0].strip():
        result.pop(0)
    return result


def main():
    lines = sys.stdin.read().splitlines()
    map_lines = extract_map(lines)
    if not map_lines:
        return
    transposed = transpose(map_lines)
    if not transposed:
        return
    print("--- Transposed Map (left-right = N-S, top-bottom = W-E) ---")
    for line in transposed:
        print(line)


if __name__ == "__main__":
    main()
