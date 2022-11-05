# Anderson Iskowitz
#Unit 4 Option 1
#Ace = 1
import random
def get_card():
    return random.randint(1,10)

def user_card_hand(current):
    card = get_card()
    print("You got a", card)
    card2 = get_card()
    print("You got a", card2)
    hand_total = card + card2
    print("Your total is", hand_total)
    return hand_total + current
def user_total(current):
    card = get_card()
    print("You drew a", card)
    return current + card

def dealer_total():
    dealer_card1 = get_card()
    dealer_card2 = get_card()
    dealer_card_total = dealer_card1 + dealer_card2
    print("Dealer total", dealer_card_total)

def get_another_card():
    input("Would you like another card?")

def get_winner():
    if user_total < 21 and dealer_total < 21:
        print("You both went over 21")
    elif user_total == dealer_total:
        print("You tied")
    elif user_total > 21:
        print("You lose")
    elif user_total < 21 and dealer_total < user_total:
        print("You win")

def main():
    current = 0
    current = user_card_hand(current)
    get_another_card()
    while (get_another_card == "yes" or "Yes" or "Y" or "y"):
        ''' this allows the function to repeat by continuing the function if it is true/"yes" '''
        print("Your total is", user_total(current))
        get_another_card()
        if (get_another_card == "no" or "No" or "N" or "n"):
            print("Your total is", current, "lets see what the dealer's total is...")
    get_winner()
main()