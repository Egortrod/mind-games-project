def greet():
    global user_name
    print('Welcome to the Mind Games!\nMay I have your name?')
    while True:
        user_name = str(input('Input your name: '))
        if len(user_name) <= 1:
            print('Please, input correct name.')
        else: break
    print(f'\nHello, {user_name}!')


def user_name():
    return user_name


if __name__ == '__main__':
    greet()