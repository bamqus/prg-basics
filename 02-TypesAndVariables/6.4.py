import random
# COMPUTER TURN
computer = random.randint(1, 6)
# YOUR TURN
you = int(input('Guess the number (1–6): '))
# RESULT
print(f'You won: {you == computer}')
print(f'(Computer had: {computer})')