from mind_games.scripts.games import calculate
from mind_games.scripts.games.calculate import outt
from mind_games.scripts.cli import greet, user_name
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
    games = ['calculate', 'ar progression', 'geom progression', 'gcd']
    print('You have to choose your game.\nInput index of chosen game:\n') 
    for index, game in enumerate(games):
        print(f'#{index + 1} - {game}')
    while True:
        user_game = int(input('\nYour game in #'))
        if len(games) - user_game >= 0 and len(games) - user_game <= len(games) and user_game != 0:
            print(f'Welcome to the {games[user_game - 1]} game and have fun!\n')
            break
        else: 
            print("Input correct game's index")


def discription_of_games():
    all_discriptions = {
        'calculate':'сorrectly solve the provided expression,\nwhich can only contain addition, subtraction and multiplication operations',
        'ar progression':'22222222222222222222222222222222222222222222222222222222222222',
        'geom progression':'333333333333333333333333333333333333333333333333333333333333333',
        'gcd':'444444444444444444444444444444444444444444444444444444444444444'
    }
    print('-' * 75)
    print(f'In {games[user_game - 1]} game you have to {all_discriptions[games[user_game - 1]]}.')
    print('-' * 75, '\n')
    print(f"Good luck and let's start!\n")


def game():
    correct_answers = 0
    while correct_answers != 3:
        match user_game:
            case 1: #calculate
                calculate.main()
                correct_answers += 1
                if outt() == False:
                    return
    if correct_answers == 3:
        print(f'Congratulations, {user_name()}!')
        # print(f'Congratulations!')


def main():
    greet()
    choose_game()
    discription_of_games()
    game()


if __name__ == '__main__':
    main()