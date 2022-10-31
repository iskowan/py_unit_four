'''
def main():
    if 6>2:
        print("Yep, 6 is greater than 2")
    print("Thanks for watching")

main()
'''
#using elif
'''
def whatGrade(grade):
    if grade == 9:
        print ("You are a freshman")
    elif grade == 10:
        print ("You are a sophmore")
    elif grade == 11:
        print ("You are a junior")
    elif grade == 12:
        print("You are a senior")
    else:
        print("You are not in high school")

def main():
    grade = input("What grade are you in?:")
    whatGrade(int(grade))

main()
'''
#Using or
'''
replay = input("Would you like to play again?")
if replay == "y" or "Y" or "Yes" or "yes":
    print("Great! Let's play a game")
else:
    print("Sorry to see you go")
'''
#using and
'''
if action == "unlock door" and hasKey == True:
    #both statements must be true to execute this
    print("You have opened the door")
else:
    print("You cannot open the door at this time")
'''