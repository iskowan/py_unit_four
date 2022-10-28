import random
def max(num1, num2):
    if num1 > num2:
        #return num1
        return(str(num1) + " is greater than" + str(num2))
    else:
        return(str(num2), " is greater than", str(num1))
    '''
    if num1 < num2
        return num2
    '''

def main():
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    print(max(num1, num2))
    #return functions allow there to be less print functions

main()
