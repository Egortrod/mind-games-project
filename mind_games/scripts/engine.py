from mind_games.scripts.games import calculate, arithmetic_progression
from mind_games.scripts.games.calculate import calc_out
from mind_games.scripts.games.arithmetic_progression import ar_out
from mind_games.scripts.cli import greet, user_name
import time
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
    print('Input index of chosen game:\n')
    time.sleep(0.8)
    for index, game in enumerate(games):
        time.sleep(0.2)
        print(f'#{index + 1} - {game}')
    while True:
        time.sleep(0.8)
        user_game = int(input('\nYour game in #'))
        if len(games) - user_game >= 0 and len(games) - user_game <= len(games) and user_game != 0:
            time.sleep(0.8)
            print(f'Welcome to the {games[user_game - 1]} game and have fun!\n')
            break
        else: 
            time.sleep(0.8)
            print("Input correct game's index")


def discription_of_games():
    all_discriptions = {
        'calculate': 'сorrectly solve the provided expression,\nwhich can only contain addition, subtraction and multiplication operations',
        'arithmetic progression': 'put the correct number in the missing place',
        'geometric progression': '333333333333333333333333333333333333333333333333333333333333333',
        'gcd': '444444444444444444444444444444444444444444444444444444444444444',
        'prime': '55555555555555555555555555555555555555555555555555555555555555555555'
    }
    time.sleep(0.8)
    print('-' * 75)
    print(f'In {games[user_game - 1]} game you have to {all_discriptions[games[user_game - 1]]}.')
    print('-' * 75, '\n')
    time.sleep(0.8)
    print(f"Good luck and let's start!\n")
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
            case 2: #arithmetic
                arithmetic_progression.main()
                time.sleep(0.8)
                correct_answers += 1
                if ar_out() == False:
                    return
    if correct_answers == 3:
        print(f'Congratulations, {user_name()}!\n\n')
        time.sleep(0.8)
        print('!!!You won!!!\n')
        # print(f'Congratulations!')


def main():
    greet()
    while True:
        choose_game()
        discription_of_games()
        game()
        print('Would you like to continue?\nIf yes, tap SPACE and ENTER.\nIf no, just tap ENTER.')
        time.sleep(0.8)
        user_ans = str(input('\nContinue?\n'))
        if user_ans != ' ':
            print('See you!')
            break
                

if __name__ == '__main__':
    main()