def add_one(number):
    return number + 1

import random
import sys
from random import randint
def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius! babe')
            return True

    else:
        print('hey idiot, i said 1 to 10 ')
        return False