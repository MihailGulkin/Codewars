class Warrior:
    RANKS = [
        "Pushover",
        "Novice",
        "Fighter",
        "Warrior",
        "Veteran",
        "Sage",
        "Elite",
        "Conqueror",
        "Champion",
        "Master",
        "Greatest"
    ]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = self.rank_up()
        self.achievements = []

    def rank_up(self):
        return self.RANKS[round(self.level // 10)]

    def exp_zeroing(self):
        if self.experience >= 10000:
            self.level = 100
            self.experience = 10000
            self.rank = self.rank_up()
        else:
            self.level = round(self.experience // 100)
            self.rank = self.rank_up()

    def training(self, _list):
        name = _list[0]
        exp = _list[1]
        level = _list[2]
        if self.level >= level:
            self.experience += exp
            self.achievements.append(name)
            self.exp_zeroing()
            return name
        else:
            return 'Not strong enough'

    def battle(self, level):
        if 1 <= level <= 100:
            rank = self.RANKS[round(level // 10)]
            if self.level == level:
                self.experience += 10
                self.exp_zeroing()
                return 'A good fight'
            elif (self.level - level == 1):
                self.experience += 5
                self.exp_zeroing()
                return 'A good fight'
            elif (self.RANKS.index(self.rank) < self.RANKS.index(rank) and abs(
                    self.level - level) >= 5):
                return "You've been defeated"
            elif (self.level < level):
                self.experience += 20 * (abs(level - self.level) ** 2)
                self.exp_zeroing()
                return 'An intense fight'
            else:
                return 'Easy fight'
        else:
            return 'Invalid level'
