#Estudo de importlib entre outras abas e entre outras pastas
#Ao utilizar __all__, você limita para que ao importar a biblioteca, puxar apenas os argumentos listados por ela

# import importlib

# print('Aula 67!')

# import aula66

# for n in range(10):
#     print(n)
#     importlib.reload(aula66)

# import aula67_package.modulo
# from aula67_package import modulo
# from aula67_package.modulo import * # * == all

# from aula67_package.modulo import soma_do_modulo

# print('AULA67 PACKAGE')

# print(soma_do_modulo(1,2))
# print(aula67_package.modulo.soma_do_modulo(1,2))
# print(modulo.soma_do_modulo(1,2))
# print(variavel)
#print(nova_variavel) #Por exemplo esta variavel, ela não foi listada no __all__, devido a isso, ocorre este erro

# from aula67_package.modulo import say_hello, soma_do_modulo
# print(__name__)
# say_hello()

from aula67_package import soma_do_modulo, say_hello

print(soma_do_modulo(2,3))
say_hello()
