# -*- coding: utf-8 -*-
import unittest
from main import search_reports, get_rows, main
from collections import OrderedDict
import sys

test_data_path = 'data/'


class ColorPrint:

    def print_fail(self, message, end='\n'):
        sys.stderr.write('\x1b[1;31m' + str(message).strip() + '\x1b[0m' + end)

    def print_pass(self, message, end='\n'):
        sys.stdout.write('\x1b[1;32m' + str(message).strip() + '\x1b[0m' + end)

    def print_warn(self, message, end='\n'):
        sys.stderr.write('\x1b[1;33m' + str(message).strip() + '\x1b[0m' + end)

    def print_info(self, message, end='\n'):
        sys.stdout.write('\x1b[1;34m' + str(message).strip() + '\x1b[0m' + end)

    def print_bold(self, message, end='\n'):
        sys.stdout.write('\x1b[1;37m' + str(message).strip() + '\x1b[0m' + end)


class TestFull(unittest.TestCase, ColorPrint):
    def setUp(self):
        self.user_search_path = 'data'
        self.user_extension = '.csv'
        self.user_Name = 'AAPL'
        self.test_reports_list = ['data/foo.csv',
                                  'data/Starhopper/Boca_Chica/25_07_2019/logs.csv',
                                  'data/BFR_logs/raptor.csv']
        self.test_reports_data = {
            'data/foo.csv': [OrderedDict([('date', '2013-02-08'),
                                          ('open', '67.7142'),
                                          ('high', '68.4014'),
                                          ('low', '66.8928'),
                                          ('close', '67.8542'),
                                          ('volume', '158168416'),
                                          ('Name', 'AAPL')])],
            'data/Starhopper/Boca_Chica/25_07_2019/logs.csv': [OrderedDict([('date', '2013-02-12'),
                                                                            ('open', '68.5014'),
                                                                            ('high', '68.9114'),
                                                                            ('low', '66.8205'),
                                                                            ('close', '66.8428'),
                                                                            ('volume', '151829363'),
                                                                            ('Name', 'AAPL')])],

            'data/BFR_logs/raptor.csv': [OrderedDict([('date', '2013-02-11'),
                                                      ('open', '68.0714'),
                                                      ('high', '69.2771'),
                                                      ('low', '67.6071'),
                                                      ('close', '68.5614'),
                                                      ('volume', '129029425'),
                                                      ('Name', 'AAPL')])]

        }
        self.test_result = {'open': 68.096, 'high': 68.863, 'low': 67.107, 'close': 67.753}

    def test_get_rows(self):
        self.print_info('Сравниваем результат функции get_rows с заранее определенным списком содержимого файлов')
        for report in self.test_reports_list:
            self.print_warn(report)
            self.assertEqual(self.test_reports_data[report], get_rows(report))
            self.print_pass('OK')
        self.print_pass('test_get_rows: OK')

    def test_search_reports(self):
        self.print_info('Сравниваем результат функции search_reports с заранее определенным списком путей до файлов')
        self.assertEqual(sorted(search_reports(test_data_path, '.csv')), sorted(self.test_reports_list))
        self.print_pass('test_search_reports: OK')

    def test_main_result(self):
        self.print_info('Сравниваем результат выполнения функции main с заранее определенным test_result')
        self.assertEqual(main(self.user_search_path, self.user_extension, self.user_Name), self.test_result)
        self.print_pass('test_main_result: OK')


if __name__ == '__main__':
    unittest.main()
