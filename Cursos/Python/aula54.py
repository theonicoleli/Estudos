pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completas = {**pessoa, **dados_pessoa}

print(pessoas_completas)

def mostro_argumentos_nomeados(*args,**kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana')

# a, b = pessoa.items()
# print(a, b)

# for chave, valor in pessoa.items():
#     print(chave, ':', valor)