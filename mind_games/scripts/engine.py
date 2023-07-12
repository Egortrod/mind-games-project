from mind_games.scripts.games import calculate, arithmetic_progression, geometric_progression
from mind_games.scripts.games.calculate import calc_out
from mind_games.scripts.games.arithmetic_progression import ar_out
from mind_games.scripts.games.geometric_progression import gm_out
from mind_games.scripts.cli import greet, user_name
import time
from colorama import Fore, Style
# from mind_games.scripts.games.calculate import *


# def greet():
#     global user_name
#     print('Welcome to the Mind Games!\nMay I have your name?')
#     while True:
#         user_name = str(input('Input your name: '))
#         if len(user_name) <= 1:
#             print('Please, input correct name.')
#         else: break


def choose_game():
    global games, user_game
    games = ['calculate', 'arithmetic progression', 'geometric progression', 'gcd', 'prime']
    time.sleep(0.8)
    print('You have to choose your game.')
    time.sleep(0.8)
    print('Input' + Fore.RED + ' index ' + Style.RESET_ALL + 'of chosen game:\n')
    time.sleep(0.8)
    for index, game in enumerate(games):
        time.sleep(0.2)
        print(Fore.RED + '#' + str(index + 1) + Fore.WHITE + ' - ' + Fore.CYAN + str(game) + Style.RESET_ALL)
    while True:
        time.sleep(0.8)
        user_game = int(input('\nYour game in #'))
        if len(games) - user_game >= 0 and len(games) - user_game <= len(games) and user_game != 0:
            time.sleep(0.8)
            print('Welcome to the ' + Fore.CYAN + str(games[user_game - 1]) + ' game ' + Style.RESET_ALL + 'and have fun!\n')
            break
        else: 
            time.sleep(0.8)
            print("Input correct game's index")


def discription_of_games():
    all_discriptions = {
        'calculate': 'сorrectly solve the provided expression,\nwhich can only contain addition, subtraction and multiplication operations',
        'arithmetic progression': 'put the correct number\nin the missing place, using the laws of arithmetic progression',
        'geometric progression': 'put the correct number\nin the missing place, using the laws of geometric progression',
        'gcd': '444444444444444444444444444444444444444444444444444444444444444',
        'prime': '55555555555555555555555555555555555555555555555555555555555555555555'
    }
    time.sleep(0.8)
    print(Fore.CYAN + ('-' * 75) + Style.RESET_ALL)
    print(f'In {games[user_game - 1]} game you have to {all_discriptions[games[user_game - 1]]}.')
    print(Fore.CYAN + ('-' * 75) + Style.RESET_ALL + '\n')
    time.sleep(0.8)
    print("Good luck and " + Fore.CYAN + "let's start!\n" + Style.RESET_ALL)
    time.sleep(0.8)


def game():
    correct_answers = 0
    while correct_answers != 3:
        match user_game:
            case 1: #calculate
                calculate.main()
                time.sleep(0.8)
                correct_answers += 1
                if calc_out() == False:
                    return
            case 2: #arithmetic progression
                arithmetic_progression.main()
                time.sleep(0.8)
                correct_answers += 1
                if ar_out() == False:
                    return
            case 3: #geometric progression
                geometric_progression.main()
                time.sleep(0.8)
                correct_answers += 1
                if gm_out() == False:
                    return
    if correct_answers == 3:
        print(f'Congratulations, {user_name()}!\n\n')
        time.sleep(0.8)
        print(Fore.CYAN + '!!!You won!!!\n' + Style.RESET_ALL)
        # print(f'Congratulations!')


def main():
    greet()
    while True:
        choose_game()
        discription_of_games()
        game()
        print('Would you like to continue?')
        print('If' + Fore.GREEN + ' yes' + Style.RESET_ALL + ', just tap ' + Fore.CYAN + 'ENTER.' + Style.RESET_ALL)
        print('If' + Fore.RED + ' no' + Style.RESET_ALL + ', tap ' + Fore.CYAN + 'any other key.' + Style.RESET_ALL)
        time.sleep(0.8)
        user_ans = str(input('\nContinue?\n'))
        if user_ans == '':
            continue
        else:
            print(Fore.CYAN + 'See you!' + Style.RESET_ALL)
            break
                

if __name__ == '__main__':
    main()