from mind_games.scripts.cli import *


def comparing(correct_answer, user_input):
    global out
    out = True
    if correct_answer == user_input:
        user_correct_answer()
    else:
        user_not_correct_answer(correct_answer, user_input)
        out = False


def user_correct_answer():
    print(Fore.GREEN + 'Correct!' + Style.RESET_ALL)


def user_not_correct_answer(correct_answer, user_input):
    print('\n\'' + str(user_input) + '\' is ' + Fore.RED + 'wrong answer' + 
          Style.RESET_ALL + ' ;(\nCorrect answer was \'' + str(correct_answer) + "\'")  
    time.sleep(0.8)
    print("\nLet's try again, " + Fore.CYAN + str(user_name()) + Style.RESET_ALL + "!\n")


def out():
    return out