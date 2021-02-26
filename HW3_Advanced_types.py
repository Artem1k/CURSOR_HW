# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
List = [int_a, str_b, set_c, lst_d, dict_e]
print("1.", id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print("2.", id(lst_d))

# 3. Define the type of each object from step 1.
print("3. ", end="")
for i in List:
    print(f'{i} is {type(i)}')

# 4*. Check the type of the objects by using isinstance.
print("4. ", end="")
for i in List:
    print(f'Is {i} list: {isinstance(i, list)}')

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print('5. Anna has {} apples and {} peaches.'.format(10, 8))

# 6. By passing index numbers into the curly braces.
print('6. Anna has {1} apples and {0} peaches.'.format(8, 10))

# 7. By using keyword arguments into the curly braces.
print('7. Anna has {apples} apples and {peaches} peaches.'.format(apples=10, peaches=8))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('8. Anna has {1:4} apples and {0:3} peaches.'.format(8, 10))

# 9. With f-strings and variables
apples, peaches = 10, 8
print(f'9. Anna has {apples} apples and {peaches} peaches.')

# 10. With % operator
print('10. Anna has %d apples and %d peaches.' % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
fruits_dict = {"apples": 10, "peaches": 8}
print('11. Anna has %(apples)d apples and %(peaches)d peaches.' % fruits_dict)

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
#
# 12. Convert (1) to list comprehension
List = [i ** 2 if i % 2 == 1 else i ** 4 for i in range(10)]
print("12.", List)

# 13. Convert (2) to regular for with if-else
List.clear()
for i in range(10):
    if i % 2 == 0:
        List.append(i // 2)
    else:
        List.append(i * 10)
print("13.", List)

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

# 15*. Convert (4) to dict comprehension.
d = {i: i ** 2 if i % 2 == 1 else i // 0.5 for i in range(1, 11)}
print("15.", d)

# 16. Convert (5) to regular for with if.
d.clear()
for i in range(10):
    if i ** 3 % 4 == 0:
        d[i] = i ** 3
print("16.", d)

# 17*. Convert (6) to regular for with if-else.
# d.clear()
for i in range(10):
    if i ** 3 % 4 == 0:
        d[i] = i ** 3
    else:
        d[i] = i
print("17.", d)

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
#
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print("18.", foo(10, 5), foo(5, 10))


# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print("19.", foo(1, 2, 3))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print("20.", sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print("21.", sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("22.", list(map(lambda x: x * 2, lst_to_sort)))

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print("23.", list(map(lambda x, y: x ** y, list_A, list_B)))

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce

print("24.", reduce(lambda x, y: x + y, lst_to_sort))

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("25.", list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print("26.", list(filter(lambda x: x < 0, b)))

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print("27.", list(filter(lambda x: x in list_1, list_2)))
