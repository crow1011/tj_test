# -*- coding: utf-8 -*-
import os
import csv
import argparse
from statistics import mean

debug = False


def search_reports(search_path, extension):
    res = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(extension):
                res.append(os.path.join(root, file))
    return res


def get_rows(file_path):
    res = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            res.append(row)
    return res


def main(user_search_path, user_extension, user_Name):
    # Готовим словарь для результатов
    result = {
        'open': [],
        'high': [],
        'low': [],
        'close': []
    }
    # собираем пути до файлов в массив
    reports = search_reports(user_search_path, user_extension)
    # проходимся циклом по массиву чтобы обработать каждый файл
    for report in reports:
        # извлекаем содержимое файла
        rows = get_rows(report)
        # обрабатываем содержимое файла по строкам
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
