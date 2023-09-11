operationslist = ["Addition", "Subtraction", "Multiplication", "Division"]

__run__ = True

def introduction():
    print("Welcome to this simple calculator, please select an operation to perform...\n"
                      "\nType 'operationslist' for a list of available operations.")

def retryfunction():
    retry = input()
    if retry.lower() == "yes":
        print("Please input an operation to perform...\n")
        operator()
    if retry.lower() == "no":
        exit()
    else:
        print("Invalid input, please try again.")
        retryfunction()

def operator():
    operation = input("")
    if operation.lower() == "addition":
        try:
            firstnumber = float(input("Please input the first number here... "))
            secondnumber = float(input("\nPlease input the second number here... "))
        except:
            print("Invalid input, would you like to try again?")
            retryfunction()
        try:
           additionresult = float(firstnumber + secondnumber)
        except:
            print("Invalid addition, would you like to try again?\nYes/No")
            retryfunction()
        try:
            if additionresult - int(additionresult) == 0:
                additionresult = int(additionresult)
        except:
            print("Result is too big, would you like to try again?\nYes/No")
            retryfunction()
        print("\nYour result is " + str(additionresult))
        print("Would you like to try again? \nYes/No")
        retryfunction()

    if operation.lower() == "subtraction":
        try:
            firstnumber = float(input("Please input the first number here... "))
            secondnumber = float(input("\nPlease input the second number here... "))
        except:
            print("Invalid input, would you like to try again?")
            retryfunction()
        try:
            subtractionresult = float(firstnumber - secondnumber)
        except:
            print("Invalid subtraction, would you like to try again?\nYes/No")
            retryfunction()
        try:
            if subtractionresult - int(subtractionresult) == 0:
                subtractionresult = int(subtractionresult)
        except:
            print("Result is too big, would you like to try again?\nYes/No")
            retryfunction()
        print("\nYour result is " + str(subtractionresult))
        print("Would you like to try again? \nYes/No")
        retryfunction()

    if operation.lower() == "multiplication":
        try:
            firstnumber = float(input("Please input the first number here... "))
            secondnumber = float(input("\nPlease input the second number here... "))
        except:
            print("Invalid input, would you like to try again?")
            retryfunction()
        try:
            multiplicationresult = float(firstnumber * secondnumber)
        except:
            print("Invalid multiplication, would you like to try again?\nYes/No")
            retryfunction()
        try:
            if multiplicationresult - int(multiplicationresult) == 0:
                multiplicationresult = int(multiplicationresult)
        except:
            print("Result is too big, would you like to try again?\nYes/No")
            retryfunction()
        print("\nYour result is " + str(multiplicationresult))
        print("Would you like to try again? \nYes/No")
        retryfunction()

    if operation.lower() == "division":
        try:
            firstnumber = float(input("Please input the first number here... "))
            secondnumber = float(input("\nPlease input the second number here... "))
        except:
            print("Invalid input, would you like to try again?")
            retryfunction()
        try:
            divisionresult = float(firstnumber / secondnumber)
        except:
            print("Invalid division, would you like to try again?\nYes/No")
            retryfunction()
        try:
            if divisionresult - int(divisionresult) == 0:
                divisionresult = int(divisionresult)
        except:
            print("Result is too big, would you like to try again?\nYes/No")
            retryfunction()
        print("\nYour result is " + str(divisionresult))
        print("Would you like to try again? \nYes/No")
        retryfunction()

    if operation.lower() == "operationslist":
        for operation in operationslist:
            print(operation)
        operator()

    else:
        print("Invalid operation, please try again.")
        operator()
        
def calculator():
    introduction()
    operator()

if __run__ == True:
    calculator()
