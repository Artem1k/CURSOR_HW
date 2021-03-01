# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
List = [int_a, str_b, set_c, lst_d, dict_e]
print("1.", id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))
# Output: 1. 9786624 140305361505392 140305361479936 140305361866304 140305362342400

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print("2.", id(lst_d))
# Output: 2. 140305361866304

# 3. Define the type of each object from step 1.
print("3. ", end="")
for i in List:
    print(f'{i} is {type(i)}')
# Output: 3. 55 is <class 'int'>
# cursor is <class 'str'>
# {1, 2, 3} is <class 'set'>
# [1, 2, 3, 4, 5] is <class 'list'>
# {'a': 1, 'b': 2, 'c': 3} is <class 'dict'>

# 4*. Check the type of the objects by using isinstance.
print("4. ", end="")
for i in List:
    print(f'Is {i} list: {isinstance(i, list)}')
# Output: 4. Is 55 list: False
# Is cursor list: False
# Is {1, 2, 3} list: False
# Is [1, 2, 3, 4, 5] list: True
# Is {'a': 1, 'b': 2, 'c': 3} list: False

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print('5. Anna has {} apples and {} peaches.'.format(10, 8))
# Output: 5. Anna has 10 apples and 8 peaches.

# 6. By passing index numbers into the curly braces.
print('6. Anna has {1} apples and {0} peaches.'.format(8, 10))
# Output: 6. Anna has 10 apples and 8 peaches.

# 7. By using keyword arguments into the curly braces.
print('7. Anna has {apples} apples and {peaches} peaches.'.format(apples=10, peaches=8))
# Output: 7. Anna has 10 apples and 8 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('8. Anna has {1:4} apples and {0:3} peaches.'.format(8, 10))
# Output: 8. Anna has   10 apples and   8 peaches.

# 9. With f-strings and variables
apples, peaches = 10, 8
print(f'9. Anna has {apples} apples and {peaches} peaches.')
# Output: 9. Anna has 10 apples and 8 peaches.

# 10. With % operator
print('10. Anna has %d apples and %d peaches.' % (apples, peaches))
# Output: 10. Anna has 10 apples and 8 peaches.

# 11*. With variable substitutions by name (hint: by using dict)
fruits_dict = {"apples": 10, "peaches": 8}
print('11. Anna has %(apples)d apples and %(peaches)d peaches.' % fruits_dict)
# Output: 11. Anna has 10 apples and 8 peaches.

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
List = [i ** 2 if i % 2 == 1 else i ** 4 for i in range(10)]
print("12.", List)
# Output: 12. [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
List.clear()
for i in range(10):
    List.append(i // 2) if i % 2 == 0 else List.append(i * 10)
print("13.", List)
# Output: 13. [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# 14. Convert (3) to dict comprehension.
d = {i: i ** 2 for i in range(1, 11) if i % 2 == 1}
print("14.", d)
# Output: 14. {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
d = {i: i ** 2 if i % 2 == 1 else i // 0.5 for i in range(1, 11)}
print("15.", d)
# Output: 15. {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
d.clear()
for i in range(10):
    if i ** 3 % 4 == 0:
        d[i] = i ** 3
print("16.", d)
# Output: 16. {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
# d.clear()
d = {}
for i in range(10):
    d[i] = i ** 3 if (i ** 3) % 4 == 0 else i
print("17.", d)
# Output: 17. {0: 0, 2: 8, 4: 64, 6: 216, 8: 512, 1: 1, 3: 3, 5: 5, 7: 7, 9: 9}

# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print("18.", foo(10, 5), foo(5, 10))


# Output: 18. 5 5

# 19*. Convert (8) to regular function
def foo(x, y, z):
    return z if y < x and x > z else y


print("19.", foo(1, 2, 3))
# Output: 19. 2

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print("20.", sorted(lst_to_sort))
# Output: 20. [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
print("21.", sorted(lst_to_sort, reverse=True))
# Output: 21. [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("22.", list(map(lambda x: x * 2, lst_to_sort)))
# Output: 22. [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print("23.", list(map(lambda x, y: x ** y, list_A, list_B)))
# Output: 23. [32, 729, 16384]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce

print("24.", reduce(lambda x, y: x + y, lst_to_sort))
# Output: 24. 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("25.", list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))
# Output: 25. [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print("26.", list(filter(lambda x: x < 0, b)))
# Output: 26. [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print("27.", list(filter(lambda x: x in list_1, list_2)))
# Output: 27. [2, 3, 5, 7]
