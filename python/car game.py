command = ""
while command != "quit":
    command=input("> ").lower()
    if command == "start":
        print("car starting")
    elif command == "stop":
        print("car stopping")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - exit the program
        """)
    elif command == "quit":
        break
    else:
        print("invalid input")