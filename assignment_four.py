# Anderson Iskowitz
#Unit 4 Option 1
import random
def get_card():
    return random.randint(1, 10)
''' getting a random value between 1 and 10 '''
def user_card_hand():
    card = get_card()
    print("You got a", card)
    card2 = get_card()
    print("You got a", card2)
    hand_total = card + card2
    print("Your total is", hand_total)
    return hand_total
def draw_card():
    card = get_card()
    return card
def dealer_total():
    card1 = get_card()
    card2 = get_card()
    card_total = card1 + card2
    return card_total
def get_another_card(current):
    draw = input("Would you like another card?")
    if draw == "yes":
        card = draw_card()
        print("You drew a", card)
        total = current + card
        print("Your total is", total)
        return get_another_card(total)
    elif draw == "no":
        print("The dealers total is", dealer_total)

def get_winner(user, dealer):
    if user < 21 and dealer < 21:
        print("You both lose")
    elif user == dealer:
        print("You tied")
    elif user > 21:
        print("You lose")
    elif user < 21 and user > dealer:
        print("You Win")
    elif user < 21 and user < dealer:
        print("You lose")

def main():
    ''' making the value of the cards 0 because you start out with no cards'''
    current = user_card_hand()
    ''' drawing two cards and adding them to the current total'''
    user_total = get_another_card(current)
    get_winner(user_total, dealer_total)

main()