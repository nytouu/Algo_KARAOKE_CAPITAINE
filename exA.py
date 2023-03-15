#!/bin/python

class Player():
    def __init__(self, name: str) -> None:
        self.nickname = name
        self.scores = [0, 0, 0, 0, 0]

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
