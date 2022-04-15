"""
4.  Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
    из строкового представления в байтовое и выполнить обратное преобразование 
    (используя методы encode и decode).
"""

from config import WORD_TASK4


def print_list(lst=[]):
    for param in lst:
        print(param)


def print_encode_list(lst=[]):
    for i in range(len(lst)):
        lst[i] = lst[i].encode(encoding="utf-8")
        print(lst[i])


def print_decode_list(lst=[]):
    for i in range(len(lst)):
        lst[i] = lst[i].decode("utf-8")
        print(lst[i])


if __name__ == '__main__':
    print_list(WORD_TASK4)
    print_encode_list(WORD_TASK4)
    print_decode_list(WORD_TASK4)
