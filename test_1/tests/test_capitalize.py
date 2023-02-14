from capitalize import capitalize

assert capitalize('hello') == 'Hello'
# if capitalize('hello') != 'Hello':
#     raise Exception('Функция работает неверно!')

assert capitalize('') == ''
# if capitalize('') != '':
#     raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
