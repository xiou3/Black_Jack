from random import seed
from random import randrange
from datetime import datetime

# globals
kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}

# functions
def hand_value(hand):
    s = 0
    ace = False
    for card in hand:
        n = card[1]
        if n == "jack" or n == "queen" or n == "king":
            s += 10
        elif n == "ace":
            ace = True
            s += 1
        else:
            s += n

    if ace:
        if s + 10 <= 21:
            s += 10

    return s

def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    
    while True:
        print(hand, hand_value(hand))
        
        choice = input("H-Hit or S-Stand: ").upper()
        if choice == "H":
            hand.add(deck.pop())
            value = hand_value(hand)
            if value >= 21:
                return hand_value(hand)
        elif choice == "S":
            return hand_value(hand)

def computer(value_player, hand):    
    hand.add(deck.pop())
    hand.add(deck.pop())
    
    while True:
        value = hand_value(hand)
        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())

        
# main
def main():
    seed(datetime.now())
    
    rounds = 1
    score = [0, 0]
    
    while True:
        print("*" * 15)
        print("Round: ", rounds)
        # print(len(deck))
        print("*" * 15)

        player_hand = set()
        player_value = player(player_hand)
        computer_hand = set()
        
        print(f"Your hand {player_hand} has {player_value} value")
        if player_value == 21:
            print("You WON!")
            result = "player"
        elif player_value > 21:
            print("You lost!")
            result = "computer"
        else:  
            print("Computer plays")
            computer_value = computer(player_value, computer_hand)
            
            print(f"Computer's hand {computer_hand} has {computer_value} value")
            if computer_value > 21:
                print("You Won!")
                result = "player"
            else:
                print("You lost!. Computer WON!")
                result = "computer"

        if result == "player":
            score[0] += 1
        else:
            score[1] += 1

        print("Player's Score: ", score[0], "Computer's Score: ", score[1])
        keep_playing = input("Do you want o play again (Y/N)? ").upper()

        if keep_playing == "N":
            if score[1] >= score[0]:
                print("Better luck next time")
            else:
                print("You are very good!")
                print("Bye bye!!")
            break
        else:
            for _ in range(len(player_hand)):
                deck.add(player_hand.pop())

            if len(computer_hand) != 0:
                for _ in range(len(computer_hand)):
                    deck.add(computer_hand.pop())
            rounds += 1
    

main()
