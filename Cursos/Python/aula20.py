# Fazer um sistema que pegue 5 notas e faça a média, porém sem quebra de programa!

nomes = {}

while True:
    print('Média de suas notas')
    nome = input('Digite seu nome: ')
    if nome in nomes:
        print(f'Sua média já foi registrada, {nome}: {nomes[nome]}')
    else:
        notas = []
        while len(notas)<5:
            nota = input('Digite uma nota: ')
            if not nota.isdigit():
                print('Digite uma nota válida!')
            else:
                nota = float(nota)
                notas.append(nota)
        sum_notas = sum(notas)/len(notas)
        nomes[nome] = sum_notas
        print(f'Sua nota média foi: {sum_notas}')