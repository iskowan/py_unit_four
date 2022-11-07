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
    return card1 + card2
def get_another_card(current):
    draw = input("Would you like another card?")
    if draw == "yes":
        card = draw_card()
        print("You drew a", card)
        print("Your total is", current + card)
        return current + card
    elif draw == "no":
        print("The dealers total is", dealer_total)
def main():
    ''' making the value of the cards 0 because you start out with no cards'''
    current = user_card_hand()
    ''' drawing two cards and adding them to the current total'''
    current2 = get_another_card(current)
    if current2 == "yes":
        user = get_another_card(current2)
    else:
        print("The dealers total is", dealer_total)
    ''' asking the user if they want to draw another card, if they do, this automatically repeats '''

main()