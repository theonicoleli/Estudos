#ESTUDOS DE MÉTODOS DE DICIONÁRIO

dicionario = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
dicionario_dois = {11: 19, 12: 99}

#dicionario[11] = dicionario.get(11, valor_padrao) + valor_desejado
#Retorna o valor associado à chave especificada. 
#Se a chave não existir, retorna o valor_padrao fornecido em vez de gerar um erro.
#Ou pode criar uma nova chave para que possa ser atribuido um valor novo a ela com o valor_desejado

dicionario.keys() 
# Retorna uma visualização de todas as chaves do dicionario, neste caso em um print retornaria:
# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(dicionario.keys())

dicionario.values()
# Tem o mesmo processo do keys, porem ele retorna o valor atribuido aquela chave, neste caso em um print retornaria:
# ([25, 18, 15, 12, 10, 8, 6, 4, 2, 1])
print(dicionario.values())

dicionario.items()
# Retorna uma visualização de cada chave e seu valor, neste caso em um print retornaria:
# ([(1, 25), (2, 18), (3, 15), (4, 12), (5, 10), (6, 8), (7, 6), (8, 4), (9, 2), (10, 1)])
print(dicionario.items())

dicionario.update(dicionario_dois)
# Adiciona um dicionário em outro, neste caso estou adicionando o dicionario_dois em dicionario, retornando um print ficaria:
# {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1, 11: 19, 12: 99}
print(dicionario)

dicionario.pop(11, 19)
dicionario.pop(12, 99)
# Com .pop é possível retirar uma chave e um valor inclusos no dicionário, retornando um print ficaria:
# {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
print(dicionario)

dicionario.popitem()
# Com .popitem é possível retirar a última chave e seu valor, neste caso um print ficaria assim:
# {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2}
print(dicionario)

dicionario.clear()
# Com .clear é possível limpar seu dicionário, neste caso um print ficaria assim:
# {}
print(dicionario)