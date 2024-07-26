"""
Задание Nº1
Сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте, сколько из них равны нулю, и выведите это количество.
"""

N = int(input("Введите количество введенных чисел N: "))

count_zero = 0

current_count = 0

while current_count < N:
    number = int(input("Введите число: "))
    if number == 0:
        count_zero += 1
    current_count += 1

print("Количество введенных чисел:", current_count)
print("Количество введенных нулей:", count_zero)
