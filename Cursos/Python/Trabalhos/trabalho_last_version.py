moedas_25_cent, moedas_50_cent, moedas_1_real, cedula_2_reais, cedula_5_reais, cedula_10_reais, cedula_20_reais, fim, pagamento = 0, 0, 0, 0, 0, 0, 0, 0, 0

telefone_pix, produtos_preco_quantidade, continuando_compra, telefone_pix = [], [], [], []

moedas_cedulas = [
    [moedas_25_cent, "moedas de 25 centavos", 0.25],
    [moedas_50_cent, "moedas de 50 centavos", 0.5],
    [moedas_1_real, "moedas de 1 real", 1],
    [cedula_2_reais, "cedulas de 2 reais", 2],
    [cedula_5_reais, "cedulas de 5 reais", 5],
    [cedula_10_reais, "cedulas de 10 reais", 10],
    [cedula_20_reais, "cedulas de 20 reais", 20]
]

def movimentacoes_pix():
    recibo_pix_total = 0
    for tp in telefone_pix:
        print(f'O telefone {tp[0]} realizou um pagamento de: R$ {tp[1]}')
        recibo_pix_total += tp[1]
    print(f'O pagamento total realizado foi de: R$ {recibo_pix_total}')

def verificar_possivel_pagamento():
    for quantidade in range(len(moedas_cedulas)):
        if trocado > moedas_cedulas[quantidade][0] * moedas_cedulas[quantidade][2]:
            return False
        else:
            return True

def troca_bebidas():
    for quantidade in range(quant_refri):
        print(f'[{quantidade+1}] {produtos_preco_quantidade[quantidade][0]} = R$ {produtos_preco_quantidade[quantidade][1]}')
    escolha_troca = int(input('Digite qual você deseja alterar: '))
    if escolha_troca in range(len([numeros[0] for numeros in produtos_preco_quantidade])+1):
        nome_produto = str(input('Digite o nome para o produto: '))
        quantidade_produto = int(input(f'Digite a quantidade para o/a {nome_produto}: '))
        preco_produto = float(input(f'Digite o preço do/da {nome_produto}: '))
        preco_produto = round(preco_produto, 2)
        produtos_preco_quantidade[escolha_troca-1][0] = nome_produto
        produtos_preco_quantidade[escolha_troca-1][1] = preco_produto
        produtos_preco_quantidade[escolha_troca-1][2] = quantidade_produto
    else:
        print('Escolha uma bebida válida!')

def mostrar_moedas_cedulas():
    for itens in moedas_cedulas:
        print(f'A quantidade de {itens[1]} são de {itens[0]}')

def quantidade_moedas_cedulas_adm():
    for itens in moedas_cedulas:
        itens[0] += int(input(f'Digite a quantidade para inserção de {itens[1]}: '))

def quantidade_moedas_cedulas_pagamento():

    global itens_depois_else
    global itens_depois
    global pagamento

    pagamento = 0
    itens_antes = 0
    itens_depois = 0

    for itens in moedas_cedulas:
        if itens[0] != 0:
            itens_antes = itens[0]
            itens[0] += int(input(f'Digite a quantidade de {itens[1]}: '))
            itens_depois = itens[0] - itens_antes
        else:
            itens[0] += int(input(f'Digite a quantidade de {itens[1]}: '))
            pagamento += itens[2] * itens[0]
            itens_depois_else = pagamento

        pagamento += itens[2] * itens_depois  # Adiciona o valor total de pagamento

