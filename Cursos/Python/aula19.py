# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
while True:
    saltos = []
    nome = input('Digite seu nome: ')
    while len(saltos)<5:
        salto = input('Digite a altura do salto em metros: ')
        if salto=='' or salto==f'\D':
            print('Digite a altura, por favor!')
        elif is_float(salto):
            salto = float(salto)
            saltos.append(salto)
    if len(saltos)==5:
        maior_salto = max(saltos)
        menor_salto = min(saltos)
        len_saltos = len(saltos)-2
        resto_saltos = (sum(saltos)-(menor_salto + maior_salto))/len_saltos

        print(f'O maior salto foi: {maior_salto} metros')
        print(f'O menor salto foi: {menor_salto} metros')
        print(f'A média dos restos dos saltos foram: {round(resto_saltos, 2)} metros')

        print('RESULTADO FINAL:')
        print(f'A média de {nome} foi de {round(resto_saltos, 2)} metros')
        print('='*100)
    else:
        continue



        
        
