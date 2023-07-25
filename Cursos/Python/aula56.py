# string = 'Théo Lucas Nicoleli'
# numero_de_letras = 5
# nova_string = '.'.join(
#     [string[indice: indice + numero_de_letras]
#     for indice in range(0, len(string), numero_de_letras)])
# print(nova_string)

nomes = ['luiz','maria','helena','josé','pedro']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)