# Anderson Iskowitz
#Unit 4 Option 1
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

def draw_card(current):
    card = get_card()
    return card + current

def dealer_total():
    card1 = get_card()
    card2 = get_card()
    return card1 + card2

def get_another_card():
    current = 0
    draw = input("Would you like another card?")
    if draw == "yes":
        card = draw_card(current)
        print("You drew a", card)
        #print("Your total is", user_card_hand + card)
        get_another_card()
    elif draw == "no":
        print("The dealers total is...", dealer_total)

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
    user_card_hand(current)
    get_another_card()
    #get_winner()

main()