#Fazer uma nova função pausada que recebe uma função e apenas um valor e faça a função apenas com esse valor

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executa_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

somaCinco = executa_funcao(soma, 5)
multiplicaDez = executa_funcao(multiplica, 10)
print(somaCinco(5))
print(multiplicaDez(10))