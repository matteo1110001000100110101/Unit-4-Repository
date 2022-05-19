# NAME OF AUTHOR: Matteo Sorgini
# NAME OF THE PROGRAM:   Random Number Generator
# DATE OF CREATION:   05-12-2022
# PURPOSE OF PROGRAM:  To output any given number by running the program and entering two random numbers

print("Welcome to the Random Number Generator")
print("Enter random number")
print("Thank you very much your number has been randomized between your values of your variables")
# VARIABLE DEFINITION
import random

rom = int(input())
teo = int(input())



random.seed()
print(random.randint(rom , teo))

# PROCESSING



# OUTPUT
print("Thank you for using the Random Number Generator, enjoy your day!")
