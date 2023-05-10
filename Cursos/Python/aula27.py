# Aprendendo a usar % no python
# d e i (inteiros)
# s - string
# f - float
# x e X - Hexadecimais (ABCDEF0123456789)

# nome = 'Théo'
# preco = 1000.948375458
# variavel = f'%s, o preço é %.2f' % (nome, preco)
# print(variavel)
# print(f'O hexadecimal de %d é %000X '% (1500, 1500))

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: <10}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{variavel:$<10}')
print(f'{variavel:#>10}')
print(f'{variavel:&^10}')
print(f'{993945.49534590430:,.2f}')