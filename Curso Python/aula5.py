print('Eleição dos alunos')
augusto=0
davy=0
quantidade_alunos = int(input("Digite quantos alunos a sala de aula tem: "))
while quantidade_alunos>0:
    print('Escolha o representante: ')
    print('Augusto(1)')
    print('Davy(2)')
    voto = int(input('Digite ao lado o representante: '))
    if voto==1:
        augusto+=1
        print('Você votou em Augusto!')
        quantidade_alunos-=1
    elif voto==2:
        davy+=1
        print('Você votou em Davy')
        quantidade_alunos-=1
    else:
        print('Escolha um número válido')
if quantidade_alunos==0:
    if augusto>davy:
        print('Augusto é o representante!')
    elif davy>augusto:
        print('Davy é o representante!')
    else:
        print('Deve ser realizado uma nova eleição, pois os votos foram igualados!')