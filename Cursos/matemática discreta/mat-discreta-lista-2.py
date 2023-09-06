import matplotlib.pyplot as plt
import numpy as np

#Função do primeiro grau
def funcaoPrimeiroGrau(a, b, x):
    return (a*x + b)

#Criando o eixo X
vetorX = np.arange(-5, 5, 1)
print(vetorX) # [-5 -4 -3 -2 -1 0 1 2 3 4] np.arange(POSIÇÃO INICIAL, POSIÇÃO FINAL, QUANTO AUMENTA)

#Criando o eixo Y
criandoFuncao = funcaoPrimeiroGrau(2, 5, vetorX)
vetorY = np.array(criandoFuncao)
print(vetorY)


#Criando o gráfico
fig = plt.figure(figsize=(10,10))
# plt.scatter(vetorX, vetorY, label = "Função primeiro Grau") # Demonstra os pontos desejáveis
plt.plot(vetorX, vetorY, label = "Função primeiro Grau") # Faz uma linha contínua
plt.title('f(x) = ax + b') # Título da função
plt.xlabel('eixo x') # Nome do label
plt.ylabel('eixo y') # Nome do label
plt.legend()
plt.grid(True, which='both') # Faz a separação dos quadrados
plt.axhline(y=0, color='k') # Deixa em negrito a linha 
plt.axvline(x=0, color='k') # Deixa em negrito a linha
plt.show() # Abre uma imagem

# Podemos observar que foi feito um gráfico com os pontos de x y
# Aumentou a quantidade de pontos
# Foi alterado o arange para