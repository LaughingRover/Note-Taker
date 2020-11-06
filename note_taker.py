def file_checker(filename):
    """
    Checks if the file exists
    """
    try:
        outputFile = open(filename, 'r')
        outputFile.close()
    except FileNotFoundError:
        return False


def read_file(filename):
    """
    read an existing file and displays it to the user
    """
    print("-----------NOTE TAKER-----------")
    f = open(filename, 'r')
    f1 = f.readlines()
    count = 1
    for line in f1:
        print(str(count) + ". " + line)
        count += 1
    f.close()


def write_file(filename):
    """
    Write a new file or overwrite an existing one
    """
    f = open(filename, 'w')
    print("Type 'exit()' on a new line to save entry and exit")
    flag = 'exit()'
    while True:
        lineInput = str(input(">>> "))
        if lineInput == flag:
            break
        else:
            f.write(lineInput + "\n")
    f.close()
    print("File saved")


def append_file(filename):
    """
    Append items to existing file
    """
    f = open(filename, 'a')
    print("Type 'exit()' on a new line to save entry and exit")
    flag = 'exit()'
    while True:
        lineInput = str(input(">>> "))
        if lineInput == flag:
            break
        else:
            f.write(lineInput + "\n")

    f.close()
    print("File saved")


def write_line(filename):
    """
    overwrite a specific line
    """
    with open(filename, 'r') as file:
        f = file.readlines()
        count = 1
        for line in f:
            print(str(count) + ". " + line)
            count += 1

    with open(filename, 'w') as file:
        while True:
            try:
                lineNum = int(
                    input("Which line do you want to replace? \n>>> "))
                break
            except ValueError:
                lineNum = int(print("Enter a line number \n>>>"))

        for i, line in enumerate(f, 1):
            if i == lineNum:
                file.writelines(input("Enter text \n>>>") + "\n")
            else:
                file.writelines(line)


filename = str(input("Enter the name of file you want to access \n>>> "))
while True:
    file_checker(filename)
    if file_checker(filename) == False:
        prompt = str(input(
            """No such file, would you like to create a new one to continue? (y/n) \n>>> """))
        prompt = prompt.lower()
        if prompt == 'y':
            write_file(filename)
    else:
        action = str(input("""
    Which action do you want to perform on the file? \n

    A) Read the file \n
    B) Write (Writes a new file or replaces content of an existing one) \n
    C) Append the file (Adds to an already existing file) \n
    D) Replace a single line \n>>> """))

        action = action.lower()
        if action == 'a':
            read_file(filename)
        elif action == 'b':
            write_file(filename)
        elif action == 'c':
            append_file(filename)
        elif action == 'd':
            write_line(filename)

    action = str(
        input("Do you want to perform another action on the file? (y/n)\n>>>"))
    action = action.lower()
    if action == 'y':
        continue
    else:
        break
