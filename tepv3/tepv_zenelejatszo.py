class Song:
    def __init__(self, title, length):
        self.title = title
        self.length = length
        self.plays = 0

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        self.songs.insert(0, song)

    def play(self, duration):
        played_time = 0
        i = 0
        while played_time < duration:
            if i >= len(self.songs):
                i = 0
            song = self.songs[i]
            if played_time + song.length <= duration:
                played_time += song.length
                song.plays += 1
            else:
                song.plays += (duration - played_time) / song.length
                played_time = duration
            i += 1

    def get_plays(self, title):
        for song in self.songs:
            if song.title == title:
                return song.plays
        return 0

# Input handling
Q = int(input())
playlist = Playlist()

for _ in range(Q):
    operation = input().split()
    if operation[0] == 'L':
        title, length = operation[1], int(operation[2])
        playlist.add_song(Song(title, length))
    elif operation[0] == 'P':
        duration = int(operation[1])
        playlist.play(duration)
    elif operation[0] == 'Q':
        title = operation[1]
        print(int(playlist.get_plays(title)))