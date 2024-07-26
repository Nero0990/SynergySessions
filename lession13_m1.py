"""
Задание Nº1
Создайте матрицы 10x10 с случайными значениями. 
Сложите их и выведите на экран."""

import random

# Создание первой матрицы 10x10 с случайными значениями
matrix_1 = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]

# Создание второй матрицы 10x10 с случайными значениями
matrix_2 = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]

# Создание третьей матрицы 10x10, которая является суммой matrix_1 и matrix_2
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j]
             for j in range(10)] for i in range(10)]

# Вывод матриц
print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nМатрица 3 (Сумма матриц 1 и 2):")
for row in matrix_3:
    print(row)
