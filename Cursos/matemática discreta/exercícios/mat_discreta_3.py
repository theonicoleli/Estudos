import random

# exercício 6

def calculoMediaAltura(alturas):
    n = len(alturas)
    soma = sum(alturas)
    media = soma / n

    return media


def fatorial(valor):
    if valor < 0:
        return "Fatorial não definido para números negativos"
    elif valor == 0:
        return 1
    else:
        return valor * fatorial(valor - 1)


alturas = [1.8, 1.65, 1.72, 1.82, 1.91]
mediaAltura = calculoMediaAltura(alturas)

print(f"A média de altura foi de: {mediaAltura:.2f} metros")

#exercícios 8
result = 0

for x in range(2, 6):
    for y in range(2, 4):
        result += (x + y) ** 2

print(result)

result = 0

for x in range(1, 4):
    for y in range(1, 3):
        result += (x*y-5)

print(result)

# exercício 9

result = 0

for x in range(5):
    result += (-1)**x*fatorial(x)

print(result)

result = 0
another_result = 0

for x in range(5):
    result += x

result = result**2

for y in range(5):
    another_result += y**2

final = result - another_result

print(final)


# exercício 10
def inverterVetor(vetor):
    vetor.reverse()

vetor = []
vezes = 5

for x in range(vezes):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

inverterVetor(vetor)
print(vetor)


# exercício 11

def sorteia(lista):
    for _ in range(6):
        valor = random.randint(1, 9)
        lista.append(valor)

def somarPar(lista):
    soma_par = 0
    pares = []
    
    for valor in lista:
        if valor % 2 == 0:
            soma_par += valor
            pares.append(valor)
    
    return soma_par, pares

num = []
sorteia(num)

soma, pares = somarPar(num)
print("Números sorteados:", num)
print("Pares sorteados:", pares)
print("A soma dos números pares foi de:", soma)


# exercício 12

def contar_consoantes(vetor):
    consoantes = []
    for caractere in vetor:
        if caractere.isalpha() and caractere.lower() not in "aeiou":
            consoantes.append(caractere)
    return consoantes

vetor = []

for _ in range(6):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)

consoantes = contar_consoantes(vetor)
numero_consoantes = len(consoantes)

print("Consoantes encontradas:", numero_consoantes)
print("Consoantes no formato de relação:", ", ".join(consoantes))


# exercício 13

def calcular_media(notas):
    return sum(notas) / len(notas)

num_alunos = 6
medias = []

for aluno in range(1, num_alunos + 1):
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Informe a nota {i} do aluno {aluno}: "))
        notas.append(nota)
    media = calcular_media(notas)
    medias.append(media)

num_alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {num_alunos_aprovados}")


# exercício 14

vetor_A = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor_A.append(numero)

soma_quadrados = sum(x ** 2 for x in vetor_A)

print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)