#ESTUDOS DE DICT COMPREHENSION

produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritório',
}

# dc = {
#     chave: valor
#     if isinstance(valor, (int, float)) else valor.upper()
#     for chave, valor
#     in produto.items()
# }

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor #serve para identificar se algum valor no dicionário é uma string, caso não seja ele vai ser somente seu valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

for item, valor in dc.items():
    print(item,':', valor, end='\n')