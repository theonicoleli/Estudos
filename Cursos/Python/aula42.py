import os

print('Banco do Brasil')

nome_cpf = {}

def criar_conta():
    global nome_cpf

    while True:
        try:
            nome = str(input('Digite seu nome: '))
            cpf = input('Digite seu cpf: ')
            saldo = input('Insira a quantidade de dinheiro desejada para a sua conta: ')
            
            if cpf.isdigit() and saldo.isdigit():
                nome_cpf[cpf] = {'nome': nome, 'saldo': int(saldo)}
                break
            else:
                print('Digite um CPF e saldo válidos!')
        except ValueError:
            print('Digite algo válido!')
            continue

def deposito_retirada_saldo():
    global nome_cpf

    while True:
        selecao = input('Digite:\n[1] Depósito\n[2] Retirada\n[3] Ver saldo\nDigite ao lado: ')

        if selecao.isdigit():
            selecao = int(selecao)
            cpf = input('Digite seu cpf: ')

            if cpf in nome_cpf:
                if selecao == 1:
                    deposito = int(input('Digite a quantidade desejada para a inserção: '))
                    nome_cpf[cpf]['saldo'] += deposito
                    print('Depósito realizado com sucesso!')
                    break
                elif selecao == 2:
                    retirada = int(input('Digite a quantidade desejada para a retirada: '))
                    if nome_cpf[cpf]['saldo'] >= retirada:
                        nome_cpf[cpf]['saldo'] -= retirada
                        print('Retirada realizada com sucesso!')
                        break
                    else:
                        print('Saldo insuficiente!')
                elif selecao == 3:
                    print('Saldo :', nome_cpf[cpf]['saldo'], 'R$')
                    voltar = input('Digite: \n[1] Para voltar\nDigite ao lado: ')
                    if voltar.isdigit():
                        voltar = int(voltar)
                        if voltar == 1:
                            break
                        else:
                            break
                else:
                    print('Selecione um valor válido!')
            else:
                print('CPF não encontrado!')
                break
        else:
            print('Digite um número válido!')

while True:
    os.system('cls')
    selecao_inicial = input('Digite:\n[1] Para criar conta\n[2] Para usar conta\nDigite ao lado: ')
    if selecao_inicial.isdigit():
        selecao_inicial = int(selecao_inicial)
        if selecao_inicial == 1:
            criar_conta()
        elif selecao_inicial == 2:
            deposito_retirada_saldo()
        else:
            print('Digite um número válido!')
    else:
        print('Digite um número válido!')
