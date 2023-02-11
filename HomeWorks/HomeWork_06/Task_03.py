# Задание №1. Задайте число. Составьте список чисел Фибоначчи.

# старое решение

# n = 8
# a = 0
# b = 1
#
# fibonacci_range = []
#
# for i in range(n):
#     fibonacci_range.append(a)
#     a, b = b, a + b
# print(fibonacci_range)

# новое решение

n = 8
range_list = [0, 1]
[range_list.append(range_list[-2] + range_list[-1]) for i in range(0, n - 2)]
print(range_list)


