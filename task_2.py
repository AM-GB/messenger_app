"""
2.  Каждое из слов «class», «function», «method» записать в байтовом типе. 
    Сделать это необходимо в автоматическом, а не ручном режиме, 
    с помощью добавления литеры b к текстовому значению, 
    (т.е. ни в коем случае не используя методы encode, decode или функцию bytes)
    и определить тип, содержимое и длину соответствующих переменных.
"""

from config import WORD_TASK2


def conversion_bytes(lst):
    for i in range(len(lst)):
        lst[i] = eval(f"b'{lst[i]}'")


def print_list(lst=[]):
    for param in lst:
        print(param)


def print_type(lst=[]):
    for param in lst:
        print(type(param))


def print_len(lst=[]):
    for param in lst:
        print(len(param))


if __name__ == '__main__':
    conversion_bytes(WORD_TASK2)
    print_type(WORD_TASK2)
    print_list(WORD_TASK2)
    print_len(WORD_TASK2)
