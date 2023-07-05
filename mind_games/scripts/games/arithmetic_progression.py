from random import randint
from mind_games.scripts.cli import *


def user_correct_answer():
    print('Correct!')


def user_not_correct_answer():
    print(f"\n'{user_input}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'."
          f"\nLet's try again, {user_name()}!\n")
    

def comparing():
    global out
    out = True
    if correct_answer == user_input:
        user_correct_answer()
    else:
        user_not_correct_answer()
        out = False


def ar_out():
    return out


def main():
    global correct_answer, user_input
    first_number = randint(1, 10)
    diff = randint(2, 5)
    result = []
    for idx in range(10):
        result.append(first_number + idx * diff)
    replaced_index = randint(0, 9)
    correct_answer = result[replaced_index]
    result[replaced_index] = '..'
    print('Question:', ' '.join([str(x) for x in result]))
    user_input = int(input('Your answer: '))
    comparing()