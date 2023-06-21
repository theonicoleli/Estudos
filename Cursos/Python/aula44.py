def criar_matriz(linhas, colunas):

    matriz = [0.0] * linhas
    for cont in range(linhas):
        matriz[cont] = [0.0] * colunas

    return matriz

def preencher_matriz(matriz):

    for cont_linhas in range(len(matriz)):
        for cont_colunas in range(len(matriz[cont_linhas])):
            matriz[cont_linhas][cont_colunas] = float(input("Valor: "))

    return matriz

mat = criar_matriz(3, 5)
mat = preencher_matriz(mat)
print(mat)

# vezes = 3
# matriz = []
# linhas = 1

# while vezes!=0:
#     number = []
#     for cont in range(5):
#         variavel = float(input(f'Digite o valor para a linha: {linhas} e posição {cont+1}: '))
#         number.append(variavel)
#     matriz.append(number)
#     vezes -= 1
#     linhas += 1

# print(matriz)