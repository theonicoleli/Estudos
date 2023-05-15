import os

lista = []

print('='*100)
print('ESTUDO DE STRING COM LISTA')
print('='*100)
while True:
    opcao = input('Quais processos gostaria de realizar com sua lista:\n[1] inserir itens\n[2] Apagar itens\n[3] Verificar itens\n[4] Encerrar Programa\nOPÇÃO: ')
    if opcao.isdigit():
        opcao = int(opcao)
        if 1<=opcao<=3:
            if opcao==1:
                os.system('cls')
                acrescentar = input('Digite oque gostaria de adicionar a lista: ')
                lista.append(acrescentar)
                print(f'O item acrescentado foi: {acrescentar}')
            elif opcao==2:
                os.system('cls')
                opcao_remocao = input('Você deseja apagar oque:\n[1] Apagar toda a lista\n[2] Apagar um item em específico\nOPÇÃO: ')
                if opcao_remocao.isdigit():
                    opcao_remocao = int(opcao_remocao)
                    if opcao_remocao==1:
                        lista = []
                        print('Limpamos sua lista!')
                    elif opcao_remocao==2:
                        remover = input('Digite oque gostaria de retirar: ')
                        if remover in lista:
                            lista.remove(remover)
                            print(f'O item retirado foi: {remover}')
                        else:
                            os.system('cls')
                            print('Digite algo incluso na lista!')
                    else:
                        print('Digite um número válido!')
                else:
                    print('Digite um valor válido!')
            elif opcao==3:
                os.system('cls')
                print(f'Os valores inclusos na lista são: {lista}')
        elif opcao==4:
            os.system('cls')
            print('Obrigado por testar nosso programa!')
            break
        else:
            os.system('cls')
            print('Escolha um número válido!')
    else:
        os.system('cls')
        print('Digite um valor válido!')