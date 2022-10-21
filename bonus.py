salary = input("What is your current salary?:")
years = input("How many years have you worked here?:")

if int(years) >= 5:
    finalSalary = (int(salary) * 0.05) + int(salary)
    print(finalSalary, "is your new annual salary")
else:
    print("Sorry, but you are not eligable for a raise at this time.")