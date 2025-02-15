from sys import stdin


def atvalt(N, base, D):
    if N == 0:
        return 1 if D == 0 else 0

    count = 0
    num = N

    while num > 0:
        digit = num % base
        if digit == D:
            count += 1
        num //= base

    return count


def main():
    N = int(stdin.readline().strip())
    D = int(stdin.readline().strip())

    total_count = 0
    for i in range(2, N + 1):
        total_count += atvalt(N, i, D)

    print(total_count)


if __name__ == '__main__':
    main()
