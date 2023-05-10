# Converte números para hexadecimal

print('Converta seu número para hexadecimal')
while True:
    numero = input('Digite o número: ')
    if numero.isdigit():
        numero = int(numero)
        print(f'O número %s convertido para hexadecimal é %X' % (numero, numero))
    else:
        print('Digite um número válido!')