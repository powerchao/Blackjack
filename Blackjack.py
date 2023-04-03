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
    hand_wager = player_bet
    print(f"Let's play a hand.\nYour bet is ${hand_wager}")
    dealer_hand = []
    player_hand = []
    draw_card(dealer_hand,2)
    draw_card(player_hand,2)
    player_doubled = False
    player_bust = False
    player_blackjack = False
    player_staying = False
    while not player_bust and not player_blackjack and not player_staying and not player_doubled:
        print("Your hand is: " + hand_string(player_hand) + ", totalling " + str(total_hand(player_hand)))
        if total_hand(player_hand) == 21:
            player_blackjack = True
        elif total_hand(player_hand) > 21:
            player_bust = True
        else:
            print("The dealer is showing a " + dealer_hand[1] + ".")
            player_action = input("Would you like to hit, double, or stand?\n").lower()
            if player_action == "hit":
                draw_card(player_hand,1)
                card_drawn = player_hand[len(player_hand)-1]
                print("You are dealt a " + card_drawn + ".")
            elif player_action == "double":
                hand_wager *= 2
                player_doubled = True
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
                print(f"\nDealer draws a " + card_drawn + "\n")
            else:
                dealer_staying = True
    print("\n\n")
    print("Your hand was " + hand_string(player_hand) + " totalling " + str(total_hand(player_hand)))
    print("Dealer\'s hand was " + hand_string(dealer_hand) + " totalling " + str(total_hand(dealer_hand)))
    if player_blackjack:
        if dealer_blackjack:
            print("Draw.")
            return 0
        else:
            print("You win!")
            return hand_wager
    elif player_bust:
        if not dealer_bust:
            print("You lose.")
            return 0 - hand_wager
        else:
            print("Draw.")
            return 0
    else:
        if dealer_blackjack:
            print("You lose.")
            return 0 - hand_wager
        elif dealer_bust:
            print("You win!")
            return hand_wager
        else:
            if total_hand(player_hand) < total_hand(dealer_hand):
                print("You lose.")
                return 0 - hand_wager
            elif total_hand(player_hand) == total_hand(dealer_hand):
                print("Draw.")
                return 0
            else:
                print("You win!")
                return hand_wager


def begin_playing(player_wallet):
    total_money = player_wallet
    continuing = True
    while continuing:
        os.system("cls")
        print("Welcome to the Blackjack table.")
        if total_money < 5:
            print("You do not have sufficient chips to play a hand.")
            continuing = False
        else:
            print(f"Your total funds: ${total_money}")
            current_wager = int(input("What would you like to bet on this hand? Minimum bet is $5\n$"))
            try:
                while current_wager < 5 or current_wager > total_money:
                    current_wager= int(input("That amount is inappropriate.\nWhat would you like to bet on this hand? Minimum bet is $5\n$"))
                total_money += blackjack(current_wager)
                play_again = input("Would you like to play another hand? y or n\n")
                if play_again != "y":
                    continuing = False
            except:
                print("Your bet amount must be entered as a single number with no commas or symbols.")
    print(f"\nYou walk away with ${total_money}")

begin_playing(500)