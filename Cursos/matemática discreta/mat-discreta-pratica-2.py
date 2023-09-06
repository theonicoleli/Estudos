import matplotlib.pyplot as plt
import numpy as np


def segundoGrauFunction(a, b, c, x):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não existe solução"
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        return x1, x2

vetorX = np.arange(-5, 5, 0.1)  # Use um passo menor para obter uma curva mais suave
vetorY = [segundoGrauFunction(2, 3, 1, x) for x in vetorX]

plt.plot(vetorX, vetorY, label="Função do segundo grau")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# Função exponencial
def funcaoExponencial(a, b, x):
    return a * (b ** x)

# Valores para a e b
a = 1  # Substitua pelo valor desejado
b = 2  # Substitua pelo valor desejado

# Valores de x no intervalo desejado
x = np.arange(-5, 5, 0.1)

# Calcular os valores correspondentes de y
y = funcaoExponencial(a, b, x)

# Criar o gráfico
plt.plot(x, y, label=f'Função Exponencial: y = {a} * {b}^x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Gráfico da Função Exponencial')
plt.show()


x = np.linspace(-10, 10, 400)  # Gere 400 pontos de -10 a 10

# Calculando os valores correspondentes de y usando a função funcaoModular
y = np.abs(x)

# Criando o gráfico
plt.plot(x, y, label='|x|', color='b')
plt.xlabel('x')
plt.ylabel('|x|')
plt.title('Gráfico da Função |x|')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()


# Criando um intervalo de valores x em graus
x_degrees = np.linspace(0, 360, 1000)  # Gere 1000 pontos de 0 a 360 graus

# Calculando os valores correspondentes de y usando a função funcaoSeno
y = np.sin(np.radians(x_degrees))

# Criando o gráfico
plt.plot(x_degrees, y, label='sin(x)', color='b')
plt.xlabel('Ângulo (graus)')
plt.ylabel('sin(x)')
plt.title('Gráfico da Função sen(x)')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
