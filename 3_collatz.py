import sys
def collatz(number): # defines collatz function with number parameter
    while number != 1: # starts the loop
        if number %2 == 1: # determines if number is odd
            number = 3 * number + 1
            print(number)
        else: # if number is even
            number = number // 2
            print(number)
    sys.exit()
print("Enter number:") #requests for user to input number.
while True: # main loop
    try: # for exception handling
        number = int(input()) # places user input inside variable(userinput)
        collatz(number) # calls collatz function
    except ValueError: # if a non-integer value is entered by the user, the next line will be executed.
        print("Please enter an integer.")
