# Gate
# 1. Создать переменную is_open и присвоить ей значение True
# 2. Создать переменную Command1 и присвоить ей значение "open"
# 3. Создать цикл while True, который будет выполняться бесконечно
# 4. Внутри цикла запросить у пользователя ввести команду
# 5. Если команда не open, close, help, exit - вывести сообщение "invalid command"
# 6. Если команда open - вывести сообщение "opening gate"
# 7. Если команда close - вывести сообщение "closing gate"
# 8. Если команда help - вывести список команд
# 9. Если команда exit - выйти из программы

print("-" * 30)
print("          Gate")
print("-" * 30)
print("Input command gate")
print("1. open - открыть ворота")
print("2. close - закрыть ворота")
print("3. help - команды")
print("4. exit - выход из программы")
print("-" * 30)
# 1. Попросить пользователя ввести команду, пока не введет "exit"
# 2. Если команда не open, close, help, exit - вывести "invalid command"
# 3. Если команда open - вывести "opening gate"
# 4. Если команда close - вывести "closing gate"
# 5. Если команда help - вывести список команд
# 6. Если команда exit - выйти из программы
#
# for x in range(30):
#     print("-", end ="")
#
# print("\n          Gate")
# x = 0
# for x in range(30):
#     print("-", end ="")
# print("\n")
is_open = True
while True:
    Command1 = input("Command: ").lower()
    if Command1 == "exit":
        break
    if Command1 != "exit" and Command1 != "open" \
        and Command1 != "close" \
        and Command1 != "help":
        print("Invalid command")
        continue
    if Command1 == "open":
        if is_open:
            print("The gates are already open ")
        else:    
            print("Opening gate")
            is_open = True
    if Command1 == "close":
        if is_open:
            is_open = False
            print("Closing gate")
        else:
            print("The gates are already closed")
    if Command1 == "help":
        print("open - Открытие ворот")
        print("close - закрыть ворота")
        print("help - команды")
        print("exit - Выход из программы")