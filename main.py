from string import ascii_letters, digits
from random import choice, shuffle

SYMBOLS = '!@#$%^&*()'


def main():
    print('Welcome to the PyPassword Generator')
    letters = int(input('How many letters would like in your password: '))
    symbols = int(input('How many symbols would you like: '))
    numbers = int(input('How many numbers would you like: '))

    result = []
    result.extend(add_characters(letters, ascii_letters))
    result.extend(add_characters(symbols, SYMBOLS))
    result.extend(add_characters(numbers, digits))
    shuffle(result)

    print(f'Here\'s your password: {"".join(result)}')


def add_characters(frequency, characters):
    return [choice(characters) for _ in range(frequency)]


if __name__ == '__main__':
    main()
