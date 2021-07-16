num1 = 22



if num1 > 10:
    print("The number is bigger than 10")
    print("Thanks")
else:
    print("Not larger than 10")
    print("Exiting program")



try:
    x = int(input("Enter a num. between 0 and 3: "))
    print(x / 0)
except ValueError:
    print("Sorry you must give a whole number.")
    print("Eg: 1,2,or 3")
except Exception as error:
    print(error)
except ZeroDivisionError as error:
    print("Can't divide by 0, sorry")