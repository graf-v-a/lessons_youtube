# Касса
# 1. Попросить пользователя ввести цену товара, пока не введет "stop"
# 2. Если цена меньше 0, то вывести "нельзя с минусом"
# 3. Если цена не число, то пропустить
# 4. Вывести сумму всех цен

for x in range(30):
    print("-", end ="")

print("\n          Касса")
x = 0
for x in range(30):
    print("-", end ="")
print("\n")

price = None
price1 = 0
while True:
    price = input("Цена:")

    if price.lower() == "stop":
        break
    if not price.isnumeric():
        continue
    if int(price) < 0:
        print("Нельзя с минусом")
        continue
    price1 = int(price1) + int(price)
        # price1 = int(price1) + int(price)
print(f"Сумма: {price1}")