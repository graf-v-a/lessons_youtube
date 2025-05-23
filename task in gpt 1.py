# Задача 1: Угадай число
# Уровень: Начальный
# Цель: Практика input(), int(), if, while
#
# Условие:
# Программа загадывает число от 1 до 10. Пользователь должен угадать число. После каждой попытки программа говорит, верно ли угадано. Если нет — просит снова ввести число.
#
# Подсказка:
#
# Используй import random и random.randint(1, 10) для загадывания числа.
#
# Используй while, чтобы повторять попытки.

import random
# Задаем случайное число от 1 до 10
number = random.randint(1, 10)
attempts = 0
# Начинаем бесконечный цикл

while True:
    # Запрашиваем у пользователя число
    guess = int(input("Угадай число от 1 до 10: "))
    attempts += 1
    if guess < 1 or guess > 10:
        print("Пожалуйста, введите число от 1 до 10.")
        continue
    # Проверяем, угадал ли пользователь
    if guess == number:
        print(f"Поздравляю! Ты угадал число c {attempts} попытки.")
        break  # Выходим из цикла, если угадали
    else:
        print("Попробуй еще раз.")