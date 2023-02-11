# Задание №1. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Введите число: '))

def fibonacci(n):
    fibonacci_range = []
    a = 1
    b = 1
    for i in range(n):
        fibonacci_range.append(a)
        a, b = b, a + b

    a = 0
    b = 1
    for i in range(n + 1):
        fibonacci_range.insert(0, a)
        a, b = b, a - b
    return fibonacci_range

print(fibonacci(n))






