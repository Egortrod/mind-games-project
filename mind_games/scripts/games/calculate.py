from random import randint
from mind_games.scripts.cli import *


def user_correct_answer():
    print('Correct!')


def user_not_correct_answer():
    print(f"\n'{user_input}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    time.sleep(0.8)
    print(f"\nLet's try again, {user_name()}!\n")
    

def comparing():
    global out
    out = True
    if correct_answer == user_input:
        user_correct_answer()
    else:
        user_not_correct_answer()
        out = False


def calc_out():
    return out


def main():
    global user_input
    global correct_answer
    variants_of_exp = ['*', '-', '+']
    first_number = randint(1, 25)
    second_number = randint(1, 10)
    exp = variants_of_exp[randint(0, 2)]
    print(f'Question: {first_number} {exp} {second_number}')
    user_input = int(input('Your answer: '))
    match exp:
            case '*':
                correct_answer = second_number * first_number
                comparing()
            case '-':
                correct_answer = first_number - second_number
                comparing()
            case '+':
                correct_answer = second_number + first_number
                comparing()


if __name__ == '__main__':       
    greet()
    main()