def troco(pagamento, itens_depois, itens_depois_else):

    global trocado

    trocado = pagamento - produtos_preco_quantidade[selecao-1][1] # Soma o valor total do pagamento e subtrai do preço do produto
    
    if trocado >= 0 and verificar_possivel_pagamento() == True:
        print(f'Troco restante: R$ {trocado}')
        
        for itens in moedas_cedulas:
            if itens[0] > 0 and trocado >= itens[2]:
                quantidade_enviada = int(trocado // itens[2])
                
                if itens[0] >= quantidade_enviada:
                    print(f'Estamos enviando {quantidade_enviada} de {itens[1]}')
                    itens[0] -= quantidade_enviada
                    trocado -= itens[2] * quantidade_enviada
        
        if trocado <= 0.04:
            print('Muito obrigado por comprar conosco!')
        
        if produtos_preco_quantidade[selecao-1][2] >= 1:
            print(f'A quantidade atual desta bebida é de {produtos_preco_quantidade[selecao-1][2] - 1}')
            produtos_preco_quantidade[selecao-1][2] -= 1
    else:
        print('Infelizmente estamos sem troco')
        
        if pagamento > 0:
            print(f'Devolvendo o valor pago: R$ {pagamento}')
        
        for itens in moedas_cedulas:
            if itens[2] <= itens_depois and itens[0] > 0 or itens[2] <= itens_depois_else and itens[0] > 0:
                quantidade_devolvida = min(itens[0], itens_depois) if itens_depois > 0 else min(itens[0], itens_depois_else)
                print(f'Estamos devolvendo {quantidade_devolvida} de {itens[1]}')
                itens[0] -= quantidade_devolvida
                if itens_depois > 0:
                    itens_depois -= quantidade_devolvida
                else:
                    itens_depois_else -= quantidade_devolvida
    
    global fim
    fim = 1
    pagamento = 0


def realizar_compra():
    global somatoria_final
    global quantidade_selecionada
    global selecao
    global fim

    if fim == 1:
        for item in continuando_compra:
            item[1] = 0
        fim = 0  # Zera o valor de fim para permitir novas compras

    print('-=' * 30)
    print('Insira qual bebida você deseja comprar:')
    print('-=' * 30)

    for quantidade, produto in enumerate(produtos_preco_quantidade):
        print(f'[{quantidade + 1}] {produto[0]} = R$ {produto[1]}')

    selecao = int(input('Digite o número do refri para a compra: '))
    if selecao == 37:
        menu_adm()
    elif 1 <= selecao <= len(produtos_preco_quantidade):
        quantidade_selecionada = int(input('Digite a quantidade desejada para comprar: '))
        if quantidade_selecionada == 0:
            print('Digite uma quantidade válida!')
        elif produtos_preco_quantidade[selecao - 1][2] > quantidade_selecionada:
            encontrado = False
            for item in continuando_compra:
                if item[0] == produtos_preco_quantidade[selecao - 1][0]:
                    item[1] += quantidade_selecionada
                    encontrado = True
                    break
            if not encontrado:
                continuando_compra.append([produtos_preco_quantidade[selecao - 1][0], quantidade_selecionada])
            continuar_comprando = int(input('Digite [1] para continuar comprando ou [2] para ir ao pagamento: '))
            if continuar_comprando == 1:
                realizar_compra()
            elif continuar_comprando == 2:
                preco_para_pagar = []
                somatoria_final = 0

                for cont in continuando_compra:
                    for num in produtos_preco_quantidade:
                        if cont[0] == num[0]:
                            preco_para_pagar.append([cont[1], num[1]])

                for itens in preco_para_pagar:
                    somatoria_final += itens[0] * itens[1]

                print(f'O total a pagar é: R$ {somatoria_final}')
        else:
            print('Estamos sem estoque desta bebida!')
    else:
        print('Digite um valor válido!')


def menu_adm():
    print(f'-='*30,'\nOlá', nomeadm,'\n','-='*30)
    print("TEMOS EM ESTOQUE:")
    for bebidas in range(len([numeros[0] for numeros in produtos_preco_quantidade])):
        print(f"[{bebidas+1}]", produtos_preco_quantidade[bebidas][0],", quantidade = ", produtos_preco_quantidade[bebidas][2])
    print('Ou digite [0] caso não queira acrescentar nenhuma bebida')
    escolha = int(input('Digite qual bebida você deseja acrescentar: '))
    if 1 <= escolha <= len(produtos_preco_quantidade[0]) and escolha != 0:
        nova_quantidade = int(input('Digite quantas novas unidades você deseja acrescentar: '))
        produtos_preco_quantidade[escolha - 1][2] += nova_quantidade
        print(f'A nova quantidade de {produtos_preco_quantidade[escolha - 1][0]} é de: {produtos_preco_quantidade[escolha - 1][2]}')
    elif escolha == 0:
        menu_adm=int(input("OK, gostaria de realizar outra operação?\n[1] Ver saldo total de produtos\n[2] Ver lucro de todos os produtos\n[3] Adicionar troco\n[4] Consultar cachê\n[5] Alterar produtos e valores\n[6] Movimentações de PIX\n[7] Cancelar operação\nDigite sua escolha ao lado: "))
        if menu_adm == 1:
            quantidade_total = 0
            for quantidade in produtos_preco_quantidade[2]:
                quantidade_total += quantidade
            print('-='*30, '\nEsta máquina tem um total de:', quantidade_total, 'bebidas')
        elif menu_adm == 2:
            lucro_produtos = []
            sum_lucro_produtos = 0
            for lucro in range(len(produtos_preco_quantidade[0])):
                lucro_produtos.append([(quantidade_inicial-produtos_preco_quantidade[lucro][2])*produtos_preco_quantidade[lucro][1]])
            for lucro in range(len(lucro_produtos)):
                print(f'O lucro de {produtos_preco_quantidade[lucro][0]} foi de: R$ {lucro_produtos[lucro]}')
            for numbers in lucro_produtos:
                numbers = int(sum(numbers))
                sum_lucro_produtos += numbers
            print(f'O lucro total foi de {sum_lucro_produtos} reais')
        elif menu_adm == 3:
            quantidade_moedas_cedulas_adm()
        elif menu_adm == 4:
            mostrar_moedas_cedulas()
        elif menu_adm == 5:
            troca_bebidas()
        elif menu_adm == 6:
            movimentacoes_pix()
        elif menu_adm == 7:
            print('Saindo do modo administrador!')

def pix():
    pagamento_pix = 0
    telefone = int(input('Digite o número de seu telefone (DDD + 9 digitos): '))
    telefone_str = str(telefone)
    if len(telefone_str) == 11:
        print('Nossa chave pix é 987.349.859-76')
        print('Estamos no aguardo de seu pagamento!')
        pix_chave = True
        while pix_chave == True:
            confirmacao_pagamento = int(input('Digite:\n[1] Verificar pagamento\nDigite ao lado: '))
            if confirmacao_pagamento == 1:
                print('Muito obrigado por comprar conósco!')
                pagamento_pix = produtos_preco_quantidade[selecao-1][1]
                telefone_pix.append([telefone, pagamento_pix])
                produtos_preco_quantidade[selecao-1][2] -= quantidade_selecionada
                break
            else:
                print('Digite um valor válido!')
                continue
    else:
        print('Digite um número válido!')

def selecao_pagamento():
    try:
        if 1<= selecao <= len([numeros[0] for numeros in produtos_preco_quantidade]) and produtos_preco_quantidade[selecao - 1][2] >= quantidade_selecionada:
            tipo_pagamento = int(input('Digite:\n[1] Moedas e Cédulas\n[2] Pix\nDigite sua escolha ao lado: '))
            if tipo_pagamento == 1:
                quantidade_moedas_cedulas_pagamento()
                troco(pagamento, itens_depois, itens_depois_else)
            elif tipo_pagamento == 2:
                pix()
        elif selecao == 37:
            print('Tenha um excelente dia administrador!')
        elif produtos_preco_quantidade[selecao - 1][2] < quantidade_selecionada:
            print('Estamos sem estoque desta bebida!')
    except ValueError:
        print('Digite um número válido!')

nomeadm = input("Olá Administrador, digite seu nome: ")
nomemaquina = input("Digite o nome ao qual você deseja que a máquina tenha: ")
quant_refri = int(input('Digite a quantidade de refri que você deseja que tenha: '))

for quantidade in range(quant_refri):
    nome_produto = input(f'Digite o nome da bebida {quantidade + 1}: ')
    preco_produto = float(input(f'Digite o preço desejado em reais para a bebida: '))
    quantidade_produto = int(input(f'Digite a quantidade desejada da bebida: '))
    quantidade_inicial = quantidade_produto
    produtos_preco_quantidade.append([nome_produto, preco_produto, quantidade_produto])

while True:
    realizar_compra()
    selecao_pagamento()