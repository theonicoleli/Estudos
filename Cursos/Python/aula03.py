valor = 30000 # Valor do preço do carros é de 30000

print("Preço do carro = ", valor,"R$")
quantidade = int(input("Digite quantos carros você deseja comprar: "))
desconto = int(input("Digite quanto de desconto foi ofericido a você pelos carros: "))


if desconto !=0:
    custo = (valor*((desconto)/100))*quantidade
else:
    custo = (valor*quantidade)

print(custo, "reais em desconto")
preço = 30000 * quantidade - custo
print("Valor final de", preço, "reais")