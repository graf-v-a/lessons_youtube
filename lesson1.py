age = int(input("Сколько вам лет? "))
if age >= 18 and age <= 30:
    print("вЫ УЖЕ ЗРЕЛЫЙ")
elif age >= 30 and age <= 50:
    print("Вы в самом расцвете")
elif age >= 50 and age <= 100:
    print("Вы стары")
else:
    print("Вы еще слишком молоды).")
