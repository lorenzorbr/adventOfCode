#!/usr/bin/env python3
import sys

def count_zeros(lines):
    pos = 50
    zeros = 0
    for line in lines:
        line = line.strip()
        if not line: 
            continue
        dirc = line[0].upper()
        try:
            dist = int(line[1:])
        except ValueError:
            continue
        if dirc == 'R':
            pos = (pos + dist) % 100
        else:  # assume 'L'
            pos = (pos - dist) % 100
        if pos == 0:
            zeros += 1
    return zeros

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 count_zero_rotations.py <input-file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    print(count_zeros(lines))
