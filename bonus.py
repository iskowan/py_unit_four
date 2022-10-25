def calculator(salary, years):
    if int(years) >= 5:
        finalSalary = (int(salary) * 0.05) + int(salary)
        print(finalSalary, "is your new annual salary")
    else:
        print("Sorry, but you are not eligable for a raise at this time.")

def main():
    salary = input("What is your current annual salary?:")
    years = input("How many years have you worked here?:")
    calculator(salary, years)

main()