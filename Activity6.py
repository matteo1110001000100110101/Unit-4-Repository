'''
The user will enter a maximum and minimum numeric value.
The computer selects a random number in the range provided by the user.
The user attempts to guess the number selected by the computer.
After each guess an appropriate output is displayed and the user is prompted to try again.
The game continues until the user guesses the correct number. The computer then displays the number of attempts to obtain the correct answer.
Make sure that your output statements and input prompts are clear, and that your game is fun to play.
You must follow all style conventions and use internal documentation to make your program easy to understand.
'''

# NAME OF AUTHOR: Matteo Sorgini
# NAME OF THE PROGRAM:   Guessing Game
# DATE OF CREATION:   05-12-2022
# PURPOSE OF PROGRAM: To guess a random number between the maximum and minimum numeric value of which your user has entered  

#print("Welcome to the guessing game")
#print("Enter two different random numbers")

import random 
rom=int(input("enter smaller number"))
teo=int(input("enter larger number"))


player_name = input("Well hello there! What is your name?")
number_of_guesses = 0
print('Thank you! '+ player_name+ ' I am Guessing a number between your values:')
car = random.randint(rom , teo)

while number_of_guesses < 1000:
    guess = int(input())
    number_of_guesses += 1
    if guess < car:
        print('The guess you have inputed is too low and incorrect! Try again!')
    if guess > car:
        print('The guess you have inputed is too high and incorrect! Try again!')
    if guess == car:
        break
if guess == car:
    print('Congratulations you won! You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(car))
