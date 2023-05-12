import random
import os

palavras = ['ábaco', 'abajur', 'abre-latas', 'açucareiro', 'agogô', 'agulha', 'alaúde', 'alfinete', 'alforje', 'algema', 'alicate', 'almofada', 'almofariz', 'ampulheta', 'âncora', 'anel', 'antena', 'anzol', 'apagador', 'apito', 'apontador', 'aquecedor', 'arado', 'arco', 'armadura', 'aro', 'arpão', 'aspirador', 'astrolábio', 'azulejo', 'bacia', 'balaio', 'balança', 'balde', 'bambolê', 'banco', 'bandeira', 'bandolim', 'batuta', 'bazuca', 'bengala', 'berço', 'berimbau', 'bicicleta', 'bidê', 'bigorna', 'binóculo', 'biombo', 'biruta', 'bisturi', 'boia', 'bola', 'boneca', 'borracha', 'botão', 'botija', 'brinco', 'bule', 'bumerangue', 'bússola', 'cabide', 'cadeado', 'cadeira', 'caderno', 'cajado', 'calculadora', 'cálice', 'campainha', 'candeeiro', 'candelabro', 'caneca', 'caneta', 'canivete', 'capa', 'capacete', 'cassete', 'cassetete', 'castiçal', 'cata-vento', 'celular', 'chicote', 'chinelo', 'chupeta', 'cinzeiro', 'clipe', 'colchão', 'colher', 'comando', 'computador', 'copo', 'dado', 'daguerreótipo', 'dardo', 'dedal', 'delineador', 'dentadura', 'descascador', 'desentupidor', 'desfibrilador', 'desodorante', 'despertador', 'detergente', 'diábolo', 'diadema', 'diamante', 'diapasão', 'diário', 'dicionário', 'didjeridu', 'dinamite', 'discman', 'disco', 'disquete', 'divã', 'dobradiça', 'dominó', 'draga', 'dreno', 'drone', 'DVD', 'echarpe', 'edredom', 'elástico', 'envelope', 'enxada', 'escada', 'escopeta', 'escorredor', 'escova', 'escudo', 'escumadeira', 'esfregão', 'esmalte', 'espada', 'espanador', 'esparadrapo', 'espátula', 'espelho', 'espingarda', 'espiral', 'esponja', 'espremedor', 'esquadro', 'estátua', 'esteira', 'estetoscópio', 'estojo', 'estribo', 'etiqueta', 'extintor', 'faca', 'fagote', 'fantoche', 'farol', 'fax', 'ferradura', 'ferro', 'fichário', 'filmadora', 'abajur', 'perfume', 'aviao', 'aeronave', 'carros', 'pneu', 'aeroporto', 'viagem', 'lua', 'sol']

def palavra_aleatoria():
    return random.choice(palavras)

letras_acertadas = ''
letras_erradas = ''
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
            if letra_digitada in letras_erradas:
                print('Esta letra já foi digitada, tente com outra letra!')
                numero_tentativas -= 1
                continue

            elif not letra_digitada in palavra_secreta:
                letras_erradas += letra_digitada
                continue

        for letra_secreta in palavra_secreta:
            os.system('cls')
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            print('='*100)
            numero_tentativas = 0
            letras_acertadas = ''
            letras_erradas = ''
            break