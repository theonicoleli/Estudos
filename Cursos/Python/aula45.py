def matrizes_valores(matriz):
    print(matriz)
    for linha in range(nLinhas):
        for coluna in range(nColunas):
            matriz[linha][coluna] = int(input('Digite um valor: '))
    return matriz

def somatoria_matriz(matrizC, matrizA, matrizB):
    for linha in range(nLinhas):
        for coluna in range(nColunas):
            matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
    return matrizC

nLinhas = 2
nColunas = 2
matrizA = [0] * nLinhas
matrizB = [0] * nLinhas
matrizC = [0] * nLinhas
for linha in range(nLinhas):
    matrizA[linha] = [0] * nColunas
    matrizB[linha] = [0] * nColunas
    matrizC[linha] = [0] * nColunas
matrizes_valores(matrizA)
matrizes_valores(matrizB)
somatoria_matriz(matrizC, matrizA, matrizB)
print(matrizC)
