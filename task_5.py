"""
5.  Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
    преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import chardet
import subprocess
import platform

from config import SITE_TASK5


def print_ping_site_list(lst):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    for site in lst:
        print('\n' + '-'*20 + site + '-'*20)

        args = ['ping', param, '3', site]
        process = subprocess.Popen(args, stdout=subprocess.PIPE)

        for line in process.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8').replace('\n', ''))


if __name__ == '__main__':
    print_ping_site_list(SITE_TASK5)
