# Задача 28: 
# Вводится десятичное число. Реализовать алгоритм его перевода в 
# двоичную систему счисления через рекурсию. Нельзя использовать функцию bin()

# *Пример:*
#    10
#    *Вывод:*
#    1010"""
    
def binary(n):
    if n == 0 or n == 1:
        return f'{n}'
    return binary(n // 2) + f'{n % 2}'

n = int(input("Введите десятичное число: "))
print(binary(n))