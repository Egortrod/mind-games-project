import time
from colorama import Fore, Style


def greet():
    global user_name
    time.sleep(0.2)
    print(Fore.GREEN + 'Welcome to the Mind Games!')
    time.sleep(0.7)
    print('May I have your name?' + Style.RESET_ALL)
    while True:
        time.sleep(0.7)
        user_name = str(input(Fore.CYAN + 'Input your name: ' + Style.RESET_ALL))
        if len(user_name) <= 1 or not user_name.isalpha():
            print(Fore.RED + 'Please, input correct name.' + Style.RESET_ALL)
        else: break
    print(Fore.GREEN + f'\nHello, {user_name}!')


def user_name():
    return user_name


if __name__ == '__main__':
    greet()