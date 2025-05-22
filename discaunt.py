print("===== Программа для расчета скидки =====")
print('Для выхода из программы, наберите "выход"')
print('-' * 40)

while True:
    price_input = input("Введите стоимость товара (в руб.): ").replace(",", ".")
    if price_input.lower() == "выход":
        break

    discount_input = input("Введите скидку (в %): ").replace(",", ".")
    if discount_input.lower() == "выход":
        break

    # Проверка, являются ли строки корректными числами
    if (price_input.replace('.', '', 1).isdigit() and
            discount_input.replace('.', '', 1).isdigit()):

        price = float(price_input)
        discount = float(discount_input)

        if discount > 100:
            print("Скидка не может превышать 100%. Повторите ввод.")
            continue

        total = price - (price * discount / 100)

        print('-' * 30)
        print(f"Итоговая сумма: {round(total, 2)} руб.")
        print('-' * 30)
    else:
        print("---- Ошибка ввода! ----")
        print("Введите только числа. Например: 199.99 или 25")
        input("Для продолжения нажмите Enter")