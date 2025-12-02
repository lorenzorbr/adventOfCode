#!/usr/bin/env python3

def count_zeros_during_rotations(lines):
    pos = 50
    zeros = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        dirc = line[0].upper()
        dist = int(line[1:])
        if dirc == 'R':
            for _ in range(dist):
                pos = (pos + 1) % 100
                if pos == 0:
                    zeros += 1
        else:  # L
            for _ in range(dist):
                pos = (pos - 1) % 100
                if pos == 0:
                    zeros += 1
    return zeros

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 part2_zero_rotations.py <input-file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    print(count_zeros_during_rotations(lines))
