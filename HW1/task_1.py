"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping 
   будет проверяться доступность сетевых узлов. Аргументом функции 
   является список, в котором каждый сетевой узел должен быть представлен 
   именем хоста или ip-адресом. В функции необходимо перебирать ip-адреса 
   и проверять их доступность с выводом соответствующего сообщения 
   («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла 
   должен создаваться с помощью функции ip_address(). 
   (Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! 
   Для уменьшения времени работы скрипта при проверке нескольких ip-адресов, 
   решение необходимо выполнить с помощью потоков)
"""
from concurrent.futures import thread
import platform
from ipaddress import ip_address
from subprocess import Popen, PIPE
from threading import Thread


def run_ping(addr, args, available=[], not_available=[], result={}):
    work = Popen(args, shell=False,  stdout=PIPE, stderr=PIPE)
    work.wait()

    if work.returncode == 0:
        available.append(str(addr))
        result['Доступные узлы'] = available
    else:
        not_available.append(str(addr))
        result['Недоступные узлы'] = not_available


def host_ping(address: list, timeout=1, requests=1):
    result = dict()
    available = list()
    not_available = list()
    threading_lst = list()
    for addr in address:
        try:
            addr = ip_address(addr)
        except ValueError:
            pass
        # command = f'ping {addr} -w {timeout} -n {requests}'
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        args = ['ping', param, f'{requests}', '-W', f'{timeout}', f'{addr}']
        thr = Thread(target=run_ping, args=(
            addr, args, available, not_available, result))
        thr.start()
        threading_lst.append(thr)

    for thr in threading_lst:
        thr.join()

    try:
        if result['Доступные узлы']:
            pass
    except KeyError:
        result['Доступные узлы'] = []

    try:
        if result['Недоступные узлы']:
            pass
    except KeyError:
        result['Недоступные узлы'] = []

    return result


if __name__ == '__main__':
    address = ['192.168.0.1', '192.168.110.51',
               'mail.ru', 'yandex.ru', 'vk.com']
    result = host_ping(address)
    print(result)
