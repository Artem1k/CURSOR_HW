d = {}
with open('task1.txt', 'r') as file:
    length = len(file.readlines())
    file.seek(0)
    for i in range(length):
        key = file.readline()[:-1]
        value = file.readline()[:-1]
        d[key] = value
print(d)
with open('task1_2.txt', 'w') as file2:
    for val in d.values():
        file2.write(f'{val} ')
