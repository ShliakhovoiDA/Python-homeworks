import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED + 'Красный текст')
print(Back.BLUE + 'Синий фон')
print(Style.RESET_ALL)
print('Снова обычный текст')