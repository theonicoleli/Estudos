#Ao utilizar __all__, você limita para que ao importar a biblioteca, puxar apenas os argumentos listados por ela

# __all__ = [
#     'variavel',
#     'soma_do_modulo'
# ]


# from aula67_package.modulo_b import say_hello   # maneira correta de importar
# from modulo_b import say_hello  # maneira errada de importar

variavel = 'Sou a variavel de "aula67_package"'

def soma_do_modulo(x,y):
    return x + y

nova_variavel = 'Théo'
# say_hello()