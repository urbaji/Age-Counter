try:
    n = int(input("Enter your age: "))
    
    if n % 2 == 0:
        print("Your age number is an even number.")
    else:
        print("Your age number is an odd number.")

except ValueError: 
    print("The number you have entered is not an integer, please try again.")

except Exception as ex:
    print(f"There is some error in the lower part of your code: {ex}.")

