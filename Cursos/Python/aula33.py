import random

preco = [1,2,3,4,5,6,7,8,9,10]

def preco_aleatorio():
    return random.choice(preco)

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
            else:
                print('Faça o pagamento completo, na próxima vez, cancelando pedido!')
        else:
            print('Digite um valor válido!')
    elif compra == '':
        print(f'As vendas realizadas foram {vendas}, já o valor ganho foi {lucro} R$')
    else:
        print('Digite um valor válido!')