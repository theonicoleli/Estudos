def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|','x + y + z=', x + y + z)

while True:
    numero = input('Digite um número que deseja somar: ')
    numero_dois = input('Digite o segundo número a somar: ')
    numero_tres = input('Digite o terceiro número: ')
    if (numero and numero_dois and numero_tres).isdigit():
        numero = int(numero)
        numero_dois = int(numero_dois)
        numero_tres = int(numero_tres)
        soma(numero, numero_dois, numero_tres)
    else:
        print('Escolha um número válido')