import random
import string
import sys

def cows_bulls():
    num = ''.join([random.choice(string.digits) for i in range(4)])
    num = list(num)
    print(num)
    cows = 0
    bulls = 0
    guess=0
    attempt =0
    while(num != guess):
        guess = input("guess the number: ")
        if(len(guess) == 4):
            guess = list(guess)
        else:
            print("Invalid. Please enter a four digit number: ")
            continue
            
        for i in range(4):
            if num[i] == guess[i]:
                cows = cows + 1
            elif num[i] in guess and num[i] != guess[i]:
                bulls = bulls + 1
        attempt = attempt + 1
        print(cows,"cows")
        print(bulls,"bulls")
    print("number of valid attempts are: ",attempt)
            
if __name__ == "__main__":
    cows_bulls()
