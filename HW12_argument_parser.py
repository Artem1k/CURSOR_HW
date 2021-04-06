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
with open(args.path_to_source_files, 'r')as f:
    reader = csv.DictReader(f)
for row in reader:
    if row['Должность'] == args.position and row['exp'] == args.exp and row['current_job_exp'] == args.current_job_exp \
            and row['age'] == args.age and row['sex'] == args.sex and row[''] and row['Город'] == args.city:
        print(row.keys())
