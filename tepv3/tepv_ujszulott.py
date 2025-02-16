def f(n, b, d):
    c = 0
    while n > 0:
        if n % b == d:
            c += 1
        n //= b
    return c


def main():
    n, d = map(int, input().split())
    m = 0

    # Handle small n cases (same as before)
    for b in range(max(2, d + 1), min(n, 10 ** 6) + 1):
        if d >= b:
            continue
        m = max(m, f(n, b, d))

    # Handle large n cases: check bases close to n
    if n > 10 ** 6:  # Only do this if n is large.
        for b in range(max(2, d + 1), min(n, int(n ** 0.5) * 100) + 1):
            if d >= b:
                continue
            m = max(m, f(n, b, d))

        for b in range(max(2, d + 1), min(n, int(n / 2) + 1) + 1):
            if d >= b:
                continue
            m = max(m, f(n, b, d))

        for b in range(max(n - 1000, 2), n + 1):  # Check bases very close to n
            if b < d + 1:
                continue
            m = max(m, f(n, b, d))

    print(m)


if __name__ == "__main__":
    main()