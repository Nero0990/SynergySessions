"""Задание Nº3
Во входную строку водится последовательность чисел через пробел. 
Для каждого числа выведите слово "YES" (в отдельной строке), 
если это число ранее встречалось в последовательности или "NO" , если не встречалось."""

# Вводим последовательность чисел через пробел
numbers = input("Введите последовательность чисел через пробел: ").split()

# Создаем пустое множество для хранения уникальных чисел
unique_numbers = set()

# Проходим по каждому числу в последовательности
for num in numbers:
    # Если число уже есть в множестве, выводим "YES"
    if num in unique_numbers:
        print("YES")
    # Если числа нет в множестве, выводим "NO" и добавляем его в множество
    else:
        print("NO")
        unique_numbers.add(num)
