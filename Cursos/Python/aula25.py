numeros = [0,1,2,3,4,5,6,7,8,9,10]
digito = int(input('Digite um número: '))
if digito in numeros:
    print(f'Seu valor está na posição {numeros[digito]}')
else:
    print('Seu valor não está no vetor')