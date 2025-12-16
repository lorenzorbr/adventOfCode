def load_ranges(path):
    ranges = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                break  # stop at blank line
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
    return ranges


def count_fresh_ids(ranges):
    if not ranges:
        return 0

    # Sort by start
    ranges.sort()

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            # Overlapping or adjacent → merge
            current_end = max(current_end, end)
        else:
            # Disjoint → finalize previous range
            total += current_end - current_start + 1
            current_start, current_end = start, end

    # Add final range
    total += current_end - current_start + 1

    return total


if __name__ == "__main__":
    ranges = load_ranges("input.txt")
    result = count_fresh_ids(ranges)
    print(result)
