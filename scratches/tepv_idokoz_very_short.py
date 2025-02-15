from sys import stdin

t = lambda s: int(s[:2]) * 60 + int(s[3:])
a, b = map(t, stdin.read().split())
print((b - a) % 1440)
