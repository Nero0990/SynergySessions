"""
Задание Nº2
Вводится натуральное число Х. 
Подсчитайте количество натуральных делителей числа Х (включая 1 и само число). x ≤ 2e9 (2 миллиарда)
"""

X = int(input("Введите натуральное число X (X не должно превышать 2e9): "))

if X > 2e9:
    print("Число X превышает допустимый предел.")
else:
    count_divisors = 0
    i = 1

    while i*i <= X:
        if X % i == 0:
            count_divisors += 2 if i*i != X else 1
        i += 1

    print("Количество натуральных делителей числа X:", count_divisors)
