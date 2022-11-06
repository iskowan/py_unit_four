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
def draw_card():
    card = get_card()
    return card
def dealer_total():
    card1 = get_card()
    card2 = get_card()
    return card1 + card2
def get_another_card():
    current = user_card_hand
    draw = input("Would you like another card?")
    if draw == "yes":
        card = draw_card()
        print("You drew a", card)
        print("Your total is", current + card)
        '''
        if current <= 21:
            print("You lose")
        '''
        get_another_card()
    elif draw == "no":
        print("The dealers total is", dealer_total)
def get_winner(user_total, dealer_total):
    if user_total < 21 and dealer_total < 21:
        print("You both went over 21")
    elif user_total == dealer_total:
        print("You tied")
    elif user_total > 21:
        print("You lose")
    elif user_total < 21 and dealer_total < user_total:
        print("You win")
    elif user_total < 21 and dealer_total > user_total:
        print("You lose")
def main():
    current = 0
    ''' making the value of the cards 0 because you start out with no cards'''
    user_card_hand(current)
    ''' drawing two cards and adding them to the current total'''
    get_another_card()
    ''' asking the user if they want to draw another card, if they do, this automatically repeats '''
    #get_winner()
    #print(get_winner(user_total, dealer_total)
main()