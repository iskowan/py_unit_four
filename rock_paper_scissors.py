import random
def who_wins(user, computer):
    if user == computer:
        print("The computer played the same as you, you tied")
    elif user == 1 and computer == 2:
        print("The computer played paper, you lose")
    elif user == 1 and comupter == 3:
        print("The computer played scissors, you lose")
    elif user == 2 and computer == 3:
        print ("The computer played scissors, you lose")
    elif user == 2 and computer == 1:
        print("The computer played rock, you win")
    elif user == 3 and computer == 1:
        print("The computer played rock, you Win")
    elif user == 3 and computer == 2:
        print("The computer played paper, you Win")

# 1 is rock, 2 is paper, 3 is scissors


def main():
    print("This is Rock, Paper, Scissors, Rock = 1 Paper = 2 Scissors =3")
    user = int(input("Rock, Paper, or Scissors?:"))
    computer = random.randint (1, 3)
    who_wins(user, computer)

main()

'''if __name__ == '__main__':
    main()
'''