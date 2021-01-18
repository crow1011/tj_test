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
print(reports)

tst = reports[0]


def get_data(file_path):
    res = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            res.append(row)
    return res

data = []

for report in reports:
    rows = get_data(report)
    for row in rows:
        if row['Name'] == user_Name:
            data.append(row)

results = {
    'open': [],
    'high': [],
    'low': [],
    'close': []
}
for row in data:
    results['open'].append(float(row['open']))
    results['high'].append(float(row['high']))
    results['low'].append(float(row['low']))
    results['close'].append(float(row['close']))

result = {}
for key, val in results.items():
    result[key] = round(mean(results[key]), 3)

print(result)
