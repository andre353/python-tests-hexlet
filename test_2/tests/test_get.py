

from get_function import get

if get({"hello": "world"}, "hello") != 'world':
    raise Exception('Функция работает неверно!')

if get({}, "hello", "kitty") != 'kitty':
    raise Exception('Функция работает неверно!')

if get({"hello": "world"}, "hello", "kitty") != 'world':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')

# Solution sample
# BEGIN
# if get({"key": "value"}, "key") != "value":
#     raise Exception('Boom!')

# if get({}, "key", "default") != "default":
#     raise Exception('Boom!')

# if get({"key": "value"}, "key", "default") != "value":
#     raise Exception('Boom!')
# END