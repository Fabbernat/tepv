import sys


def all_characters_are_unique(s: str) -> bool:
    return len(s) == len(set(s))


def filter_names(names: list) -> list:
    valid_names = [name for name in names if len(name) >= 5 and all_characters_are_unique(name)]
    if not valid_names:
        return []

    min_length = min(map(len, valid_names))
    return [name for name in valid_names if len(name) == min_length]


def main():
    n = int(sys.stdin.readline().strip())
    names = [sys.stdin.readline().strip() for _ in range(n)]
    # print(names)

    filtered_names = filter_names(names)

    if filtered_names:
        print(max(filtered_names))
    else:
        print("Nincs")

if __name__ == '__main__':
    main()
