import argparse
import csv

'''exp; required: false; default: min(exp)
current_job_exp; required: false; default: max(current_job_exp)
sex; required: false
city; required: false
position; required: false
age; required: false
path_to_source_files; required: true;
destination_path; required: false; default: .
destination_filename; required: false; default: f"2020_june_mini.csv".'''
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument('--exp', '-e', required=False, default='min(exp)')
parser.add_argument('--current_job_exp', '-j', required=False, default='max(current_job_exp)')
parser.add_argument('--sex', '-s', required=False)
parser.add_argument('--city', '-c', required=False)
parser.add_argument('--position', '-p', required=False)
parser.add_argument('--age', '-a', required=False)
parser.add_argument('--path_to_source_files', '-t', required=True)
parser.add_argument('--destination_path', '-P', required=False, default='.')
parser.add_argument('--destination_filename', '-F', required=False, default=f"2020_june_mini.csv")
args = parser.parse_args()
'''The script should read the .csv file and get the information based on your input and generate a new .csv
file with that info

Example of input:
-exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...'''
with open(args.path_to_source_files, 'r') as f:
    reader = csv.DictReader(f)
    if args.exp == 'min(exp)':
        lst_exp = []
        for row in reader:
            lst_exp.append(float(row['exp']))
        args.exp = min(lst_exp)
        del lst_exp
        f.seek(0)
    if args.current_job_exp == 'max(current_job_exp)':
        lst_current_job_exp = []
        for row in reader:
            lst_current_job_exp.append(float(row['current_job_exp']))
        args.current_job_exp = max(lst_current_job_exp)
        del lst_current_job_exp
        f.seek(0)
    with open('new_file.csv', 'w') as new_f:
        # field_names = list(map(lambda x: x.replace('\n', '')[1:-1], next(f).split(',')))
        # writer = csv.DictWriter(new_f, fieldnames=field_names)
        # writer.writeheader()
        fieldnames = ["N", "Город", "Зарплата.в.месяц", "Изменение.зарплаты.за.12.месяцев", "Должность", "exp",
                      "current_job_exp", "Язык.программирования", "Специализация", "Возраст", "Пол", "Образование",
                      "Университет", "Еще.студент", "Уровень.английского", "Размер.компании", "Тип.компании",
                      "Предметная.область"]
        writer = csv.DictWriter(new_f, fieldnames=fieldnames)
        next(f)
        for row in reader:
            if args.position:
                if row['Должность'] != args.position:
                    continue
            if args.exp:
                if float(row['exp']) != float(args.exp):
                    continue
            if args.current_job_exp:
                if float(row['current_job_exp']) != float(args.current_job_exp):
                    continue
            if args.age:
                if float(row["Возраст"]) != float(args.age):
                    continue
            if args.sex:
                if row["Пол"] != args.sex:
                    continue
            if args.city:
                if row['Город'] != args.city:
                    continue
            writer.writerow(row)
'''python3 ~/PycharmProjects/CURSOR_HW/HW12_argument_parser_1.py --exp 10 --path_to_source_files 
~/PycharmProjects/CURSOR_HW/2020_june_mini.csv
Output in new_file.csv
'''
