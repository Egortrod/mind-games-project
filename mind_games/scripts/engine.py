from games import calculate


def greet():
    global user_name
    print('Welcome to the Mind Games!\nMay I have your name?')
    while True:
        user_name = str(input('Input your name: '))
        if len(user_name) <= 1:
            print('Please, input correct name.')
        else: break


def choose_game():
    global games, user_game
    games = ['calculate', 'ar progression', 'geom progression', 'gcd']
    print('Choose your game.\nInput index of chosen game:\n') 
    for index, game in enumerate(games):
        print(f'#{index + 1} - {game}')
    while True:
        user_game = int(input('\nYour game in #'))
        if len(games) - user_game >= 0 and len(games) - user_game <= len(games) and user_game != 0:
            print(f'Welcome to the {games[user_game - 1]} game!\nHave fun!')
            break
        else: 
            print("Input correct game's index")


def discription_of_games():
    all_discriptions = {
        'calculate':'111111111111111111111111111111111111111111111111111111111',
        'ar progression':'22222222222222222222222222222222222222222222222222222222222222',
        'geom progression':'333333333333333333333333333333333333333333333333333333333333333',
        'gcd':'444444444444444444444444444444444444444444444444444444444444444'
    }
    print(f'In {games[user_game - 1]} game you have to {all_discriptions[games[user_game - 1]]}.'
          f"\nGood luck and let's start!")


def game():
    calculate.calc()
    # if calculate.correct_answers() == 3:
    #     print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    greet()
    choose_game()
    discription_of_games()
    game()