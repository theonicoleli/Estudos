# Calculadora em PYTHON

def is_float(string):
    try:
        float(string)
        return True
    except:
        return False
    
    
def processamentos(string):
    if tipo_processamento == string:
        numeros = []
        while 1==1:
            numero = input('Número (caso queira finalizar a operação digite [S]air): ')
            if string==5 and numero.isdigit():
                numero = int(numero)
                if numero >= 1:
                    contador = numero
                    fatorial = 1
                    while contador > 1:
                        fatorial = fatorial * contador
                        contador = contador - 1
                    print(f'O valor final de sua operação foi: {fatorial}')
                else:
                    if numero == 0:
                        print(f'O valor final de sua operação foi: {fatorial}')
                    else:
                        print("Numero negativo!")
                print('='*100)
                break
            if is_float(numero):
                numero = float(numero)
                numeros.append(numero)
            elif not numero.isnumeric():
                numero = str(numero)
                numero = numero.islower()
                resultado = numeros[0]
                if numero == 'sair' or 's':
                    if string==1:
                        print(f'O valor final de sua operação foi: {round(sum(numeros), 2)}')
                    elif string==2:
                        for i in range(1, len(numeros)):
                            resultado -= numeros[i]
                        print(f'O valor final de sua operação foi: {round(resultado, 2)}')
                    elif string==3:
                        for i in range(1, len(numeros)):
                            resultado *= numeros[i]
                        print(f'O valor final de sua operação foi: {round(resultado, 2)}')
                    elif string==4:
                        for i in range(1, len(numeros)):
                            resultado /= numeros[i]
                        print(f'O valor final de sua operação foi: {round(resultado, 2)}')
                    print('='*100)
                    break
            else:
                print('Escolha um valor válido!')

print('Calculadora!')
while True:
    tipo_processamento = input('As opções são:\n1) Soma\n2) Subtração\n3) Multiplicação\n4) Divisão\n5) Fatorial\nDigite o tipo de processamento você deseja: ')
    if tipo_processamento.isdigit():
        tipo_processamento = int(tipo_processamento)
        processamentos(tipo_processamento)
    else:
        print('Selecione um valor válido!')
        continue
            