# Anderson Iskowitz
#Unit 4 Option 1
import random
'''
def ace():
    print(" --------")
    print("| A      |")
    print("|        |")
    print("|        |")
    print("|      A |")
    print(" --------")
def card2():
    print(" --------")
    print("| 2      |")
    print("|        |")
    print("|        |")
    print("|      2 |")
    print(" --------")
def card3():
    print(" --------")
    print("| 3      |")
    print("|        |")
    print("|        |")
    print("|      3 |")
    print(" --------")
def card4():
    print(" --------")
    print("| 4      |")
    print("|        |")
    print("|        |")
    print("|      4 |")
    print(" --------")
def card5():
    print(" --------")
    print("| 5      |")
    print("|        |")
    print("|        |")
    print("|      5 |")
    print(" --------")
def card6():
    print(" --------")
    print("| 6      |")
    print("|        |")
    print("|        |")
    print("|      6 |")
    print(" --------")
def card7():
    print(" --------")
    print("| 7      |")
    print("|        |")
    print("|        |")
    print("|      7 |")
    print(" --------")
def card8():
    print(" --------")
    print("| 8      |")
    print("|        |")
    print("|        |")
    print("|      8 |")
    print(" --------")
def card9():
    print(" --------")
    print("| 9      |")
    print("|        |")
    print("|        |")
    print("|      9 |")
    print(" --------")
def card10():
    print(" --------")
    print("| 10     |")
    print("|        |")
    print("|        |")
    print("|     10 |")
    print(" --------")
    '''
def get_card():
    return random.randint(1, 10)
''' getting a random value between 1 and 10 '''
'''
if get_card() == 1:
    ace()
if get_card() == 2:
    card2()
if get_card() == 3:
    card3()
if get_card() == 4:
    card4()
if get_card() == 5:
    card5()
if get_card() == 6:
    card6()
if get_card() == 7:
    card7()
if get_card() == 8:
    card8()
if get_card() == 9:
    card9()
if get_card() == 10:
    card10()
'''

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
        get_another_card(total)
        return get_another_card(total)
    elif draw == "no":
        print("The dealers total is", dealer_total)
def main():
    ''' making the value of the cards 0 because you start out with no cards'''
    current = user_card_hand()
    ''' drawing two cards and adding them to the current total'''
    get_another_card(current)
    print("Your total is", get_another_card)

main()