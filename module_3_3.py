def print_params (a = 1, b = 'String', c = True):
    print(a, b, c)

print('Функция с параметрами по умолчанию:')
print_params(25, [1, 2, 3], 4)
print()

print('Распаковка параметров:')
values_list = [False, 'str', 2]
values_dict = {'a': None, 'b': 10, 'c': 'elif'}
print_params(*values_list)
print_params(**values_dict)
print()

print('Распаковка + отдельные параметры:')
values_list_2 = ['строка', 77.99]
print_params(*values_list_2, 42)

