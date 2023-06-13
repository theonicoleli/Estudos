# 1) Implemente um programa em Python para verificar se um número
# passado como argumento para um módulo está em um determinado
# intervalo de valores, também passado como argumento. Se estiver o
# módulo retorna True, senão False.

def verificador_numero(numero):
    if numero in range(11):
        print('Número válido!')
        return True
    else:
        print('Número não válido!')
        return False
    
while True:
    numero = int(input('Digite um número: '))
    verificador_numero(numero)