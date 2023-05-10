import random

palavras = ['abajur', 'perfume', 'aviao', 'aeronave', 'carros', 'pneu', 'aeroporto', 'viagem', 'lua', 'sol']

def palavra_aleatoria():
    return random.choice(palavras)

letras_acertadas = ''
numero_tentativas = 0

while True:
    palavra_secreta = palavra_aleatoria()
    asterisco = ''
    for letras in palavra_secreta:
        letras = '*'
        asterisco += letras
    print(asterisco)
    while 1==1:
        palavra_formada = ''
        letra_digitada = input('Digite uma letra: ')
        numero_tentativas += 1

        if len(letra_digitada) > 1:
            print('Digite apenas uma letra!')
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        else:
            if not letra_digitada in palavra_secreta:
                continue

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            print('='*100)
            numero_tentativas = 0
            letras_acertadas = ''
            break