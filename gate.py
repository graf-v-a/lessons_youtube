# Gate
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
while True:
    Command1 = input("Command: ")
    if Command1.lower() == "exit":
        break
    if Command1.lower() != "exit" and Command1.lower() != "open" \
        and Command1.lower() != "close" \
        and Command1.lower() != "help":
        print("Invalid command")
        continue
    if Command1.lower() == "open":
        print("Opening gate")
    if Command1.lower() == "close":
        print("Closing gate")
    if Command1.lower() == "help":
        print("open - Открытие ворот")
        print("close - закрыть ворота")
        print("help - команды")
        print("exit - Выход из программы")