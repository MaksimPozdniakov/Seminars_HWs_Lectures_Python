# Написать программу, угадай число, только загадывает пользователь, а отгадывает компьютер.
user_number = int(input('Загадайте число: '))

import random 

result = None
min_number = 1
max_number = 100

while result != '=':
    coputer_number = random.randint(min_number, max_number)
    print(coputer_number)
    result = input('= , < , > ')
    
    if result == '>':
        min_number =  coputer_number + 1
    
    elif result == '<':
        max_number = coputer_number - 1

print('Компьютер отгадал ')



