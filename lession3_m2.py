"""
Задание Nº2 
А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить,
что тоже очень важно для программиста. ) 
и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому.
В следующих уроках мы дополним эту форму до полноценного теста, который будет проверять правильность ответов,
а пока - начнем с малого.
Напоминаем, что разделить эти данные тебе поможет команда ер внутри команды print,
например, чтобы разделить переменные знаком + нужно ввести:
print(a1, a2, a3, sep=+')
Подсказка: последняя стадия развития - Homo sapiens sapiens.
"""
# стадии развития человека: "Australopithecus", "Homo habilis", "Homo erectus", "Neanderthal", "Homo sapiens sapiens"
# Подсказка для пользователя
print("Введите этапы эволюции человека по порядку. Последняя стадия - Homo sapiens sapiens.")

# Запрашиваем у пользователя этапы эволюции
etap1 = input("Введите первый этап: ")
etap2 = input("Введите второй этап: ")
etap3 = input("Введите третий этап: ")
etap4 = input("Введите четвертый этап: ")
etap5 = "Homo sapiens sapiens"  # Последний этап уже известен

# Выводим все этапы, разделенные знаком =>
print(etap1, etap2, etap3, etap4, etap5, sep=' => ')
