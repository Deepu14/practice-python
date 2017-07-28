"""This time, we’re going to do exactly the opposite. You, the user, will have in your head a number 
between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, 
too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number."""


import random
import sys

def guess_game2(number):
    attempts = 0
    guess = 0
    #number = int(input("Enter a number between 0 and 100: "))
    if(number in range(0,101)):
        while(guess != number):
            guess = random.randint(1,100)
            attempts += 1
            print(guess)
            if(guess == number):
                print("system guessed the number")
            elif (guess < number):
                print("too low")
            else:
                print("too high") 
    else:
        print("Please enter a number between 0 and 100 ")
        sys.exit()
    print("number of attempts are: ", attempts)

guess_game2(100)
guess_game2(1000)
guess_game2(9)
