# Nome: Théo lucas Nicoleli

# 1) Criar conjuntos

a = {1,2,3,4,5,6}
print(a)

# 2) Criar conjuntos apartir de lista:

lista = ['banana', 'peras', 'laranjas', 'abacates']
b = set(lista)
print(b)

# 3) Seguindo a mesma lógica do anterior:

lista_dois = ['banana', 'peras', 'laranjas', 'limões', 'bananas', 'bananas', 'abacates', 'laranjas']
c = set(lista_dois)
print(c)

# Comparando os itens, podemos perceber que nos conjuntos, os elementos não se repetem

# 4) Imprima a cardinalidade do conjunto C obtido no item 3 da forma: "A cardinalidade do conjunto C = {} é tamanho"

print(len(c))

# 5) Teste as relações de pertinência e imprima a resposta (D = {1,2,3,4,5})
# Dica: utilize a palavra reservada do python “in”

d = {1,2,3,4,5}

# a) 2 ∈ 𝐴:

if (2 in d):
    print('Sim, estou em A!')
else:
    print('Não incluso em A')

# b) 6 ∈ 𝐴:

if (6 in d):
    print('Sim, estou em A!')
else:
    print('Não incluso em A')

# c) ∅ ∈ 𝐴:

if (set() in d):
    print('Sim, estou em A!')
else:
    print('Não incluso em A')


# 6) Teste a igualdade entre os conjuntos e = {1,2,3} e f = {3,2,1}, A é igual a B? Imprima o resultado

e = {1,2,3}
f = {3,2,1}

if (e == f):
    print('Somos iguais!')
else:
    print('Não somos iguais.')

# 7) Utilize a função issubset() para testar todos os subconjuntos de g = {2,3,4} – imprima os resultados

g = {2,3,4}

print(f"O número dois {'está em g!' if {2}.issubset(g) else 'não está em g.'}")
print(f"O número dois {'está em g!' if {3}.issubset(g) else 'não está em g.'}")
print(f"O número dois {'está em g!' if {4}.issubset(g) else 'não está em g.'}")

# Agora, faça o teste utilizando o operador de pertinência em python para o seguinte exemplo:
# {1,2} ∈ G
if ({1,2} in g):
    print('Está contido!')
else:
    print('Não está contido.')
# Qual resultado é esperado? O python respeita esse resultado? 
# O resultado deverá ser falso, e o python interpretou corretamente!

# Faça o teste para o conjunto vazio:
# ∅ 𝑐 G
if (set().issubset(g)):
    print('O conjunto vazio pertence a g!')
else:
    print('Conjunto vazio não pertence a G.')
# Qual resultado é esperado? O python respeita esse resultado?
# O resultado esperado era de ser verdadeiro, e o python interpretou corretamente!


# 8) Crie uma verificação para testar se H = {1,2,3} é subconjunto próprio de I = {1,2,3,4,5} – imprima o código e resultado.
# Agora reaproveite o código para testar se J = {5,3,4,2,1} é subconjunto próprio de I.

h = {1,2,3}
i = {1,2,3,4,5}
j = {5,3,4,2,1}

print(f"O conjunto H é {'subconjunto de I!' if h.issubset(i) else 'não é subconjunto de I.'}")
print(f"O conjunto J é {'subconjunto de I!' if j.issubset(i) else 'não é subconjunto de I.'}")


# 9) Considerando k = {1,2,3,4,5} e l = {4,5,6,7,8,9,10} faça a conta (mostrando a simbologia matemática e 
# imprima os resultados em python)

k = {1,2,3,4,5}
l = {4,5,6,7,8,9,10}

# a) k ∪ l
print(k | l) # | em python é utilizado para fazer união de conjuntos, ou pode ser utilizado o .union() também!
print(k.union(l))
# b) k ∩ l
print(k & l) # & em python é utilizado para interseção de conjuntos, ou pode ser utilizado o .intersection() também!
print(k.intersection(l))
# c) k – l
print(k - l) # - em python é utilizado para diferença de conjuntos, ou pode ser utilizado o .difference() também!
print(k.difference(l))
# d) L – K
print(l - k)
print(l.difference(k))
