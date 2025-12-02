#!/usr/bin/env python3

def is_invalid_id(n):
    s = str(n)
    if s[0] == '0':
        return False
    L = len(s)
    for l in range(1, L // 2 + 1):
        if L % l != 0:
            continue
        repeat_count = L // l
        if s[:l] * repeat_count == s:
            return True
    return False

def sum_invalid_ids(ranges_line):
    total = 0
    ranges = ranges_line.strip().split(',')
    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 giftshop_invalid_ids_part2.py <input-file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        line = f.readline()
    print(sum_invalid_ids(line))
