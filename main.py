import random
from importlib.metadata import pass_none
import foolproof

print('Добро пожаловать в числовую угадайку')

main_digit = random.randint(1, 100)
guess_digit = pass_none(main_digit)
counter = 0

while guess_digit != main_digit:
    guess_digit = input()

    if not foolproof.is_valid(guess_digit):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    guess_digit = int(guess_digit)

    if guess_digit == main_digit:
        print('Вы угадали, поздравляем!')
    elif guess_digit < main_digit:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        counter += 1
    elif guess_digit > main_digit:
        print('Ваше число больше загаданного, попробуйте еще разок')
        counter += 1

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print('Колличество попыток:', counter)
