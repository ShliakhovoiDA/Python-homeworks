with open("text_11.txt", "w", encoding="utf-8") as file:
    while True:
        string = input("Введите все, что угодно, и получите строки в файле из своей абракадабры. \n"
                       "Если Вам надоело, ничего не вводите и нажмите Enter: ")
        if string == '' or string == " ":
            break
        file.write(string + '\n')