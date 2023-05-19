matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l},{c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)

for l in range(0, 3):
    linha = sum(matriz[l])
    print(f'A soma da linha {l} é: {linha}')
for c in range(0, 3):
    coluna = sum(matriz[c])
    print(f'A soma da coluna {c} é: {coluna}')

print('-=' * 30)