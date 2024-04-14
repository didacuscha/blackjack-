import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            self.__init__()  # Reinitialize the deck if out of cards
            return self.cards.pop()

def card_value(card):
    if card.value in ['Jack', 'Queen', 'King']:
        return 10
    elif card.value == 'Ace':
        return 11
    else:
        return int(card.value)

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card.value == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def check_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21

class House:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.deck = Deck()
        self.hand = []

    def __repr__(self):
        return f"{self.name}, P2P Blackjack House."

    def shuffle(self):
        self.deck.shuffle()

    def draw_card(self):
        card = self.deck.draw_card()
        self.hand.append(card)
        return card

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

class Gambler:
    def __init__(self, name, money, house):
        self.name = name
        self.money = money
        self.deck = Deck()
        self.hand = []
        self.house = house
        self.bet = 0

    def __repr__(self):
        return f"{self.name} has an account balance of {self.money}"

    def place_bet(self, amount):
        if amount > self.money:
            print("Insufficient funds.")
        else:
            self.bet = amount
            self.money -= amount

    def draw_card(self):
        card = self.deck.draw_card()
        self.hand.append(card)
        return card

    def pass_turn(self):
        # Evaluate hands and apply payout or loss
        player_value = hand_value(self.hand)
        house_value = hand_value(self.house.hand)
        if check_blackjack(self.hand) and not check_blackjack(self.house.hand):
            self.money += 2.5 * self.bet
        elif player_value > house_value and player_value <= 21 or house_value > 21:
            self.money += 2 * self.bet
        elif player_value == house_value:
            self.money += self.bet  # return the bet if it's a draw
        self.bet = 0
        self.hand = []
        self.house.hand = []

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

# Initialization of the House and Gambler
def main():
    house = House("Octopus", 1000000)
    player = Gambler("Diego", 1000, house)
    
    while True:
        house.shuffle()  # Ensure the deck is shuffled before starting
        player.place_bet(int(input("Place your bet: ")))  # Player places a bet
        
        # Initial draw
        player.draw_card()
        player.draw_card()
        house.draw_card()
        house.draw_card()
        

        print(f"Your hand: {player.show_hand()} (Value: {hand_value(player.hand)})")
        print(f"House's hand: {house.hand[0]}, [Hidden Card]")

        # Check for Blackjack
        if check_blackjack(player.hand) and not check_blackjack(house.hand):
            print(f"Blackjack! You win ${2.5 * player.bet}!")
            player.money += 2.5 * player.bet
        elif check_blackjack(house.hand):
            print("House has Blackjack!")
        else:
            # Player's turn
            while hand_value(player.hand) < 21:
                action = input("Do you want to (h)it or (s)tand? ")
                if action.lower() == 'h':
                    player.draw_card()
                    print(f"Your hand: {player.show_hand()} (Value: {hand_value(player.hand)})")
                    if hand_value(player.hand) > 21:
                        print("Bust! You lose.")
                        break
                elif action.lower() == 's':
                    print("You chose to stand.")
                    break

            # House's turn if player hasn't busted
            if hand_value(player.hand) <= 21:
                while hand_value(house.hand) < 17:
                    house.draw_card()
                    print(f"House draws: {house.hand[-1]} (New Total: {hand_value(house.hand)})") # Show each card house draws
                    if hand_value(house.hand) >= 17:  # Check after drawing to stop if 17 or more
                        break
                print(f"House's final hand: {house.show_hand()} (Value: {hand_value(house.hand)})")

                # Compare hands
                if hand_value(house.hand) > 21:
                    print(f"You win ${2 * player.bet}!")  # House busts
                    player.money += 2 * player.bet
                elif hand_value(player.hand) > hand_value(house.hand):
                    print(f"You win ${2 * player.bet}!")
                    player.money += 2 * player.bet
                elif hand_value(player.hand) == hand_value(house.hand):
                    print("It's a draw!")
                    player.money += player.bet  # Return the bet if it's a draw
                else:
                    print("House wins.")

        # Reset for next round
        player.hand = []
        house.hand = []
        player.bet = 0

        # Check if player wants to continue
        if input("Play another round? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
