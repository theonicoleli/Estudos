# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda x: x['nome'],
    reverse=True
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos_ordenados_por_nome),
    key = lambda x: x['preco']
)


# Estudos com key

outros_produtos = [
    {'nome': 'Celular TopMax', 'preco': 1500.00},
    {'nome': 'Smart TV UltraHD', 'preco': 2000.99},
    {'nome': 'Fone Sem Fio', 'preco': 99.90},
    {'nome': 'Abacate App', 'preco': 499.50},
    {'nome': 'Notebook UltraFast', 'preco': 2999.00},
]

# Ordena a lista outros_produtos pelo nome em ordem alfabética usando o campo 'nome' como chave
outros_produtos.sort(key=lambda x: x['nome'])

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*outros_produtos, sep='\n')