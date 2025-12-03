def max_joltage_for_bank(bank: str) -> int:
    """
    Given a string of digits (a battery bank), return the maximum
    two-digit number formed by choosing two batteries in order.
    """
    digits = list(map(int, bank.strip()))
    best = 0

    # choose digit i first, digit j second, i < j
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            value = digits[i] * 10 + digits[j]
            if value > best:
                best = value

    return best


def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            if line.strip():
                total += max_joltage_for_bank(line)

    print("Total output joltage:", total)


if __name__ == "__main__":
    main()
