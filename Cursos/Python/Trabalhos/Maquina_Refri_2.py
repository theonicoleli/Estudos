lista_de_produtos = []
moedas_cedulas = []
preco_dos_produtos = []
quantidade_dos_produtos = []

pagamento_continuacao = 0
pagamento_total_possivel = 0
vendas = 0
moedas_1_real_pagamento = 0
moedas_25_cent_pagamento = 0
moedas_50_cent_pagamento = 0
moedas_25_cent = 0+moedas_25_cent_pagamento
moedas_50_cent = 0+moedas_50_cent_pagamento
moedas_1_real = 0+moedas_1_real_pagamento
cedula_2_reais = 0
cedula_5_reais = 0
cedula_10_reais = 0
cedula_20_reais = 0
moedas_pagamento_total = moedas_1_real_pagamento+moedas_25_cent_pagamento+moedas_50_cent_pagamento 
moedas_totais = moedas_50_cent+moedas_25_cent+moedas_1_real+moedas_1_real_pagamento+moedas_25_cent_pagamento+moedas_50_cent_pagamento
cedulas_totais = cedula_2_reais+cedula_5_reais+cedula_10_reais+cedula_20_reais
cedulas_moedas_totais = moedas_50_cent+moedas_25_cent+moedas_1_real+moedas_1_real_pagamento+moedas_25_cent_pagamento+moedas_50_cent_pagamento+cedula_2_reais+cedula_5_reais+cedula_10_reais+cedula_20_reais

nomeadm = str(input("Olá Administrador, digite seu nome: "))
nomemaquina = str(input("Digite o nome ao qual você deseja que a máquina tenha: "))
quant_refri = int(input('Digite a quantidade de refri que você deseja que tenha: '))

for quantidade in range(quant_refri):
    lista_de_produtos.append(str(input(f'Digite o nome da bebida {quantidade+1}: ')))
    preco_dos_produtos.append(float(input(f'Digite o preço desejado em reais para a bebida {lista_de_produtos[quantidade]}: ')))
    quantidade_dos_produtos.append(int(input(f'Digite a quantidade desejada da bebida {lista_de_produtos[quantidade]}: ')))

add_reais = int(input('Quer adicionar moedas e cédulas:\nDigite [1] para SIM ou [2] para NÃO: '))
if add_reais == 1:
    while add_reais == 1:
        add_cedulas_moedas = int(input('Digite [1] para Cédula ou [2] para moedas: '))
        if add_cedulas_moedas == 1:
            cedula_2_reais = int(input('Digite a quantidade de cédulas de 2 reais: '))
            cedula_5_reais = int(input('Digite a quantidade de cédulas de 5 reais: '))
            cedula_10_reais = int(input('Digite a quantidade de cédulas de 10 reais: '))
            cedula_20_reais = int(input('Digite a quantidade de cédulas de 20 reais: '))
        elif add_cedulas_moedas == 2:
            moedas_25_cent = int(input('Digite a quantidade de moedas de 25 centavos: '))
            moedas_50_cent = int(input('Digite a quantidade de moedas de 50 centavos: '))
            moedas_1_real = int(input('Digite a quantidade de moedas de 1 real: '))
        continuar_adicionando = int(input('Digite [1] para continuar ou [2] para sair: '))
        if continuar_adicionando == 1:
            continue
        else:
            add_reais += 1
            break
elif add_reais == 2:
    print('Ok!')
else:
    print('Por favor, selecione um número válido!')
