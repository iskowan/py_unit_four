# Anderson Iskowitz
#Unit 4 Option 1
#Ace = 1
import random
def get_card():
    return random.randint(1,10)
def user_total():
    user_card1 = get_card()
    user_card2 = get_card()
    user_card_total = user_card1 + user_card2
    print("Your cards are", user_card1, "and", user_card2, "with a total of", user_card_total)

def dealer_total():
    dealer_card1 = get_card()
    dealer_card2 = get_card()

def new_card():
    get_new_card = input("Would you like to draw another card?:")
    if get_new_card == "yes" or "Yes":
        print(get_card())
    elif get_new_card == "no" or "No":
        print("Ok, your total is" '', 'user_card_total''')
    else:
        print("Sorry there was an Error")
        new_card()

def main():
    user_total()
    dealer_total()
    new_card()

main()



'''
def user_total():
    return int(get_card() + get_card())
def dealer_total():
    get_card()
    get_card()
def get_winner():
    if user_total > 21 and dealer_total > 21:
        print("You both went over 21 and lose")
def main():
    print("Welcome to Black Jack.")
    print("How to play:")
    print("1. ")
    print(user_total)
    draw = input("Would you like to draw")
    if draw == "yes" or "Yes":
        card = get_card
        print("You drew a", card)


main()
'''