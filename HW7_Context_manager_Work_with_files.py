import pickle
import openpyxl

# Task 1
d = {}
with open('task1.txt', 'r') as file:
    length = len(file.readlines())
    file.seek(0)
    for i in range(int(length / 2)):
        key = file.readline().replace('\n', '')
        value = file.readline().replace('\n', '')
        d[key] = value
print(d)

# Task 1_2
with open('task1_2.txt', 'w') as file2:
    for val in d.values():
        file2.write(f'{val} ')

# Task 2
with open('task2', 'rb') as task2:
    print(task2.read())
    task2.seek(0)
    lst = pickle.load(task2)
    print(lst)
    print(sum(lst) / len(lst))


# Task 3
class OpenExcel:
    def __init__(self, file_name, readonly=True):
        self._obj = openpyxl.open(file_name, readonly)

    def __enter__(self):
        return self._obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._obj.close()
