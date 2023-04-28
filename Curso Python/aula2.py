print("Preço do ingresso para o cinema")
quantidade = int(input("Digite o numero de ingressos ao qual você deseja comprar: "))
desconto = int(input("Caso você tenha disponível descontos e deseja utilizar, coloque a porcentagem em desconto:"))
valor = 20 # Valor do ingresso é 20 reais

if desconto != 0:
    ingresso = (valor*((desconto)/100)) * quantidade
else:
    ingresso = valor * quantidade

print(ingresso, "reais de desconto")
preço = 20 * quantidade - ingresso
print("Valor final de", preço, "reais")