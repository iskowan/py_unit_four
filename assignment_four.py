# Anderson Iskowitz
#Unit 4 Option 1
import random
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
def get_card():
    card = random.randint(1, 10)
    if card == 1:
        ace()
        return 1
    if card == 2:
        card2()
        return 2
    if card == 3:
        card3()
        return 3
    if card == 4:
        card4()
        return 4
    if card == 5:
        card5()
        return 5
    if card == 6:
        card6()
        return 6
    if card == 7:
        card7()
        return 7
    if card == 8:
        card8()
        return 8
    if card == 9:
        card9()
        return 9
    if card == 10:
        card10()
        return 10
''' getting a random value between 1 and 10 '''
def user_card_hand():
    '''Setting up the user's hand'''
    card = get_card()
    card2 = get_card()
    print("You drew a", card)
    print("You drew a", card2)
    hand_total = card + card2
    print("Your total is", hand_total)
    return hand_total
def draw_card():
    '''function to draw a card'''
    card = get_card()
    return card
def dealer_total():
    '''setting up the dealer's hand'''
    card1 = get_card()
    print("The dealer drew a", card1)
    card2 = get_card()
    print("The dealer drew a", card2)
    card_total = card1 + card2
    if card_total <= 15:
        card3 = get_card()
        print("The dealer drew a", card3)
        new_card_total = card_total + card3
        if new_card_total <= 15:
            card4 = get_card()
            print("The dealer drew a", card4)
            total = new_card_total + card4
            return total
    return card_total
def get_another_card(current):
    '''gets more cards if needed/wanted'''
    draw = input("Would you like another card?")
    if draw == "yes":
        card = draw_card()
        print("You drew a", card)
        total = current + card
        print("Your total is", total)
        return total
    elif draw == "no":
        return current
def get_winner(user, dealer):
    '''compares the user total to the dealer total to calcualte the winner'''
    if user > 21 and dealer > 21:
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
    '''calling user_card_hand and naming it "current" '''
    current = user_card_hand()
    '''asking user if they want another card'''
    user_total1 = get_another_card(current)
    '''naming dealer_total()'''
    dealers_total = dealer_total()
    '''printing the dealer and user total'''
    print("Dealer's Total is", dealers_total)
    print("Your total is", user_total1)
    '''calling get winner to print the winner'''
    get_winner(user_total1, dealers_total)

'''calling main function'''
main()