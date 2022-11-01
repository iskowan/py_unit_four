import random
def who_wins(user, computer):
    ''' 1 is rock, 2 is paper, 3 is scissors'''
    if user == computer:
        print("The computer played the same as you, you tied")
    elif user == "rock" or "Rock" and computer == 2:
        print("The computer played paper, you lose!")
    elif user == "paper" or "Paper" and comupter == 3:
        print("The computer played scissors, you lose!")
    elif user == "paper" or "Paper" and computer == 3:
        print ("The computer played scissors, you lose!")
    elif user == "paper" or "Paper" and computer == 1:
        print("The computer played rock, you win!")
    elif user == "Scissors" or "scissors" and computer == 1:
        print("The computer played rock, you win!")
    elif user == "Scissors" or "scissors" and computer == 2:
        print("The computer played paper, you win!")
    else:
        print("You didnt put in rock, paper, or scissors")



def main():
    print("This is Rock, Paper, Scissors")
    user = str(input("Rock, Paper, or Scissors?:"))
    computer = random.randint (1, 3)
    who_wins(user, computer)

main()

'''if __name__ == '__main__':
    main()
'''