# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
# отдельных текстовых файлах.

# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def compression_algorithm(my_str):
    letter = my_str[0]
    count = 1
    result = ''

    for i in my_str[1:]:
        if i == letter:
            count += 1
        else:
            result += str(count) + letter
            letter = i
            count = 1
    result += str(count) + letter
    return result

def decryption_algorithm(new_str):
    pars_my_str = []
    for i in range(0, len(new_str)):
        pars_my_str.append(new_str[i])

    list_tuples = []
    for i in range(0, len(pars_my_str) - 1, 2):
        list_tuples.append((int(pars_my_str[i]), pars_my_str[i + 1]))
    create_list_tuples = list(list_tuples)

    general_list = [e for l in create_list_tuples for e in l]

    new_str = ''
    for i in range(1, len(general_list), 2):
        new_str += general_list[i] * general_list[i - 1]
    return new_str

my_str = 'aaaaabbbcccc'
print(f'Изначальная строка: {my_str} -> Строка после сжатия: {compression_algorithm(my_str)}')
print(f'Сжатая строка: {compression_algorithm(my_str)} -> Расшифрованная строка'
      f' {decryption_algorithm(compression_algorithm(my_str))}')

result = compression_algorithm(my_str)
with open('compression_result.txt', 'w', encoding='UTF-8') as my_str:
    my_str.write('Строка после сжатия: ')
    my_str.write(result)

with open('compression_result.txt', 'r', encoding='UTF-8') as my_str:
    my_str1 = my_str.readline()
my_str1 = my_str1.replace('Строка после сжатия: ', '')

new_result = decryption_algorithm(my_str1)

with open('decryption_result.txt', 'w', encoding='UTF-8') as new_str:
    new_str.write('Расшифрованная строка: ')
    new_str.write(new_result)






