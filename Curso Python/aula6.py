while True: 
    valor_ingresso = float(input("Digite o valor do ingresso = "))
    numero_ingressos = int(input("Digite o número de ingressos = "))
    desconto = float(input("Digite seu desconto = "))
    valor_estacionamento = float(input("Digite o valor estacionamento = "))
    if desconto != 0:
        ingresso = (valor_ingresso*((desconto)/100)) * numero_ingressos
    else:
        ingresso = valor_ingresso * numero_ingressos
    preco = valor_ingresso * numero_ingressos + valor_estacionamento - ingresso
    print("Valor a pagar = ", preco)
    if preco>0:
        pagamento = float(input('Insira o valor a ser pago: '))
        if pagamento>preco:
            troco = pagamento-preco
            print('Muito obrigado por comprar com nossa equipe!')
            print('Estamos devolvendo seu troco!', troco, 'reais')
        elif pagamento==preco:
            print('Muito obrigado por comprar com nossa equipe!')
        else:
            print("Não podemos finalizar sua compra, voltando ao início!")
    else:
        print("Voltando ao início")
    continue
