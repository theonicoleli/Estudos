import random

preco = [1,2,3,4,5,6,7,8,9,10]
possivel_troco = [1,2,3,4,5,6,7,8,9]

def preco_aleatorio():
    return random.choice(preco)

def vezes_aleatoria():
    return random.choice(possivel_troco)

vezes = vezes_aleatoria()

def troco_mercado():
    numbers = []
    for number in range(vezes):
        variavel = random.choice(possivel_troco)
        numbers.append(variavel)
    return numbers

troco_random = troco_mercado()
troco_random_str = ''.join(str(troco) for troco in troco_random)
troco_random_str = int(troco_random_str)
produtos = []

produtos_mercado = {}

vendas = 0
lucro = 0

for c in range(1,101):
    produtos.append(c)

for produto in produtos:
    produtos_mercado[produto] = preco_aleatorio()

while True:
    print(produtos)
    compra = input('Digite o produto que deseja pagar: ')
    if compra.isdigit():
        compra = int(compra)
        compra = produtos_mercado[compra]
        valor = compra
        print(f'O valor a ser pago é de {valor}')
        pagamento = input('Digite o valor a pagar: ')
        if pagamento.isdigit():
            pagamento = int(pagamento)
            if pagamento == valor:
                print('Obrigado por comprar conosco!')
                vendas += 1
                lucro += valor
            elif pagamento>valor:
                print('Obrigado por comprar conosco!')
                vendas += 1
                lucro += valor
                valor = pagamento - valor
                if troco_random_str >= valor:
                    print(f'O seu é troco é de: {valor}')
                else:
                    print('Estamos sem troco, aceitamos apenas valores inteiros!')
            else:
                print('Faça o pagamento completo, na próxima vez, cancelando pedido!')
        else:
            print('Digite um valor válido!')
    elif compra == '':
        print(f'As vendas realizadas foram {vendas}, já o valor ganho foi {lucro} R$ e o troco disponível é de {troco_random_str} R$')
    else:
        print('Digite um valor válido!')