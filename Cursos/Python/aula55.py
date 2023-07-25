#List Comprehension

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]

# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

# novos_produtos = [
#     {'nome': produto['nome'], 'preco': produto['preco'], }
#     for produto in produtos
# ]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] * 1.05) > 10
]

# print(*novos_produtos, sep='\n')          
# print(novos_produtos)

p(novos_produtos)