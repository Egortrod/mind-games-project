from random import randint
from mind_games.scripts.cli import *
from colorama import Fore, Style


def user_correct_answer():
    print(Fore.GREEN + 'Correct!' + Style.RESET_ALL)


def user_not_correct_answer():
    print('\n\'' + str(user_input) + '\' is ' + Fore.RED + 'wrong answer' + 
          Style.RESET_ALL + ' ;(\nCorrect answer was \'' + str(correct_answer) + "\'")  
    time.sleep(0.8)
    print("\nLet's try again, " + Fore.CYAN + str(user_name()) + Style.RESET_ALL + "!\n")
    

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
    match user_difficult_idx():
        case 0:
            first_number = randint(100, 200)
            second_number = randint(1, 100)
            exp = variants_of_exp[randint(1, 2)]
        case 1:
            first_number = randint(100, 500)
            second_number = randint(50, 100)
            exp = variants_of_exp[randint(1, 2)]
        case 2:
            first_number = randint(50, 100)
            second_number = randint(50, 100)
            exp = variants_of_exp[0]
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


# if __name__ == '__main__':       
#     greet()
#     main()