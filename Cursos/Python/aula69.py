# Estudos com map

# map(funcao, sequencia)
# O map recebe a função e aplica a cada elemento contido na sequência
# Alguns exemplos a baixo:

# DOBRANDO NÚMEROS

def dobrar(numero):
    return numero * 2

numeros = [1,2,3,4,5]
dobrados = map(dobrar, numeros)

numeros_dobrados = list(dobrados)
print(numeros_dobrados) # o resultado do print será: [2, 4, 6, 8, 10]


# CONVERTENDO PARA UPPERCASE

palavras = ['estudos','de','python','com','théo']
uppercase = map(str.upper, palavras)

list_uppercase = list(uppercase)
print(list_uppercase) # o resultado do print será: ['ESTUDOS', 'DE', 'PYTHON', 'COM', 'THÉO']


# CONVERTENDO VALORES NUMÉRICOS PARA STRING

valores = [10, 20, 30, 40, 50]
valores_como_strings = map(str, valores)

lista_valores_como_strings = list(valores_como_strings)
print(lista_valores_como_strings)  # o resultado do print será: ['10', '20', '30', '40', '50']
