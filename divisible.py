def is_divisible(num1, num2):
    if is_divisible(num1, num2):
        num1 % num2 == 0
        print(num1, "is divisible by ", num2)
    else:
        print(num1, "is not divisible by ", num2)

    """
    Checks to see if one number is evenly divisible by the second
    :param num1: The number being tested
    :param num2: The divisor
    :return: True if num1 is evenly divisible by num2, false otherwise
    """

    pass


def main():

    # Get the two pieces of input from the user.
    num = int(input("What is the first number? "))
    check = int(input("What is the second number? "))

    if is_divisible(num, check):
        print(num, "is divisible by", check)
    else:
        print(num, "is not divisible by", check)


if __name__ == '__main__':
    main()
