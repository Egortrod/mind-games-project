from mind_games.scripts.games import calculate, arithmetic_progression, geometric_progression, gcd, prime
from mind_games.scripts.cli import greet, user_name, difficulty
from mind_games.scripts.supp import out
from colorama import Fore, Style
import time
# from mind_games.scripts.games.calculate import calc_out
# from mind_games.scripts.games.arithmetic_progression import ar_out
# from mind_games.scripts.games.geometric_progression import gm_out
# from mind_games.scripts.games.gcd import gcd_out
# from mind_games.scripts.games.prime import prime_out
# from mind_games.scripts.games.calculate import *


# def greet():
#     global user_name
#     print('Welcome to the Mind Games!\nMay I have your name?')
#     while True:
#         user_name = str(input('Input your name: '))
#         if len(user_name) <= 1:
#             print('Please, input correct name.')
#         else: break

global GAMES, ALL_DISCRIPTION
GAMES = ['calculate', 'arithmetic progression', 'geometric progression', 'divisor', 'prime number']
ALL_DISCRIPTION = {
        'calculate': 'сorrectly solve the provided expression,\nwhich can only contain addition, '
        'subtraction and multiplication operations',
        'arithmetic progression': 'put the correct number\nin the missing place, using the laws of arithmetic progression',
        'geometric progression': 'put the correct number\nin the missing place, using the laws of geometric progression',
        'divisor': 'determine the greatest common divisor of two numbers',
        'prime number': 'determine whether a given number is\nprime or not. **pay attention to how to give answers!**'
    }


def choose_game():
    global user_game
    time.sleep(0.8)
    print('You have to choose your game.')
    time.sleep(0.8)
    print('Input' + Fore.RED + ' index ' + Style.RESET_ALL + 'of chosen game:\n')
    time.sleep(0.8)
    for index, game in enumerate(GAMES):
        time.sleep(0.2)
        print(Fore.RED + '#' + str(index + 1) + Fore.WHITE + ' - ' + Fore.CYAN + str(game) + Style.RESET_ALL)
    while True:
        time.sleep(0.8)
        user_game = int(input('\nYour game in #'))
        if len(GAMES) - user_game >= 0 and len(GAMES) - user_game <= len(GAMES) and user_game != 0:
            time.sleep(0.8)
            print('Welcome to the ' + Fore.CYAN + str(GAMES[user_game - 1]) + ' game ' + Style.RESET_ALL + 'and have fun!\n')
            break
        else: 
            print(Fore.RED + "Input correct game's index!" + Style.RESET_ALL)


def discription_of_games():
    time.sleep(0.8)
    print(Fore.CYAN + ('-' * 75) + Style.RESET_ALL)
    print(f'In {GAMES[user_game - 1]} game you have to {ALL_DISCRIPTION[GAMES[user_game - 1]]}.')
    print(Fore.CYAN + ('-' * 75) + Style.RESET_ALL + '\n')
    # time.sleep(0.8)
    # print("Good luck and " + Fore.CYAN + "let's start!\n" + Style.RESET_ALL)
    # time.sleep(0.8)


def game():
    global correct_answers
    correct_answers = 0
    while correct_answers != 3:
        match user_game:
            case 1: #calculate
                calculate.main()
                time.sleep(0.8)
                if out() == False:
                    return
                correct_answers += 1
            case 2: #arithmetic progression
                arithmetic_progression.main()
                time.sleep(0.8)
                if out() == False:
                    return
                correct_answers += 1
            case 3: #geometric progression
                geometric_progression.main()
                time.sleep(0.8)
                if out() == False:
                    return
                correct_answers += 1
            case 4: #gcd
                gcd.main()
                time.sleep(0.8)
                if out() == False:
                    return
                correct_answers += 1
            case 5: #prime
                prime.main()
                time.sleep(0.8)
                if out() == False:
                    return
                correct_answers += 1
    if correct_answers == 3:
        # user_score += 1
        print('Congratulations, ' + Fore.CYAN + user_name() + Style.RESET_ALL + '!\n')
        time.sleep(0.8)
        print(Fore.CYAN + '!!!You won!!!' + Style.RESET_ALL)
        time.sleep(0.8)
        # print('Your score: ' + Fore.CYAN + str(user_score) + Style.RESET_ALL + '!\n')
        # time.sleep(0.8)
        # print(f'Congratulations!')


def main():
    try:
        greet()
        user_score = 0
        while True:
            choose_game()
            discription_of_games()
            difficulty()
            game()
            if correct_answers == 3:
                user_score += 1
            print('Your score = ' + Fore.CYAN + str(user_score) + '/5' + Style.RESET_ALL)
            if user_score == 5:
                print(Fore.GREEN + '\n!!!YOU WON ALL GAME!!! Congratulations!' + Style.RESET_ALL)
                time.sleep(0.8)
                print(Fore.CYAN + 'Goodbye! See you!' + Style.RESET_ALL)
                break
            time.sleep(0.8)
            print('Claim 5 points to ' + Fore.CYAN + 'WIN the game' + Style.RESET_ALL + '!' + '\n')
            time.sleep(0.8)
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
    except ValueError:
        time.sleep(0.8)
        print(Fore.RED + '\nYou entered the wrong value!\nStart the game from the beginning!'
              + '\nDo not just press ENTER in choises and use only integer values!' + Style.RESET_ALL)
                

if __name__ == '__main__':
    main()