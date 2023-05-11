# def saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar

# while True:
#     nome = input('Digite seu nome: ')
#     s1 = saudacao('Bom dia')
#     if not nome.isdigit():
#         print(s1(nome))
#     else:
#         print('Digite um nome, não um dígito!')

# falar_bom_dia = saudacao('Bom dia')
# falar_boa_noite = saudacao('Boa noite')
# falar_boa_tarde = saudacao('Boa tarde')

# for nome in ['Maria','Luiz', 'Regina', 'Alessandra', 'Nicole', 'Théo', 'Pedro']:
#     print(falar_bom_dia(nome))
# for nome in ['Maria','Luiz', 'Regina', 'Alessandra', 'Nicole', 'Théo', 'Pedro']:
#     print(falar_boa_tarde(nome))
# for nome in ['Maria','Luiz', 'Regina', 'Alessandra', 'Nicole', 'Théo', 'Pedro']:
#     print(falar_boa_noite(nome))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar

numero = input('Digite um número: ')
if numero.isdigit():
    numero = int(numero)
    duplicar = criar_multiplicador(numero)
    triplicar = criar_multiplicador(numero*numero)
    quadruplicar = criar_multiplicador(numero*numero*numero)
    print(duplicar(numero))
    print(triplicar(numero))
    print(quadruplicar(numero))
else:
    print('Escolha um número válido!')