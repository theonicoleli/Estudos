list = [33,37,44,16,21,1]
lista_dois = [8,4,5,6,7]
list[2] = 44 # Posição da lista e seu valor
list.append(12) # Adicionando o número 12 na lista
print(list)
list.sort() # Formata a lista para que fique organizada do menor para o maior
print(list)
list.insert(3, 27) # Posição e elemento
list.remove(1) # Removendo o número 1 da lista
list.pop() # Removendo o último número da lista
list.pop(0) # Removendo o número da posição 0
print(f'A quantidade total de número desta lista são de {len(list)}')
list.extend(lista_dois)
print(list)
print(f'Posição do número 37 na lista é: {list.index(37)}') # Retorna a posição do número digitado