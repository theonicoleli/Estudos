tabela = [    ['Nome', 'Idade', 'Profissão'],
    ['Ana', 25, 'Engenheira'],
    ['Carlos', 38, 'Advogado'],
    ['Marta', 30, 'Médica'],
    ['João', 45, 'Professor']
]

for linha in tabela:
    for coluna in linha:
        print(f''.join(str(coluna).ljust(12)), end='')
    print()