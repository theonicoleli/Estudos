pessoas = {}

while True:
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    if nome in pessoas:
        print(f'Você já foi registrado(a), nome: {nome}, idade: {idade} anos')
    elif not nome.isdigit() and idade.isdigit():
        print(f'Me chamo {nome} e tenho {idade} anos')
        pessoas[nome] = idade
    else:
        print('Não foi digitado nenhum nome e nenhuma idade')