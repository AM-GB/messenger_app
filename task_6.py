"""
6.  Создать текстовый файл test_file.txt, заполнить его тремя строками:
    «сетевое программирование», «сокет», «декоратор». Далее забыть о том, 
    что мы сами только что создали этот файл и исходить из того, 
    что перед нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК 
    вне зависимости от того, в какой кодировке он был создан.
"""

import chardet


def encoding_definition_file(file):
    with open(file, "rb") as f:
        return chardet.detect(f.read())['encoding']


def print_file(file, encoding):
    with open(file, "r", encoding=encoding) as f:
        print(f.read())


if __name__ == '__main__':
    encoding = encoding_definition_file('test_file.txt')
    print(encoding)

    print_file('test_file.txt', encoding)
