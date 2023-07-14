import time
from colorama import Fore, Style


def greet():
    global user_name
    time.sleep(0.2)
    print('Welcome to the' + Fore.CYAN +  ' Mind Games!' + Style.RESET_ALL)
    time.sleep(0.8)
    print('May I have your name?')
    while True:
        time.sleep(0.7)
        user_name = str(input(Fore.CYAN + 'Input your name: ' + Style.RESET_ALL))
        if len(user_name) <= 1 or not user_name.isalpha():
            print(Fore.RED + 'Please, input correct name.' + Style.RESET_ALL)
        else: break
    print('\nHello, ' + Fore.CYAN + user_name + Style.RESET_ALL + '!')


def difficulty():
    global diffs, user_diff
    time.sleep(0.8)
    print('Choose ' + Fore.RED + '# of difficulty ' + Style.RESET_ALL + 'of game:\n')
    time.sleep(0.6)
    diffs = ['easy', 'medium', 'hard']
    for idx, diff in enumerate(diffs):
        time.sleep(0.2)
        print(Fore.RED + '#' + str(idx + 1) + Style.RESET_ALL + ' - ' + Fore.CYAN + str(diff) + Style.RESET_ALL)
    time.sleep(0.8)
    while True:
        user_diff = int(input('\nYour difficult: '))
        if user_diff not in [1, 2, 3]:
            time.sleep(0.8)
            print(Fore.RED + 'Choose correct index!' + Style.RESET_ALL)
        else:
            break
    time.sleep(0.8)
    print("Good luck and " + Fore.CYAN + "let's start!\n" + Style.RESET_ALL)
    time.sleep(0.8)


def user_difficult_word():
    return diffs[user_diff - 1]


def user_difficult_idx():
    return int(user_diff - 1)


def user_name():
    return user_name


if __name__ == '__main__':
    greet()