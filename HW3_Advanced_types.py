# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
List = [int_a, str_b, set_c, lst_d, dict_e]
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# 3. Define the type of each object from step 1.
for i in List:
    print(f'{i} is {type(i)}')

# 4*. Check the type of the objects by using isinstance.
for i in List:
    print(f'Is {i} list: {isinstance(i, list)}')

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}

print('Anna has {} apples and {} peaches.'.format(10, 8))

# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches.'.format(8, 10))

# 7. By using keyword arguments into the curly braces.
print('Anna has {apples} apples and {peaches} peaches.'.format(apples=10, peaches=8))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {1:4} apples and {0:3} peaches.'.format(8, 10))

# 9. With f-strings and variables
apples, peaches = 10, 8
print(f'Anna has {apples} apples and {peaches} peaches.')

# 10. With % operator
print('Anna has %d apples and %d peaches.' % (apples, peaches))
