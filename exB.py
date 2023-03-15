#!/bin/python

class Player():
    def __init__(self, name: str) -> None:
        self.nickname = name
        self.scores = []

    def setScore(self, song: int, score: int) -> None:
        if score > self.scores[song]:
            self.scores[song] = score

    def getTotal(self) -> int:
        total = 0
        for score in self.scores:
            if score != 0:
                total += score

        return total

    def getAverage(self) -> int:
        total = length = 0
        for score in self.scores:
            if score != 0:
                length += 1
                total += score

        return int(total / length)

    def getBestScore(self) -> int:
        best = 0
        for i in range(len(self.scores)):
            if self.scores[i] > self.scores[best]:
                best = i

        return best

    def getWorstScore(self) -> int:
        worst = 0
        for i in range(len(self.scores)):
            if self.scores[i] < self.scores[worst]:
                worst = i

        return worst

    def getScore(self, song: int) -> int:
        return self.scores[song]


class Karaoke():
    def __init__(self, player: Player) -> None:
        self.players = [player]
        self.songs = 0
        self.songList = []

    def addSong(self, title: str) -> None:
        self.songList.append(title)
        self.songs += 1

    def removeSong(self, title: str) -> None:
        for song in self.songList:
            if song == title:
                self.songList.remove(song)

    def getSongIndex(self, title: str) -> int:
        for i in range(len(self.songList)):
            if self.songList[i] == title:
                return i
        return -1

    def addPlayer(self, player: Player) -> None:
        self.players.append(player)

    def removePlayer(self, player: Player) -> None:
        if self.players.index(player) > 0:
            self.players.remove(player)

    def getSongBestScore(self, title: str) -> int:
        best = 0
        i = self.getSongIndex(title)
        for player in self.players:
            if player.getScore(i) > best:
                best = player.getScore(i)
        return best

    def getBestPlayerAverage(self) -> int:
        best = 0
        for player in self.players:
            if player.getAverage() > best:
                best = player.getAverage()

        return best

def main():
    p1 = Player("Miguel")
    p2 = Player("Pablo")

    p1.setScore(0, 59)
    p1.setScore(4, 80)

    p2.setScore(3, 89)

    print(p1.getTotal(), p1.getAverage(), p1.getBestScore(), p1.getWorstScore())

    print(max(p1.getBestScore(), p2.getBestScore()))


if __name__ == "__main__":
    main()
