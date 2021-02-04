# -*- coding: utf-8 -*-
import os
import csv
import argparse
from statistics import mean
import timeit
import tracemalloc
debug = True
tracemalloc.start()

def search_reports(search_path, extension):
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(extension):
                yield open(os.path.join(root, file))


def get_rows(files):
    for fname in files:
        reader = csv.DictReader(fname, delimiter=',')
        for row in reader:
            yield row


def main(user_search_path, user_extension, user_Name):
    # Готовим словарь для результатов
    result = {
        'open': [],
        'high': [],
        'low': [],
        'close': []
    }
    # создаем генератор с путями до файлов
    reports = search_reports(user_search_path, user_extension)
    # создаем генератор со строками из файлов
    rows = get_rows(reports)
    for row in rows: 
        # если поле Name в строке соотвествует параметру пользователя,\
        # добавляем значения в словарь для результатов
        if row['Name'] == user_Name:
            result['open'].append(float(row['open']))
            result['high'].append(float(row['high']))
            result['low'].append(float(row['low']))
            result['close'].append(float(row['close']))

    # приводим значения в словаре для результатов от массива значений к среднему
    # округляем среднее до 3х знаков после точки
    for key, val in result.items():
        result[key] = round(mean(result[key]), 3)
    return result


if __name__ == '__main__':
    if debug:
        # /dev
        user_search_path = 'data'
        user_extension = '.csv'
        user_Name = 'AAPL'
        # \dev
    else:
        parser = argparse.ArgumentParser(description='Find Name in data.')
        parser.add_argument('data_dir', type=str, help='Set path to csv data dir')
        parser.add_argument('search_Name', type=str, help='Set name for search in data')
        args = parser.parse_args()
        user_extension = '.csv'
        user_search_path = args.data_dir
        user_Name = args.search_Name
    output = main(user_search_path, user_extension, user_Name)
    print(output)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()