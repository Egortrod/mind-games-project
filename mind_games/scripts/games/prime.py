from random import randint
from colorama import Fore, Style
from mind_games.scripts.cli import *
from mind_games.scripts.supp import *


# def user_correct_answer():
#     print(Fore.GREEN + 'Correct!' + Style.RESET_ALL)


# def user_not_correct_answer():
#     print('\n\'' + str(user_input) + '\' is ' + Fore.RED + 'wrong answer' + 
#         Style.RESET_ALL + ' ;(\nCorrect answer was \'' + str(correct_answer) + "\'")  
#     time.sleep(0.8)
#     print("\nLet's try again, " + Fore.CYAN + str(user_name()) + Style.RESET_ALL + "!\n")
    

# def comparing():
#     global out
#     out = True
#     if correct_answer == user_input:
#         user_correct_answer()
#     else:
#         user_not_correct_answer()
#         out = False


# def prime_out():
#     return out


def main():
    global correct_answer, user_input
    match user_difficult_idx():
        case 0:
            question = randint(1, 50)
        case 1:
            question = randint(50, 500)
        case 2:
            question = randint(100, 10000)
    correct_answer = 'yes'
    print(f'Question: is {question} prime or not?')
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            correct_answer = 'no'
            break
    user_input = str(input('Your answer (yes/no): '))
    comparing(correct_answer, user_input)