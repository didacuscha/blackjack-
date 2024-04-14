class House:
    def __init__(self, name, money, game):
        self.name = name
        self.money = money
        self.game = game
    
    def __repr__(self):
        return str(self.name) + ", P2P Blackjack House. "
    
    def play_game(self, game):
        pass

    def draw_card(self, game):
        pass

    def pass_turn(self):
        pass

    def payout(self):
        pass

    def shuffle(self):
        pass

class Gambler:
    def __init__(self, name, money, house, bets, record):
        self.name = name
        self.money = money
        self.house = house
        self.bets = bets
        self.record = record
  
    def __repr__(self):
        return str(self.name) + " has an account balance of " + str(self.money)
    
    def play_round(self):
        pass

    def draw_card(self):
        pass

    def pass_turn(self):
        pass
    
octopus = House("octopus", 1000000, {})
diego = Gambler("diego", 1000, octopus, [], [])

print(octopus)
print(diego)
    

