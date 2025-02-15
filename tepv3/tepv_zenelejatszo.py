from sys import stdin

class Song:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.p = 0

def solve():
    q = int(stdin.readline())
    pl = []
    s = {}

    for _ in range(q):
        ln = stdin.readline().split()
        op = ln[0]

        if op == 'L':
            n, d = ln[1], int(ln[2])
            if n in s:
                try:
                    pl.remove(s[n])
                except ValueError:
                    pass
            ns = Song(n, d)
            pl.insert(0, ns)
            s[n] = ns

        elif op == 'P':
            t = int(ln[1])
            if pl:
                total_duration = sum(song.d for song in pl)
                if total_duration > 0:
                    complete_cycles = t // total_duration
                    remainder = t % total_duration

                    for song in pl:
                        song.p += complete_cycles

                    cum_duration = 0
                    for song in pl:
                        cum_duration += song.d
                        if remainder >= cum_duration:
                            song.p += 1
                        elif remainder > cum_duration - song.d:
                            song.p += 1

        else:
            n = ln[1]
            print(s[n].p if n in s else 0)

if __name__ == "__main__":
    solve()
