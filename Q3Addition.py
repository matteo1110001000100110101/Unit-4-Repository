# NAME OF AUTHOR:  Matteo Sorgini
# NAME OF THE PROGRAM:  User addition questions calculator
# DATE OF CREATION:  05-19-2022
# PURPOSE OF PROGRAM:  To find the sum of two numbers in an equation using addition

# VARIABLE DEFINITION
print("Hello, and welcome to Asking users addition questions")
print("Please enter any two numbers you would like")
import random



teo = random.randint(1, 100)
zoo = random.randint(1, 100)


random.seed()

# INPUT



# PROCESSING

answer = teo + zoo
print('What is the answer of these two added numbers' + str(teo) + '+' + str(zoo))

dog = int(input())
if dog == answer:
    print("You have been granted the correct answer")
else:
    print("It's alright you'll get it right next time")

# OUTPUT

print('Thank you for using the User addition questions calculator')
