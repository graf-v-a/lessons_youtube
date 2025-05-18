# Gate
print("Input command gate")
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