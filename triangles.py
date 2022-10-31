def is_triangle(side1, side2, side3):
    if side1 > side2 + side3 or side2 > side3 + side1 or side3 > side1 + side2:
        print("These lengths would not make a triangle")
    elif side1 <= side2 + side3 or side2 <= side3 + side1 or side3 <= side1 +side2:
        print("These lengths would make a triangle")
    pass



def main():
    side_length1 = input("Enter the first length:")
    side_length2 = input("Enter the second length:")
    side_length3 = input("Enter the thrid length:")
    is_triangle(side_length1, side_length2, side_length3)
    pass


if __name__ == '__main__':
    main()

