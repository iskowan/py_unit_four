import random

def number_distance(player_guess):
    return((abs(int(num1), int(player_guess))))
def guess_number():
    num1 = random.randint(1, 10)
    player_guess = int(input("I'm thinking of a number between 1 and 10, what number do you think I'm thinking of?:"))
    if player_guess == num1:
        print("You guessed the number! It was ", num1)
    else:
        print("sorry, my number was", num1, "you were", number_distance, "away")

def main():
    guess_number()

main()