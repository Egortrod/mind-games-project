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


# def gm_out():
#     return out


def main():
    global correct_answer, user_input
    first_number = randint(1, 25)
    diff = randint(2, 5)
    result = []
    for idx in range(1, 6):
        result.append(first_number * diff ** (idx-1))
    replaced_index = randint(0, 4)
    correct_answer = result[replaced_index]
    result[replaced_index] = '..'
    print('Question:', ' '.join([str(x) for x in result]))
    user_input = int(input('Your answer: '))
    comparing(correct_answer, user_input)


# if __name__ == '__main__':
#     main()
