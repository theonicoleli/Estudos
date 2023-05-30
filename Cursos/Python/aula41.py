#ESTUDOS DE MÉTODOS DE SET
# SET É UM MÉTODO MUTÁVEL, PORÉM SEUS ARGUMENTOS SÃO IMUTÁVEIS

test_list = [5, 6, 7]

s1 = set()
s1.add(10)
# Com o add podemos adicionar um elemento por vez na set();
# Se printar, ficará assim:
# {10};
# lembrando que ele utiliza de chaves assim como o dicionário, porém diferente do dicionário, ele salva apenas 1 argumento.
print(s1)

s1.update((18, 20, 30, 40))
# Foi transformado para tupla para que fosse possível passar as informações sem quebrar os números;
# Por exemplo, se fizesse assim:
s2 = {2,3,4}
s2.update('Otavio')
# Cada letra do Otavio, ficara separada, por isso transformamos para tupla, para que não se perca os argumentos
print(s2)
# Com o update podemos adicionar vários elementos de uma vez na set();
# Se printar, ficará assim:
# {10, 18, 20, 30, 40}
print(s1)
# Com o update podemos adicionar outro set, tupla, lista a sua set atual, por exemplo:
s1.update(s2)
s1.update(test_list)
print(s1)

s1.remove(10)
# Com o remove, podemos retirar um elemento que desejamos de nosso set.
# Porém apenas remove aquele presente no set, caso contrário ocorrerá um erro
# Neste caso eu removi o 10.
print(s1)

s1.discard(18)
# Com o discard, podemos retirar um elemento que desejamos de nosso set.
# Porém diferente do remove, caso não exista o elemento desejado para retirar, não ocorrerá um erro.
# Neste caso eu removi o 18.
print(s1)

s1.pop()
# Remove e retorna um elemento arbitrário do conjunto.
print(s1)

s3 = {100, 1000, 10000}
s1 = s1.union(s3)
# Retorna um novo conjunto que contém todos os elementos de ambos os conjuntos.
print(s1)

s1 = s1.intersection(s3)
# Retorna um novo conjunto que contém só os elementos presentes em ambos os conjuntos.
print(s1)

s4 = {100, 93, 83, 28}
s1 = s1.difference(s4)
# Retorna um novo conjunto dos elementos diferentes dos presentes no s4
print(s1)

s1 = s1.symmetric_difference(s4)
# Retorna um novo conjunto dos elementos diferentes em ambas as sets
# Ou seja, vai printar todos os argumentos diferentes
print(s1)