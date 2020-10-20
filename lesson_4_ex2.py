my_list = [10, 1, 1, 1, 44, 54, 56, 1, 1, 25, 30, 45, 50, 44, 56, 57, 89, 43]
print(f'Сравните старый список: {my_list} из {len(my_list)} элементов')
new_list = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i - 1]]
print(f'С новым списком: {new_list} из {len(new_list)} элементов.')
