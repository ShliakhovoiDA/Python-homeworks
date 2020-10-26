dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_5ex4.txt", "w", encoding="utf-8") as new:
    with open("text_numbers.txt", "r", encoding="utf-8") as my_file:
        new.writelines([line.replace(line.split()[0], dictionary.get(line.split()[0])) for line in my_file])
