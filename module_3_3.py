def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
c = [1, 2, 3]
print_params(1, '25', True)
print_params(1, '25', c)

values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 =[3.14, 'Str']
print_params(*values_list_2, 42)