# Gate
print("Input command gate")
while True:
    Command1 = input("Command: ").lower()
    if Command1 == "exit":
        break
    if Command1 != "exit" and Command1 != "open" \
        and Command1!= "close" \
        and Command1 != "help":
        print("Invalid command")
        continue
    if Command1 == "open":
        print("Opening gate")
    if Command1 == "close":
        print("Closing gate")
    if Command1 == "help":
        print("open - Открытие ворот")
        print("close - закрыть ворота")
        print("help - команды")
        print("exit - Выход из программы")