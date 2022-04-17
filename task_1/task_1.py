"""
1.  Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных 
    данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. 
    Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и 
считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений 
извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для 
хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также 
оформить в виде списка и поместить в файл main_data (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать 
получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re
import os


SEARCH_LIST = [
    'Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы'
]


def get_data(search_list):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = []
    main_data.append(search_list)

    file_list = os.listdir(os.getcwd())

    for file in file_list:
        if re.match(f'info', file):
            with open(file, encoding='cp1251') as file:
                string = file.read()

                os_prod_list.append(re.findall(
                    search_list[0] + r".{1,}", string)[0].split('  ')[-1].strip())
                os_name_list.append(re.findall(
                    search_list[1] + r".{1,}", string)[0].split('  ')[-1].strip())
                os_code_list.append(re.findall(
                    search_list[2] + r".{1,}", string)[0].split('  ')[-1].strip())
                os_type_list.append(re.findall(
                    search_list[3] + r".{1,}", string)[0].split('  ')[-1].strip())

            main_data.append([
                os_prod_list[-1],
                os_name_list[-1],
                os_code_list[-1],
                os_type_list[-1],
            ])

    return main_data


def write_to_csv(file):
    with open(file, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data(SEARCH_LIST):
            f_n_writer.writerow(row)


if __name__ == "__main__":
    write_to_csv('result.csv')
