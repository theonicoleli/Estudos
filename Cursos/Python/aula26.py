import random
import os

numbers = [0,1,2,3,4,5,6,7,8,9]
other_numbers = [1,2,3,4,5,6,7,8,9]

while True:
    print('Digite os números para a MEGASENA')

    def quantidade_vezes():
        return random.choice(other_numbers)
    
    vezes = quantidade_vezes()

    def valor_vencedor():
        lista = []
        for number in range(vezes):
            valor = random.choice(numbers)
            lista.append(valor)
        return lista

    valor_vencendo = valor_vencedor()
    valor = ''.join(str(valores) for valores in valor_vencendo)
    valor = int(valor)

    def selecao_aleatoria():
        number = []
        for numero in range(6):
            aleatorio = random.choice(numbers)
            number.append(aleatorio)
        return number

    numeros_random = selecao_aleatoria()
    numeros_str =''.join(str(num) for num in numeros_random)
    numeros_str = int(numeros_str)

    digitos = []
    acertos = []
    vezes = 6

    while vezes>0:
        digito = input('Digite um número: ')
        vezes -= 1
        if digito.isdigit():
            digito = int(digito)
            digitos.append(digito)
            if digito in numeros_random:
                if digito in acertos:
                    if numeros_random.count(digito) > acertos.count(digito):
                        acertos.append(digito)
                else:
                    acertos.append(digito)
                    continue
        else:
            print('Digite um número válido!')
            vezes += 1
    if digitos == numeros_random:
        os.system('cls')
        print(f'Parabéns você acertou todos os números {numeros_str}, você ganhou: {valor} R$')
        print('='*100)
    elif acertos:
        os.system('cls')
        premio_por_acerto = valor * 0.16667 * len(acertos)
        print(f'Parabéns! Você acertou {len(acertos)} número(s) {acertos}.\nO valor correto era: {numeros_str}\nO prêmio total era de: {valor} R$')
        print(f'Você ganhou: {round(premio_por_acerto, 2)} R$')
        print('='*100)
    else:
        os.system('cls')
        print(f'Infelizmente você não ganhou a aposta! O valor correto era {numeros_str}')
        print('='*100)