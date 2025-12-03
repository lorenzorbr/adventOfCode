def max_k_digits(bank: str, k: int = 12) -> int:
    """
    Given a string 'bank' of digits, choose exactly k digits in order
    to form the lexicographically largest possible number.
    """
    digits = list(map(int, bank.strip()))
    drop = len(digits) - k  # how many digits we are allowed to remove
    stack = []

    for d in digits:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)

    # If we didn't drop enough, truncate from the end
    result_digits = stack[:k]

    # Convert list of digits to integer
    value = int("".join(str(x) for x in result_digits))
    return value


def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                total += max_k_digits(line, 12)

    print("Total output joltage:", total)


if __name__ == "__main__":
    main()
