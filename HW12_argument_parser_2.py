'''
source_file_path; required: true;
start_salary; required: false; help: starting point of salary;
end_salary; required: false; help: the max point of salary;
position; required: false; help: position role
age; required: false; help: Age of person
language; required: false; help; Programming language

Based on this info generate a new report of average salary.'''

import argparse
import csv

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument('--source_file_path', '-f', required=True)
parser.add_argument('--start_salary', '-s', required=False, help='starting point of salary')
parser.add_argument('--end_salary', '-e', required=False, help='the max point of salary;')
parser.add_argument('--position', '-p', required=False, help='position role')
parser.add_argument('--age', '-a', required=False, help='Age of person')
parser.add_argument('--language', '-l', required=False, help='Programming language')
args = parser.parse_args()

with open(args.source_file_path, 'r') as f:
    reader = csv.DictReader(f)
    price_list = []
    for row in reader:
        if args.position:
            if row['Должность'] != args.position:
                continue
        if args.age:
            if int(row['Возраст']) != args.age:
                continue
        if args.start_salary:
            if float(row['Зарплата.в.месяц']) < float(args.start_salary):
                continue
        if args.end_salary:
            if float(row['Зарплата.в.месяц']) > float(args.end_salary):
                continue
        price_list.append(float(row['Зарплата.в.месяц']))
print(round(sum(price_list) / len(price_list), 2))
'''
python3 ~/PycharmProjects/CURSOR_HW/HW12_argument_parser_2.py -f ~/PycharmProjects/CURSOR_HW/2020_june_mini.csv -s 12000 
14472.22
python3 ~/PycharmProjects/CURSOR_HW/HW12_argument_parser_2.py -f ~/PycharmProjects/CURSOR_HW/2020_june_mini.csv -s 12000
 -p 'Senior Software Engineer'
14666.67
'''
