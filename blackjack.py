class House:
    def __init__(self, name, money, game):
        self.name = name
        self.money = money
        self.game = game

class Gambler:
    def __init__(self, name, money, broke, house, bets, record):
        self.name = name
        self.money = money
        self.broke = broke
        self.house = house
        self.bets = bets
        self.record = record
  
    def __repr__(self):
        return str(self.name) + " has an account balance of " + str(self.money)
