from random import randint
from mind_games.scripts.cli import *
from colorama import Fore, Style
import math


def user_correct_answer():
    print(Fore.GREEN + 'Correct!' + Style.RESET_ALL)


def user_not_correct_answer():
    print('\n\'' + str(user_input) + '\' is ' + Fore.RED + 'wrong answer' + 
        Style.RESET_ALL + ' ;(\nCorrect answer was \'' + str(correct_answer) + "\'")  
    time.sleep(0.8)
    print("\nLet's try again, " + Fore.CYAN + str(user_name()) + Style.RESET_ALL + "!\n")
    

def comparing():
    global out
    out = True
    if correct_answer == user_input:
        user_correct_answer()
    else:
        user_not_correct_answer()
        out = False


def gcd_out():
    return out


def main():
    global correct_answer, user_input
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    correct_answer = math.gcd(first_number, second_number)
    print(f'Question: {first_number} and {second_number}')
    user_input = int(input('Your answer: '))
    comparing()