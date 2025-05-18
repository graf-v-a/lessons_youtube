# Gate
print("---------Программа управления воротами--------------")
print("Input command gate")
is_open = True
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
        if is_open:
            print("It`s already open.")
        else:
            print("Opening gate.")
            is_open = True
    if Command1 == "close":
        if is_open:
            print("Closing gate")
            is_open = False
        else:
            print("It`s already closed.")

    if Command1 == "help":
        print("open - Открытие ворот")
        print("close - закрыть ворота")
        print("help - команды")
        print("exit - Выход из программы")