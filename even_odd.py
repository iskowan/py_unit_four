number = int(input("Give me a random number:"))
def even_or_odd(number):
    if number % 2 ==0:
        print(number, "is an even number")
    else:
        print(number, "is not an even number")
    """
    Create a function that will tell if a number is even or odd. Use two if statements to do this.
    :param number: could be any positive or negative integer
    :return: either "x is an even number" or "x is an odd number"
    """
    pass

def main():
    even_or_odd(number)
    # First, make sure to delete the word "pass" then get input from the user.
    # They should type in a number, make sure to convert it to an int
    # Next, call the even_or_odd function, and make sure to pass the user's number as a parameter.
    pass


if __name__ == '__main__':
    main()