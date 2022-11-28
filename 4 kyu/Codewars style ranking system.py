class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, num):
        assert (-8 <= num <= 8 and num != 0)

        if self.rank < 8:
            ranks = [i for i in range(-8, 9) if i != 0]
            numPosition = ranks.index(num)
            rankPosition = ranks.index(self.rank)

            if (numPosition > rankPosition):
                self.progress += 10 * (numPosition - rankPosition) ** 2

            elif (numPosition < rankPosition):
                if (numPosition == rankPosition - 1):
                    self.progress += 1
            else:
                self.progress += 3

            while (self.progress >= 100):
                self.progress -= 100
                if (self.rank == -1):
                    self.rank += 2
                else:
                    self.rank += 1

                if (self.rank == 8):
                    self.progress = 0
                    break
