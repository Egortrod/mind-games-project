from random import randint
# from engine import user_name as name


def calc():
    global correct_answers
    correct_answers = 0
    variants_of_exp = ['*', '-', '+']
    while correct_answers != 3:
        first_number = randint(1, 25)
        second_number = randint(1, 25)
        exp = variants_of_exp[randint(0, 2)]
        print(f'Question: {first_number} {exp} {second_number}')
        user_input = int(input('Your answer: '))
        match exp:
            case '*':
                correct_answer = second_number * first_number
                if correct_answer == user_input:
                    print('Correct!')
                    correct_answers += 1
                else:
                    print(f"'{user_input}' is wrong answer ;(. "
                          f"Correct answer was '{correct_answer}'.")
                        #   f"\nLet's try again, {name}!")
                    break
            case '-':
                correct_answer = first_number - second_number
                if correct_answer == user_input:
                    print('Correct!')
                    correct_answers += 1
                else:
                    print(f"'{user_input}' is wrong answer ;(. "
                          f"Correct answer was '{correct_answer}'.")
                        #   f"\nLet's try again, {name}!")
                    break
            case '+':
                correct_answer = second_number + first_number
                if correct_answer == user_input:
                    print('Correct!')
                    correct_answers += 1
                else:
                    print(f"'{user_input}' is wrong answer ;(. "
                          f"Correct answer was '{correct_answer}'.")
                        #   f"\nLet's try again, {name}!")
                    break

if __name__ == '__main__':       
    calc()