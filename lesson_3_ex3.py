# убрать минимум, и получится все круто

def my_func(n1, n2, n3):
    my_numbers = [n1, n2, n3]
    try:
        my_numbers.remove(min(my_numbers))
        return sum(my_numbers)
    except ValueError:
        return 'Введите числа!'
    except TypeError:
        return 'Введите числа!'


print(my_func(n1=int(input('1-st: ')), n2=int(input('2-nd: ')), n3=int(input('3-rd: '))))

# при попытке ввода буквы выводит ValueError несмотря на то, что она записана в исключения