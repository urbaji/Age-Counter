try:
    n = int(input("Enter your age: "))
except ValueError: 
    print("The number you have entered is not an integer, please try again.")
else:
    if n % 2 == 0:
        print("Your number is an even number.")
    else:
        print("Your number is an odd number.")
