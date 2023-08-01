# Exercícios com o conhecimento de decoradores

import time

def creatingContent(func):
    def contentIntern(*args, **kwargs):
        print('Checking the content...')
        time.sleep(3)
        for letter in args:
            verifyContent(letter)
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        print('Verified content!')
        print(f'{resultado}')
        print(f'Time taken: {end_time - start_time:.4f} seconds')
        return resultado
    return contentIntern

@creatingContent
def countingletter(string):
    quanty = len(string)
    return quanty


def verifyContent(param):
    if not isinstance(param, str):
        raise TypeError('Please, enter a valid parameter')
    

while True:
    name = input('Digite um nome: ')
    if isinstance(name, str):
        string = countingletter(name)
        print(string)
    else:
        print('Digite um nome!')