import random
import os

deck = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

def blackjack(player_bet):
    """Initializies the Blackjack game"""

    def draw_card(hand,cards):
        hand.append(random.choice(list(deck)))
        if cards > 1:
            draw_card(hand,cards-1)
    
    def total_hand(hand):
        hand_sum = 0
        high_aces = 0
        for card in hand:
            if card == "Ace":
                high_aces += 1
            hand_sum += deck[card]
        while hand_sum > 21 and high_aces > 0:
            hand_sum -= 10
            high_aces -= 1
        return hand_sum

    def hand_string(hand):
        output_string = "["
        for number in range(len(hand)):
            output_string += hand[number]
            if number < len(hand)-1:
                output_string += ", "
        output_string += "]"
        return output_string
    
    os.system("cls")
    print(f"Let's play a hand.\nYour bet is ${player_bet}")
    dealer_hand = []
    player_hand = []
    draw_card(dealer_hand,2)
    draw_card(player_hand,2)
    player_bust = False
    player_blackjack = False
    player_staying = False
    while not player_bust and not player_blackjack and not player_staying:
        print("Your hand is: " + hand_string(player_hand) + ", totalling " + str(total_hand(player_hand)))
        if total_hand(player_hand) == 21:
            player_blackjack = True
        elif total_hand(player_hand) > 21:
            player_bust = True
        else:
            print("The dealer is showing a " + dealer_hand[1] + ".")
            player_action = input("Would you like to hit or stay?\n").lower()
            if player_action == "hit":
                draw_card(player_hand,1)
                card_drawn = player_hand[len(player_hand)-1]
                print("You are dealt a " + card_drawn + ".")
            else:
                player_staying = True
    dealer_bust = False
    dealer_blackjack = False
    dealer_staying = False
    while not dealer_bust and not dealer_blackjack and not dealer_staying:
        print("Dealer\'s hand is: " + hand_string(dealer_hand))
        if total_hand(dealer_hand) == 21:
            dealer_blackjack = True
        elif total_hand(dealer_hand) > 21:
            dealer_bust = True
        else:
            if total_hand(dealer_hand) < 17:
                draw_card(dealer_hand,1)
                card_drawn = dealer_hand[len(dealer_hand)-1]
                print(f"Dealer draws a " + card_drawn + "\n")
            else:
                dealer_staying = True
    print("\n\n\n")
    print("Your hand was " + hand_string(player_hand) + " totalling " + str(total_hand(player_hand)))
    print("Dealer\'s hand was " + hand_string(dealer_hand) + " totalling " + str(total_hand(dealer_hand)))
    if player_blackjack:
        if dealer_blackjack:
            print("Draw.")
            return 0
        else:
            print("You win!")
            return player_bet
    elif player_bust:
        if not dealer_bust:
            print("You lose.")
            return 0 - player_bet
        else:
            print("Draw.")
            return 0
    else:
        if dealer_blackjack:
            print("You lose.")
            return 0 - player_bet
        elif dealer_bust:
            print("You win!")
            return player_bet
        else:
            if total_hand(player_hand) < total_hand(dealer_hand):
                print("You lose.")
                return 0 - player_bet
            elif total_hand(player_hand) == total_hand(dealer_hand):
                print("Draw.")
                return 0
            else:
                print("You win!")
                return player_bet


def begin_playing(player_wallet):
    total_money = player_wallet
    os.system("cls")
    print("Welcome to the Blackjack table.")
    continuing = True
    while continuing:
        if total_money < 5:
            print("You do not have sufficient chips to play a hand.")
            continuing = False
        else:
            print(f"Your total funds: ${total_money}")
            current_wager = int(input("What would you like to bet on this hand? Minimum bet is $5\n$"))
            while current_wager < 5:
                current_wager= int(input("What would you like to bet on this hand? Minimum bet is $5\n$"))
            total_money += blackjack(current_wager)
            play_again = input("Would you like to play another hand? y or n\n")
            if play_again != "y":
                continuing = False
    print(f"\nYou walk away with ${total_money}")

begin_playing(500)            
            


