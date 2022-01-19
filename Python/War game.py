import random, time

# Define basic variables for further usage. It will allow to create Card class.
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ['Two', 'Three', 'Four', "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {'Two':2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven": 7, "Eight":8,
          "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}


# Define 3 classes. Card, Deck and Player
# Card class with 3 atributes and 1 print method. This allows to create card objects.
# Deck class iterates through predefined variables and creates a deck of cards. It has 2 methods. Shuffle and deal_one.
# Player class has 4 methods. remove_one, add_cards, show_value and print.
class Card():
  
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player():
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,cards):
        
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
            
    def show_value(self):
        total = 0
        for card in self.all_cards:
            total += card.value
        return total
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# Define 2 functions for displaying information during the game.
# Both cards_printer() and war_printer() are almost the same. They both take 2 arguments and display information about used cards.
def cards_printer(card_1, card_2):
    print(f"Player 1 with {card_1} vs Player 2 with {card_2}")
    
def war_printer(card_1, card_2):
    print('\nCards on top:')
    print(f'Player 1 with {card_1} vs Player 2 with {card_2}\n')


# main() function to run game logic
def main():

    print('\n*******  WAR GAME! ********')
    time.sleep(2)
    print('\n' * 10)
    print('Do you prefer to play longer game(52 cards) or shorter one (26 cards)? Please specify L or S\n')

    # Define main variables for further usage.
    # Both game_on and check are boolean type values used for while loop logic. Variables round_num and ran are used to keep track of numbers.
    game_on = True
    check = False
    round_num = 0
    ran = 0

    # First while loop to choose shorter or longer game variant.
    while ran == 0:
        
        choice = input()
        if choice.upper() == 'L':
            ran = 26
        elif choice.upper() == 'S':
            ran = 13
        else:
            print("Sorry, I don`t understand. Please type L or S")

    # Create variables for a deck and both players. Then deal cards for each player.
    new_deck = Deck()
    new_deck.shuffle()

    player_one = Player("Player 1")
    player_two = Player("Player 2")

    for x in range(ran):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    time.sleep(2)

    # Second while loop to specify how many cards each player needs to stake in war. The limit is 50% of all cards.
    print(f"Please speficy how many cards each player will need to participate in war\nThe limit is {round(ran/2)}")
    while check == False:
        
        choice = input()
        
        if choice.isdigit() == False:
            print("Enter an integer\n")
        elif int(choice) == 0 or int(choice) > round(ran/2):
            print("Out of the range")
        else:
            check = True

    time.sleep(2)
    
    # Main loop for game logic.
    # While non of the players have 0 cards, in each round a cards is taken from their hand. The one with higher value will take both cards.
    # If cards have the same value, it will initialize the war.
    # Each player stacks required amount of cards. If they don`t have enought cards, they lose. Player with higher value wins both stacks.
    while game_on:
        
        round_num += 1
        print(f"Round {round_num}")
        
        # Check if players have any cards left. If not, they lose
        if len(player_one.all_cards) == 0:
            print("Player 1 out of cards, Player 2 wins!")
            game_on = False
        elif len(player_two.all_cards) == 0:
            print("Player 2 out of cards, Player 1 wins!")
            game_on = False 
        else:
            # Create variables for currently used cards and remove top cards from player's hands.
            # Use cards_printer to display which cards are being used.
            player_one_cards = []
            player_two_cards = []
            
            removed_card_one = player_one.remove_one()
            removed_card_two = player_two.remove_one()
            
            cards_printer(removed_card_one, removed_card_two)
            
            player_one_cards.append(removed_card_one)
            player_two_cards.append(removed_card_two)
            
            war = True
            
            while war:
                # Check each scenario. The winner takes both cards. As in the war game, player_two_cards goes at the end of the list.
                if player_one_cards[-1].value > player_two_cards[-1].value:
                    player_one.add_cards(player_one_cards)
                    player_one.add_cards(player_two_cards)
                    war = False
                elif player_one_cards[-1].value < player_two_cards[-1].value:
                    player_two.add_cards(player_two_cards)
                    player_two.add_cards(player_one_cards)
                    war = False
                else:
                    # First it checks if players have enough cards to participate in war. If not, they lose and game ends.
                    print("\nWAR!")
                    
                    if len(player_one.all_cards) < int(choice):
                        print("Player 1 unable to participate in war. Player 2 wins at war!")
                        game_on = False
                        break
                    elif len(player_two.all_cards) < int(choice):
                        print("Player 2 unable to aprticipate in war. player 1 wins at war!")
                        game_on = False
                        break
                    else:
                        # Takes "choice" number of cards from each player and compares the last stacked.
                        for num in range(int(choice)):
                            player_one_cards.append(player_one.remove_one())
                            player_two_cards.append(player_two.remove_one())

                        war_printer(player_one_cards[-1], player_two_cards[-1])
    
    time.sleep(2)
    print('\n' * 10)
    print("******** Thanks for playing ********")
    print('\n' * 3)  


if __name__ == '__main__':
    main()