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
    return user_card_total

def dealer_total():
    dealer_card1 = get_card()
    dealer_card2 = get_card()
    dealer_card_total = dealer_card1 + dealer_card2
    print("Dealer total", dealer_card_total)

def get_new_card():
    new_card = input("Would you like to draw another card?:")
    if new_card == str("Yes") or str("yes"):
        new_draw_card = get_card()
        new_user_total = user_card_total + new_draw_card
        '''                 ^^How do I get this to work here'''
        print("Your new total is", new_user_total)
        print(new_draw_card)
    elif new_card == str("No") or str("no"):
        print("Ok, your total is:")
    else:
        print("There was an error")

def main():
    user_total()
    get_new_card()
    dealer_total()

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