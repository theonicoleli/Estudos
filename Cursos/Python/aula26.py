import random

numbers = [0,1,2,3,4,5,6,7,8,9]

while True:
    print('Digite os números para a MEGASENA')
    def selecao_aleatoria():
        number = []
        for numero in range(6):
            aleatorio = random.choice(numbers)
            number.append(aleatorio)
        return number

    numeros_random = selecao_aleatoria()
    numeros_str = ''.join(str(num) for num in numeros_random)

    digitos = []

    for n in range(6):
        digito = int(input('Digite um número: '))
        digitos.append(digito)
    if digitos == numeros_random:
        print(f'Parabéns você acertou todos os números {numeros_str}')
        print('='*100)
    else:
        print(f'Infelizmente você não ganhou a aposta! O valor correto era {numeros_str}')
        print('='*100)