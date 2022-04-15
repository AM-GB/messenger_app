"""
1.  Каждое из слов «разработка», «сокет», «декоратор» представить в строковом 
    формате и проверить тип и содержание соответствующих переменных. 
    Затем с помощью онлайн-конвертера преобразовать строковые представление 
    в формат Unicode и также проверить тип и содержимое переменных.
"""

from config import WORD_TASK1, WORD_UNICODE_TASK1


def type_check_list(lst=[]):
    for param in lst:
        print(type(param))


def print_list(lst=[]):
    for param in lst:
        print(param)


if __name__ == '__main__':
    type_check_list(WORD_TASK1)

    type_check_list(WORD_UNICODE_TASK1)
    print_list(WORD_UNICODE_TASK1)
