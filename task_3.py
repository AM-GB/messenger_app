"""
3.  Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. 
    Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

from config import WORD_TASK3


def conversion_bytes(word):
    return eval(f"b'{word}'")


if __name__ == '__main__':
    for word in WORD_TASK3:
        try:
            print(conversion_bytes(word))
        except SyntaxError:
            print(f"невозможно записать в байтовом типе '{word}'")
