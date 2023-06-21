contIguais = 0

sorteio = [1, 2, 3, 4, 5, 6]
aposta = []

for numbers in range(6):
    aposta.append(int(input(f'Digite um número por vez da sua aposta, na posição {numbers+1}: ')))

for contSorteio in range(len(sorteio)):
    for contAposta in range(len(aposta)):
        if sorteio[contSorteio] == aposta[contAposta]:
            contIguais += 1

print("Iguais = ", contIguais)