with open("text_11.txt", "r", encoding="utf-8") as file:
    print(f"Рассматриваемый файл: {file.name}")
    my_line = file.readlines()
    for index, value in enumerate(my_line, 1):
        words_count = len(value.split())
        print(f"В {index} строке {words_count} слов и {len(value)} символов")
