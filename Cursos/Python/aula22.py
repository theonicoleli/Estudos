# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print('Seja bem vindo ao nosso mundo!')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
ano_atual = input('Digite o ano atual: ')
ano_nascimento = int(ano_atual) - idade

print(f'Seja bem vindo {nome}! O ano de seu nascimento é {ano_nascimento} ')