# Creates the collatz() function
def collatz(number):
    if number == 1:  # Ends the program
       print('Collatz Complete')
    elif number % 2 == 0: # Determines whether the number is even
       print(int(number // 2))
       collatz(number / 2)
    else: # If number is odd, returns the previous number multiplied by new parameters
        print(int(3 * number + 1))
        collatz(3 * number + 1)
try: # Used to return input parameters
    collatz(int(input('Enter number greater than 1: ')))
except ValueError: # If value entered is not an integer
    print('Non-integer entered, program will exit')
    