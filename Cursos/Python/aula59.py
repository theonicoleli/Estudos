lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome': 'Luiz'},
]

for item in lista:

    if isinstance(item, set):
        print('SET')
        print(item)

    elif isinstance(item, dict):
        print('DICT')
        print(item)

    elif isinstance(item, tuple):
        print('TUPLE')
        print(item)

    elif isinstance(item, bool):
        print('BOOL')
        print(item)
    
    elif isinstance(item, str):
        print('STR')
        print(item)
    
    elif isinstance(item, (int, float)):
        print('INT or FLOAT')
        print(item)