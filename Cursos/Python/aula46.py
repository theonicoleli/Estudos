def verifica_simetria(matriz):

    n = len(matriz)
    transposta = [[matriz[j][i] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != transposta[i][j]:
                return False
            
    return True

matriz = [
    [1,2,3],
    [2,4,5],
    [3,5,6]
]

if verifica_simetria(matriz):
    print('A matriz é simétrica!')
else:
    print('A matriz não é simétrica!')