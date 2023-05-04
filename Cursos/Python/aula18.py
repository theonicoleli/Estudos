# Escreva um programa que imprima todos os números ímpares entre 1 e 100. Para isso, você pode utilizar um laço de repetição while para iterar de 1 a 100, e dentro do laço, utilizar um condicional if para verificar se o número atual é ímpar. Se for, imprima-o na tela.

#for i in range(1,101): # Utilizando For
    #if i % 2 != 0:
        #print(i)

digito = int(input('Digite o número que você quer que o contador chegue mostrando todos os impares: '))
number = 0
while True: # Utilizando while
    if number % 2 !=0:
        print(number)
    if number == digito:
        break
    number+=1