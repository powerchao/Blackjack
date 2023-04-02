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

def blackjack():
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
        print("Let's play a hand.")
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
        print("Your hand was " + hand_string(player_hand) + "totalling " + str(total_hand(player_hand)))
        print("Dealer\'s hand was " + hand_string(dealer_hand) + "totalling " + str(total_hand(dealer_hand)))
        if player_blackjack:
            if dealer_blackjack:
                print("Draw.")
            else:
                print("You win!")
        elif player_bust:
            if not dealer_bust:
                print("You lose.")
            else:
                print("Draw.")
        else:
            if dealer_blackjack:
                print("You lose.")
            elif dealer_bust:
                print("You win!")
            else:
                if total_hand(player_hand) < total_hand(dealer_hand):
                    print("You lose.")
                else:
                    print("You win!")
        again = input("Play again? y or n\n")
        if again != "y":
            continuing = False


blackjack()
            

            
            


