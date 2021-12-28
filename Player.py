class Player:
    def __init__(self):
        self.hand = []
        self.name = ""
        self.win_count = 0

    def __str__(self):
        return "NAME: " + self.name + " | HAND: " + self.hand.__str__() + " | win count: " + str(self.win_count)

    def __repr__(self):
        return "NAME: " + self.name + " | HAND: " + self.hand.__str__() + " | win count: " + str(self.win_count)

    def __gt__(self, other):
        self_d = self.hand[3]
        other_d = other.hand[3]
        if self_d > other_d: return True
        else: return False
        
    def __lt__(self, other):
        self_d = self.hand[3]
        other_d = other.hand[3]
        if self_d < other_d: return True
        else: return False

    def removeDom(self, expr):
        for x in range(len(self.hand)):
            if self.hand[x] == expr:
                self.hand.pop(x)
                return True
        return False

    def doesHandHave(self, expr):
        for x in self.hand:
            if x == expr:
                return True
        return False

    def isEmpty(self):
        if len(self.hand) == 0: return True
        return False

    def addDom(self, expr):
        self.hand.append(expr)
    
    def winRound(self):
        self.win_count += 1