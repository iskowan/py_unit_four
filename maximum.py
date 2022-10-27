def max(num1, num2):
    if num1 > num2:
        print(num1, "is greater than", num2)
        #return num1
    else:
        print(num2, "is greater than", num1)
        #return num2

def main():
    getNum1 = input("Give one random number:")
    getNum2 = input("Give another random number:")
    max(getNum1, getNum2)

main()
