import os
import csv
from statistics import mean

# dev
user_search_path = 'data'
user_extension = '.csv'
user_Name = 'AAPL'


# dev


def search_reports(search_path, extension):
    res = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(extension):
                res.append(os.path.join(root, file))
    return res


reports = search_reports(user_search_path, user_extension)


def get_rows(file_path):
    res = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            res.append(row)
    return res


def main():
    result = {
        'open': [],
        'high': [],
        'low': [],
        'close': []
    }

    for report in reports:
        rows = get_rows(report)
        for row in rows:
            if row['Name'] == user_Name:
                result['open'].append(float(row['open']))
                result['high'].append(float(row['high']))
                result['low'].append(float(row['low']))
                result['close'].append(float(row['close']))

    for key, val in result.items():
        result[key] = round(mean(result[key]), 3)
    return result


if __name__ == '__main__':
    output = main()
    print(output)