while True:
    entrada_moedas_25_cent = 0
    entrada_moedas_50_cent = 0
    entrada_moedas_1_real = 0
    continuacao_while = 0
    continuar_pagando = 0
    print('-='*30)
    print('Insira qual bebida você deseja comprar:')
    print('-='*30)
    for quantidade in range(quant_refri):
        print(f'[{quantidade+1}] {lista_de_produtos[quantidade]} = R$ {preco_dos_produtos[quantidade]}')
    selecao = int(input('Digite o número do refri para a compra: '))
    if 1 <= selecao <= quant_refri:
        if quantidade_dos_produtos[selecao-1] > 0:
            while continuacao_while==0:
                preco_dos_produtos_atual = preco_dos_produtos[selecao-1]
                if continuar_pagando == 0:
                    preco_dos_produtos_atual = preco_dos_produtos_atual
                    pagamento = int(input(f'O custo a ser pago é de {preco_dos_produtos_atual}\nVocê deseja realizar o pagamento de qual forma:\n[1] Moedas\n[2] Cédulas\n[3] Moedas e Cédulas\nInsira a forma a qual você deseja ao lado: '))
                elif continuar_pagando == 1:
                    preco_dos_produtos_atual = (preco_dos_produtos_atual-pagamento_continuacao)
                    pagamento = int(input(f'O custo a ser pago é de {preco_dos_produtos_atual}\nVocê deseja realizar o pagamento de qual forma:\n[1] Moedas\n[2] Cédulas\n[3] Moedas e Cédulas\nInsira a forma a qual você deseja ao lado: '))
                if pagamento == 1:
                    entrada_dinheiro = int(input('Digite:\n[1] Moedas de 25 centavos\n[2] Moedas 50 centavos\n[3] Moedas 1 real\nInsira a forma a qual você deseja ao lado: '))
                    if entrada_dinheiro == 1:
                        entrada_moedas_25_cent += int(input('Digite a quantidade de moedas de 25 centavos: '))
                        moedas_25_cent_pagamento += entrada_moedas_25_cent
                    elif entrada_dinheiro == 2:
                        entrada_moedas_50_cent += int(input('Digite a quantidade de moedas de 50 centavos: '))
                        moedas_50_cent_pagamento += entrada_moedas_50_cent
                    elif entrada_dinheiro == 3:
                        entrada_moedas_1_real += int(input('Digite a quantidade de moedas de 1 real: '))
                        moedas_1_real_pagamento += entrada_moedas_1_real
                    pagamento_total = (entrada_moedas_25_cent*0.25)+(entrada_moedas_50_cent*0.5)+(entrada_moedas_1_real*1)
                    if pagamento_total < preco_dos_produtos_atual:
                        continuar_pagando = int(input('Digite:\n[1] Para continuar pagando\n[2] Para cancelar compra e devolução de dinheiro\nDigite ao lado a opção: '))
                        if continuar_pagando == 1:
                            pagamento_continuacao = pagamento_total
                            continue
                        elif continuar_pagando == 2:
                            if entrada_moedas_25_cent>0:
                                print(f'Enviando as moedas de 25 centavos = [{entrada_moedas_25_cent}]')
                                entrada_moedas_25_cent -= entrada_moedas_25_cent
                            if entrada_moedas_50_cent>0:
                                print(f'Enviando as moedas de 50 centavos = [{entrada_moedas_50_cent}]')
                                entrada_moedas_50_cent -= entrada_moedas_50_cent   
                            if entrada_moedas_1_real>0:                             
                                print(f'Enviando as moedas de 1 real = [{entrada_moedas_1_real}]')
                                entrada_moedas_1_real -= entrada_moedas_1_real
                            break
                    else:
                        quantidade_dos_produtos[selecao-1] -= 1
                        if pagamento_total == preco_dos_produtos_atual:
                            print(f'Muito obrigado por comprar conosco!\nA quantidade atual de {lista_de_produtos[selecao-1]} é de {quantidade_dos_produtos[selecao-1]}')
                        elif pagamento_total > preco_dos_produtos_atual:
                            print(f'Muito obrigado por comprar conosco!\nA quantidade atual desta bebida é de {quantidade_dos_produtos[selecao-1]}')
                            continuacao_while==1
                            if pagamento_continuacao==0:
                                pagamento_total-=preco_dos_produtos_atual
                            else:
                                pagamento_total-=(preco_dos_produtos_atual+pagamento_continuacao)
                            if pagamento_total>0:
                                print(f'Seu troco foi de {pagamento_total}')
                            else:
                                break
                            if pagamento_total == 0:
                                break
                            else:
                                if pagamento_total>0 or pagamento_total>0 and cedulas_moedas_totais>0:
                                    while pagamento_total>=20 and cedula_20_reais>0:
                                        print("Estamos mandando uma cédula de 20 reais")
                                        pagamento_total -= 20
                                        cedula_20_reais-=1
                                    while pagamento_total>= 10 and cedula_10_reais>0:
                                        print("Estamos mandando uma cédula de 10 reais")
                                        pagamento_total -= 10
                                        cedula_10_reais-=1
                                    while pagamento_total>= 5 and cedula_5_reais>0:
                                        print("Estamos mandando uma cédula de 5 reais")
                                        pagamento_total -= 5
                                        cedula_5_reais-=1
                                    while pagamento_total>= 2 and cedula_2_reais>0:
                                        print("Estamos mandando uma cédula de 2 reais")
                                        pagamento_total -= 2
                                        cedula_2_reais-=1
                                    while pagamento_total >= 1 and moedas_1_real>0:
                                        print("Estamos mandando uma moeda de 1 real")
                                        pagamento_total -= 1
                                        moedas_1_real-=1
                                    while pagamento_total >= 0.5 and moedas_50_cent>0:
                                        print("Estamos mandando uma moeda de 50 centavos")
                                        pagamento_total -= 0.5
                                        moedas_50_cent-=1
                                    while pagamento_total >= 0.25 and moedas_25_cent>0:
                                        print("Estamos mandando uma moeda de 25 centavos")
                                        pagamento_total -= 0.25
                                        moedas_25_cent-=1
                                    if pagamento_total<=0.04:
                                        pagamento_total=0
                                    if pagamento_total!=0:  
                                        pagamento_total_possivel=1
                                    else:
                                        pagamento_total_possivel=0
                        break
    else:
        print('Selecione um valor válido!')
        continue