import time
from colorama import Fore, Style


def greet():
    global user_name
    time.sleep(0.2)
    print('Welcome to the' + Fore.CYAN +  ' Mind Games!' + Style.RESET_ALL)
    time.sleep(0.7)
    print('May I have your name?')
    while True:
        time.sleep(0.7)
        user_name = str(input(Fore.CYAN + 'Input your name: ' + Style.RESET_ALL))
        if len(user_name) <= 1 or not user_name.isalpha():
            print(Fore.RED + 'Please, input correct name.' + Style.RESET_ALL)
        else: break
    print('\nHello, ' + Fore.CYAN + user_name + Style.RESET_ALL + '!')


def dificult():
    global diffs, user_diff
    print('Choose ' + Fore.RED + '# of difficulty ' + Style.RESET_ALL + 'of game:')
    diffs = ['easy', 'medium', 'hard']
    for idx, diff in enumerate(diffs):
        print(Fore.RED + '#' + str(idx) + Style.RESET_ALL + ' - ' + Fore.CYAN + str(diff) + Style.RESET_ALL)
    user_diff = int(input('Your difficult: '))
    while True:
        if user_diff not in [1, 2, 3]:
            print(Fore.RED + 'Choose correct index!' + Style.RESET_ALL)
        else:
            break


def user_difficult_word():
    return diffs[user_diff - 1]


def user_difficult_idx():
    return user_diff - 1


def user_name():
    return user_name


if __name__ == '__main__':
    greet()