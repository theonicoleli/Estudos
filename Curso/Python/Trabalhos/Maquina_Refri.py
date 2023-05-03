troco_possivel=0
moedas5cent=0
moedas10cent=0
moedas25cent=0
moedas50cent=0
moedas1real=0
moedasiniciais5cent=0
moedasiniciais10cent=0
moedasiniciais25cent=0
moedasiniciais50cent=0
moedasiniciais1real=0
cedula2reais=0
cedula5reais=0
cedula10reais=0
cedula20reais=0
cedula50reais=0
cedula100reais=0
cedula200reais=0
cedulainiciais2reais=0
cedulainiciais5reais=0
cedulainiciais10reais=0
cedulainiciais20reais=0
cedulainiciais50reais=0
cedulainiciais100reais=0
cedulainiciais200reais=0
addmoedas5cent=0
addmoedas10cent=0
addmoedas25cent=0
addmoedas50cent=0
addmoedas1real=0
addcedula2reais=0
addcedula5reais=0
addcedula10reais=0
addcedula20reais=0
addcedula50reais=0
addcedula100reais=0
addcedula200reais=0
insmoedas5cent=0
insmoedas10cent=0
insmoedas25cent=0
insmoedas50cent=0
insmoedas1real=0
inscedula2reais=0
inscedula5reais=0
inscedula10reais=0
inscedula20reais=0
inscedula50reais=0
inscedula100reais=0
inscedula200reais=0
nomeadm = str(input("Olá Administrador, digite seu nome: "))
nomemaquina = str(input("Digite o nome ao qual você deseja que a máquina tenha: "))
addmarcasrefri=int(input("Gostaria de adicionar marcas de bebidas?[1 para SIM e 2 para NÃO] "))
if addmarcasrefri==1:
    quantidaderefri=int(input("Gostaria de adicionar quantas nova marcas de bebidas?(no máx 5) "))
    print('-------------------------------------------------------')
    if quantidaderefri==1:
        nomerefri1=str(input("Digite o nome da bebida: "))
        quantidaderefri1=int(input("Quantas unidades: "))
        precorefri1=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        quantidadeinicialrefri1=quantidaderefri1
        precoinicialrefri1=precorefri1
    elif quantidaderefri==2:
        nomerefri1=str(input("Digite o nome da bebida: "))
        quantidaderefri1=int(input("Quantas unidades: "))
        precorefri1=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri2=str(input("Digite o nome da bebida: "))
        quantidaderefri2=int(input("Quantas unidades: "))
        precorefri2=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        quantidadeinicialrefri1=quantidaderefri1
        quantidadeinicialrefri2=quantidaderefri2
        precoinicialrefri1=precorefri1
        precoinicialrefri2=precorefri2
    elif quantidaderefri==3:
        nomerefri1=str(input("Digite o nome da bebida: "))
        quantidaderefri1=int(input("Quantas unidades: "))
        precorefri1=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri2=str(input("Digite o nome da bebida: "))
        quantidaderefri2=int(input("Quantas unidades: "))
        precorefri2=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri3=str(input("Digite o nome da bebida: "))
        quantidaderefri3=int(input("Quantas unidades: "))
        precorefri3=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        quantidadeinicialrefri1=quantidaderefri1
        quantidadeinicialrefri2=quantidaderefri2
        quantidadeinicialrefri3=quantidaderefri3
        precoinicialrefri1=precorefri1
        precoinicialrefri2=precorefri2
        precoinicialrefri3=precorefri3
    elif quantidaderefri==4:
        nomerefri1=str(input("Digite o nome da bebida: "))
        quantidaderefri1=int(input("Quantas unidades: "))
        precorefri1=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri2=str(input("Digite o nome da bebida: "))
        quantidaderefri2=int(input("Quantas unidades: "))
        precorefri2=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri3=str(input("Digite o nome da bebida: "))
        quantidaderefri3=int(input("Quantas unidades: "))
        precorefri3=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri4=str(input("Digite o nome da bebida: "))
        quantidaderefri4=int(input("Quantas unidades: "))
        precorefri4=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        quantidadeinicialrefri1=quantidaderefri1
        quantidadeinicialrefri2=quantidaderefri2
        quantidadeinicialrefri3=quantidaderefri3
        quantidadeinicialrefri4=quantidaderefri4
        precoinicialrefri1=precorefri1
        precoinicialrefri2=precorefri2
        precoinicialrefri3=precorefri3
        precoinicialrefri4=precorefri4
    elif quantidaderefri==5:
        nomerefri1=str(input("Digite o nome da bebida: "))
        quantidaderefri1=int(input("Quantas unidades: "))
        precorefri1=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri2=str(input("Digite o nome da bebida: "))
        quantidaderefri2=int(input("Quantas unidades: "))
        precorefri2=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri3=str(input("Digite o nome da bebida: "))
        quantidaderefri3=int(input("Quantas unidades: "))
        precorefri3=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri4=str(input("Digite o nome da bebida: "))
        quantidaderefri4=int(input("Quantas unidades: "))
        precorefri4=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        nomerefri5=str(input("Digite o nome da bebida: "))
        quantidaderefri5=int(input("Quantas unidades: "))
        precorefri5=float(input("Digite o preço ao qual você deseja: R$"))
        print('-------------------------------------------------------')
        quantidadeinicialrefri1=quantidaderefri1
        quantidadeinicialrefri2=quantidaderefri2
        quantidadeinicialrefri3=quantidaderefri3
        quantidadeinicialrefri4=quantidaderefri4
        quantidadeinicialrefri5=quantidaderefri5
        precoinicialrefri1=precorefri1
        precoinicialrefri2=precorefri2
        precoinicialrefri3=precorefri3
        precoinicialrefri4=precorefri4
        precoinicialrefri5=precorefri5
    if (1<=quantidaderefri<=5):
        inserindomoedas=int(input("Gostaria de adicionar troco? [1 para SIM ou 2 para Não]"))
        if inserindomoedas==1:
            print('-------------------------------------------------------')
            print("Insira as moedas!")
            print('-------------------------------------------------------')
            insmoedas5cent=int(input('Quantidade de moedas de 5 centavos:'))
            insmoedas10cent=int(input('Quantidade de moedas de 10 centavos:'))
            insmoedas25cent=int(input('Quantidade de moedas de 25 centavos:'))
            insmoedas50cent=int(input('Quantidade de moedas de 50 centavos:'))
            insmoedas1real=int(input('Quantidade de moedas de 1 real:'))
            insmoedas=insmoedas5cent+insmoedas10cent+insmoedas25cent+insmoedas50cent+insmoedas1real
            print('-------------------------------------------------------')
            print("Agora insira as cédulas!")
            print('-------------------------------------------------------')
            inscedula2reais=int(input('Quantidade de cédulas de 2 reais:'))
            inscedula5reais=int(input('Quantidade de cédulas de 5 reais:'))
            inscedula10reais=int(input('Quantidade de cédulas de 10 reais:'))
            inscedula20reais=int(input('Quantidade de cédulas de 20 reais:'))
            inscedula50reais=int(input('Quantidade de cédulas de 50 reais:'))
            inscedula100reais=int(input('Quantidade de cédulas de 100 reais:'))
            inscedula200reais=int(input('Quantidade de cédulas de 200 reais:'))
            inscedulas=inscedula2reais+inscedula5reais+inscedula10reais+inscedula20reais+inscedula50reais+inscedula100reais+inscedula200reais
        elif inserindomoedas==2:
            print("Ok! Será apenas aceito as compras com o valor inteiro, pois não haverá troco.")
        else:
            print("Escolha um número válido!")
    else:
        print("Máquina Processando!")

else:
    print("Não temos mais utilidade por aqui!")
while True:
    totaladdmoedas5cent=insmoedas5cent+addmoedas5cent
    totaladdmoedas10cent=insmoedas10cent+addmoedas10cent
    totaladdmoedas25cent=insmoedas25cent+addmoedas25cent
    totaladdmoedas50cent=insmoedas50cent+addmoedas50cent
    totaladdmoedas1real=insmoedas1real+addmoedas1real
    totaladdcedula2reais=inscedula2reais+addcedula2reais
    totaladdcedula5reais=inscedula5reais+addcedula5reais
    totaladdcedula10reais=inscedula10reais+addcedula10reais
    totaladdcedula20reais=inscedula20reais+addcedula20reais
    totaladdcedula50reais=inscedula50reais+addcedula50reais
    totaladdcedula100reais=inscedula100reais+addcedula100reais
    totaladdcedula200reais=inscedula200reais+addcedula200reais
    totaladdmoedas=totaladdmoedas5cent+totaladdmoedas10cent+totaladdmoedas25cent+totaladdmoedas50cent+totaladdmoedas1real
    totaladdcedula=totaladdcedula2reais+totaladdcedula5reais+totaladdcedula10reais+totaladdcedula20reais+totaladdcedula50reais+totaladdcedula100reais+totaladdcedula200reais
    if addmarcasrefri!=1 or quantidaderefri<1 or quantidaderefri>5:
        print("Reinicie a máquina para que possamos vender suas bebidas!")
        break
    else:
        print('-------------------------------------------------------')
        print(nomemaquina)
        if quantidaderefri==1:
            print("Insira qual bebida você deseja comprar:")
            print("[1]", nomerefri1," = R$", precorefri1)
        elif quantidaderefri==2:
            print("Insira qual bebida você deseja comprar:")
            print("[1]", nomerefri1," = R$", precorefri1)
            print("[2]", nomerefri2," = R$", precorefri2)
        elif quantidaderefri==3:
            print("Insira qual bebida você deseja comprar:")
            print("[1]", nomerefri1," = R$", precorefri1)
            print("[2]", nomerefri2," = R$", precorefri2)
            print("[3]", nomerefri3," = R$", precorefri3)
        elif quantidaderefri==4:
            print("Insira qual bebida você deseja comprar:")
            print("[1]", nomerefri1," = R$", precorefri1)
            print("[2]", nomerefri2," = R$", precorefri2)
            print("[3]", nomerefri3," = R$", precorefri3)
            print("[4]", nomerefri4," = R$", precorefri4)
        elif quantidaderefri==5:
            print("Insira qual bebida você deseja comprar:")
            print("[1]", nomerefri1," = R$", precorefri1)
            print("[2]", nomerefri2," = R$", precorefri2)
            print("[3]", nomerefri3," = R$", precorefri3)
            print("[4]", nomerefri4," = R$", precorefri4)
            print("[5]", nomerefri5," = R$", precorefri5)
        refri=int(input("Coloque o número da bebida ao lado: "))
        if refri==37:
            print('-------------------------------------------------------')
            print("OLÁ,", nomeadm)
            print('-------------------------------------------------------')
            if quantidaderefri==1:
                print("TEMOS EM ESTOQUE:")
                print("[1]",nomerefri1, "quantidade = ", quantidaderefri1)
            elif quantidaderefri==2:
                print("TEMOS EM ESTOQUE:")
                print("[1]",nomerefri1, "quantidade = ", quantidaderefri1)
                print("[2]",nomerefri2, "quantidade = ", quantidaderefri2)  
            elif quantidaderefri==3:
                print("TEMOS EM ESTOQUE:")
                print("[1]",nomerefri1, "quantidade = ", quantidaderefri1)
                print("[2]",nomerefri2, "quantidade = ", quantidaderefri2)
                print("[3]",nomerefri3, "quantidade = ", quantidaderefri3)
            elif quantidaderefri==4:
                print("TEMOS EM ESTOQUE:")
                print("[1]",nomerefri1, "quantidade = ", quantidaderefri1)
                print("[2]",nomerefri2, "quantidade = ", quantidaderefri2)
                print("[3]",nomerefri3, "quantidade = ", quantidaderefri3)
                print("[4]",nomerefri4, "quantidade = ", quantidaderefri4)
            elif quantidaderefri==5:
                print("TEMOS EM ESTOQUE:")
                print("[1]",nomerefri1, "quantidade = ", quantidaderefri1)
                print("[2]",nomerefri2, "quantidade = ", quantidaderefri2)
                print("[3]",nomerefri3, "quantidade = ", quantidaderefri3)
                print("[4]",nomerefri4, "quantidade = ", quantidaderefri4)
                print("[5]",nomerefri5, "quantidade = ", quantidaderefri5)
            produtos=int(input("Gostaria de acrescentar ou retirar bebidas? [Usar 1 para Sim ou 2 para Não] "))
            print('-------------------------------------------------------')
            if produtos == 2:
                print("OK, gostaria de realizar outra operação?")
                print("[1] Ver saldo total de produtos")
                print("[2] Ver lucro de todos os produtos")
                print("[3] Adicionar troco")
                print("[4] Consultar cachê")
                print("[5] Alterar produtos e valores")
                print("[6] Cancelar operação")
                menu_adm=int(input("Digite sua escolha ao lado: "))
                if menu_adm==1:
                    if quantidaderefri==1:
                        saldototaldeprodutos=quantidaderefri1
                    elif quantidaderefri==2:
                        saldototaldeprodutos=quantidaderefri1+quantidaderefri2
                    elif quantidaderefri==3:
                        saldototaldeprodutos=quantidaderefri1+quantidaderefri2+quantidaderefri3
                    elif quantidaderefri==4:
                        saldototaldeprodutos=quantidaderefri1+quantidaderefri2+quantidaderefri3+quantidaderefri4
                    elif quantidaderefri==5:
                        saldototaldeprodutos=quantidaderefri1+quantidaderefri2+quantidaderefri3+quantidaderefri4+quantidaderefri5
                    print('-------------------------------------------------------')
                    print("Esta máquina tem um total de", saldototaldeprodutos,"bebidas")
                elif menu_adm==2:
                    print('-------------------------------------------------------')
                    lucrorefri1= (quantidadeinicialrefri1-quantidaderefri1)*precorefri1
                    if quantidaderefri==1:
                        if lucrorefri1>=0:
                            print("O dinheiro ganho com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        else:
                            print("O dinheiro perdido com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        lucrototal= (lucrorefri1)
                        if lucrototal>=0:
                            print("O dinheiro ganho no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                        else:
                            print("O dinheiro perdido no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                    elif quantidaderefri==2:
                        if lucrorefri1>=0:
                            print("O dinheiro ganho com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        else:
                            print("O dinheiro perdido com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        lucrorefri2= (quantidadeinicialrefri2-quantidaderefri2)*precorefri2
                        if lucrorefri2>=0:
                            print("O dinheiro ganho com [2]", nomerefri2, ":" , lucrorefri2,"reais") 
                        else:
                            print("O dinheiro perdido com [2]", nomerefri2, ":" , lucrorefri2,"reais")
                        lucrototal= (lucrorefri1+lucrorefri2)
                        if lucrototal>=0:
                            print("O dinheiro ganho no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                        else:
                            print("O dinheiro perdido no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                    elif quantidaderefri==3:
                        if lucrorefri1>=0:
                            print("O dinheiro ganho com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        else:
                            print("O dinheiro perdido com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        lucrorefri2= (quantidadeinicialrefri2-quantidaderefri2)*precorefri2
                        if lucrorefri2>=0:
                            print("O dinheiro ganho com [2]", nomerefri2, ":" , lucrorefri2,"reais") 
                        else:
                            print("O dinheiro perdido com [2]", nomerefri2, ":" , lucrorefri2,"reais")
                        lucrorefri3= (quantidadeinicialrefri3-quantidaderefri3)*precorefri3
                        if lucrorefri3>=0:
                            print("O dinheiro ganho com [3]", nomerefri3, ":" , lucrorefri3,"reais") 
                        else:
                            print("O dinheiro perdido com [3]", nomerefri3, ":" , lucrorefri3,"reais")
                        lucrototal= (lucrorefri1+lucrorefri2+lucrorefri3)
                        if lucrototal>=0:
                            print("O dinheiro ganho no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                        else:
                            print("O dinheiro perdido no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                    elif quantidaderefri==4:
                        if lucrorefri1>=0:
                            print("O dinheiro ganho com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        else:
                            print("O dinheiro perdido com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        lucrorefri2= (quantidadeinicialrefri2-quantidaderefri2)*precorefri2
                        if lucrorefri2>=0:
                            print("O dinheiro ganho com [2]", nomerefri2, ":" , lucrorefri2,"reais") 
                        else:
                            print("O dinheiro perdido com [2]", nomerefri2, ":" , lucrorefri2,"reais")
                        lucrorefri3= (quantidadeinicialrefri3-quantidaderefri3)*precorefri3
                        if lucrorefri3>=0:
                            print("O dinheiro ganho com [3]", nomerefri3, ":" , lucrorefri3,"reais") 
                        else:
                            print("O dinheiro perdido com [3]", nomerefri3, ":" , lucrorefri3,"reais")
                        lucrorefri4= (quantidadeinicialrefri4-quantidaderefri4)*precorefri4
                        if lucrorefri4>=0:
                            print("O dinheiro ganho com [4]", nomerefri4, ":" , lucrorefri4,"reais")
                        else:
                            print("O dinheiro perdido com [4]", nomerefri4, ":" , lucrorefri4,"reais")
                        lucrototal= (lucrorefri1+lucrorefri2+lucrorefri3+lucrorefri4)
                        if lucrototal>=0:
                            print("O dinheiro ganho no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                        else:
                            print("O dinheiro perdido no total de todas as bebidas juntos foi de: ", lucrototal,"reais")  
                    elif quantidaderefri==5:
                        if lucrorefri1>=0:
                            print("O dinheiro ganho com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        else:
                            print("O dinheiro perdido com [1]", nomerefri1, ":" , lucrorefri1,"reais") 
                        lucrorefri2= (quantidadeinicialrefri2-quantidaderefri2)*precorefri2
                        if lucrorefri2>=0:
                            print("O dinheiro ganho com [2]", nomerefri2, ":" , lucrorefri2,"reais") 
                        else:
                            print("O dinheiro perdido com [2]", nomerefri2, ":" , lucrorefri2,"reais")
                        lucrorefri3= (quantidadeinicialrefri3-quantidaderefri3)*precorefri3
                        if lucrorefri3>=0:
                            print("O dinheiro ganho com [3]", nomerefri3, ":" , lucrorefri3,"reais") 
                        else:
                            print("O dinheiro perdido com [3]", nomerefri3, ":" , lucrorefri3,"reais")
                        lucrorefri4= (quantidadeinicialrefri4-quantidaderefri4)*precorefri4
                        if lucrorefri4>=0:
                            print("O dinheiro ganho com [4]", nomerefri4, ":" , lucrorefri4,"reais")
                        else:
                            print("O dinheiro perdido com [4]", nomerefri4, ":" , lucrorefri4,"reais")
                        lucrorefri5= (quantidadeinicialrefri5-quantidaderefri5)*precorefri5
                        if lucrorefri5>=0:
                            print("O dinheiro ganho com [5]", nomerefri4, ":" , lucrorefri4,"reais")
                        else:
                            print("O dinheiro perdido com [5]", nomerefri5, ":" , lucrorefri5,"reais")
                        lucrototal= (lucrorefri1+lucrorefri2+lucrorefri3+lucrorefri4+lucrorefri5)
                        if lucrototal>=0:
                            print("O dinheiro ganho no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                        else:
                            print("O dinheiro perdido no total de todas as bebidas juntos foi de: ", lucrototal,"reais") 
                elif menu_adm == 3:
                    print('-------------------------------------------------------')
                    print("Insira as moedas!")
                    print('-------------------------------------------------------')
                    addmoedas5cent=int(input('Quantidade de moedas de 5 centavos:'))
                    addmoedas10cent=int(input('Quantidade de moedas de 10 centavos:'))
                    addmoedas25cent=int(input('Quantidade de moedas de 25 centavos:'))
                    addmoedas50cent=int(input('Quantidade de moedas de 50 centavos:'))
                    addmoedas1real=int(input('Quantidade de moedas de 1 real:'))
                    addmoedas=addmoedas5cent+addmoedas10cent+addmoedas25cent+addmoedas50cent+addmoedas1real
                    print('-------------------------------------------------------')
                    print("Agora insira as cédulas!")
                    print('-------------------------------------------------------')
                    addcedula2reais=int(input('Quantidade de cédulas de 2 reais:'))
                    addcedula5reais=int(input('Quantidade de cédulas de 5 reais:'))
                    addcedula10reais=int(input('Quantidade de cédulas de 10 reais:'))
                    addcedula20reais=int(input('Quantidade de cédulas de 20 reais:'))
                    addcedula50reais=int(input('Quantidade de cédulas de 50 reais:'))
                    addcedula100reais=int(input('Quantidade de cédulas de 100 reais:'))
                    addcedula200reais=int(input('Quantidade de cédulas de 200 reais:'))
                    addcedulas=addcedula2reais+addcedula5reais+addcedula10reais+addcedula20reais+addcedula50reais+addcedula100reais+addcedula200reais
                elif menu_adm==4:
                    totalmoedas5cent=addmoedas5cent+moedasiniciais5cent+insmoedas5cent
                    totalmoedas10cent=addmoedas10cent+moedasiniciais10cent+insmoedas10cent
                    totalmoedas25cent=addmoedas25cent+moedasiniciais25cent+insmoedas25cent
                    totalmoedas50cent=addmoedas50cent+moedasiniciais50cent+insmoedas50cent
                    totalmoedas1real=addmoedas1real+moedasiniciais1real+insmoedas1real
                    totalmoedas=totalmoedas5cent+totalmoedas10cent+totalmoedas25cent+totalmoedas50cent+totalmoedas1real
                    totalcedula2reais=addcedula2reais+cedulainiciais2reais+inscedula2reais
                    totalcedula5reais=addcedula5reais+cedulainiciais5reais+inscedula5reais
                    totalcedula10reais=addcedula10reais+cedulainiciais10reais+inscedula10reais
                    totalcedula20reais=addcedula20reais+cedulainiciais20reais+inscedula20reais
                    totalcedula50reais=addcedula50reais+cedulainiciais50reais+inscedula50reais
                    totalcedula100reais=addcedula100reais+cedulainiciais100reais+inscedula100reais
                    totalcedula200reais=addcedula200reais+cedulainiciais200reais+inscedula200reais
                    totalcedulas=totalcedula2reais+totalcedula5reais+totalcedula10reais+totalcedula20reais+totalcedula50reais+totalcedula100reais+totalcedula200reais            
                    print('-------------------------------------------------------')
                    print("A quantidade de moedas:")
                    print('-------------------------------------------------------')
                    print("A quantidade de moedas de 5 centavos são de:", totalmoedas5cent)
                    print("A quantidade de moedas de 10 centavos são de:", totalmoedas10cent)
                    print("A quantidade de moedas de 25 centavos são de:", totalmoedas25cent)
                    print("A quantidade de moedas de 50 centavos são de:", totalmoedas50cent)
                    print("A quantidade de moedas de 1 real são de:", totalmoedas1real)
                    print('-------------------------------------------------------')
                    print("A quantidade de cédulas:")
                    print('-------------------------------------------------------')
                    print("A quantidade de cédulas de 2 reais são de:", totalcedula2reais)
                    print("A quantidade de cédulas de 5 reais são de:", totalcedula5reais)
                    print("A quantidade de cédulas de 10 reais são de:", totalcedula10reais)
                    print("A quantidade de cédulas de 20 reais são de:", totalcedula20reais)
                    print("A quantidade de cédulas de 50 reais são de:", totalcedula50reais)
                    print("A quantidade de cédulas de 100 reais são de:", totalcedula100reais)
                    print("A quantidade de cédulas de 200 reais são de:", totalcedula200reais)  
                elif menu_adm==5:
                    if quantidaderefri==1:
                        print('Insira qual refri você deseja alterar:')
                        print('[1] ', nomerefri1 ,'= R$', precorefri1)
                        refrimudanca=int(input('Coloque o número do refri ao lado:'))
                        if refrimudanca==1:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri1+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri1=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri1=float(input('Insira o novo preço de '+nomerefri1+': '))
                                print('-------------------------------------------------------')   
                        else:
                            print("Selecione um número válido!")
                    elif quantidaderefri==2:
                        print('Insira qual refri você deseja alterar:')
                        print('[1] ', nomerefri1 ,'= R$', precorefri1)
                        print('[2] ', nomerefri2 ,'= R$', precorefri2)
                        refrimudanca=int(input('Coloque o número do refri ao lado:'))
                        if refrimudanca==1:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri1+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri1=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri1=float(input('Insira o novo preço de '+nomerefri1+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==2:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri2+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri2=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri2=float(input('Insira o novo preço de '+nomerefri2+': '))
                                print('-------------------------------------------------------')    
                        else:
                            print("Selecione um número válido!")   
                    elif quantidaderefri==3:
                        print('Insira qual refri você deseja alterar:')
                        print('[1] ', nomerefri1 ,'= R$', precorefri1)
                        print('[2] ', nomerefri2 ,'= R$', precorefri2)
                        print('[3] ', nomerefri3 ,'= R$', precorefri3)
                        refrimudanca=int(input('Coloque o número do refri ao lado:'))
                        if refrimudanca==1:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri1+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri1=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri1=float(input('Insira o novo preço de '+nomerefri1+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==2:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri2+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri2=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri2=float(input('Insira o novo preço de '+nomerefri2+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==3:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri3+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri3=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri3=float(input('Insira o novo preço de '+nomerefri3+': '))
                                print('-------------------------------------------------------')  
                        else:
                            print("Selecione um número válido!")   
                    elif quantidaderefri==4:
                        print('Insira qual refri você deseja alterar:')
                        print('[1] ', nomerefri1 ,'= R$', precorefri1)
                        print('[2] ', nomerefri2 ,'= R$', precorefri2)
                        print('[3] ', nomerefri3 ,'= R$', precorefri3)
                        print('[4] ', nomerefri4 ,'= R$', precorefri4)
                        refrimudanca=int(input('Coloque o número do refri ao lado:'))
                        if refrimudanca==1:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri1+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri1=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri1=float(input('Insira o novo preço de '+nomerefri1+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==2:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri2+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri2=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri2=float(input('Insira o novo preço de '+nomerefri2+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==3:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri3+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri3=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri3=float(input('Insira o novo preço de '+nomerefri3+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==4:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri4+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri4=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri4=float(input('Insira o novo preço de '+nomerefri4+': '))
                                print('-------------------------------------------------------')  
                        else:
                            print("Selecione um número válido!")   
                    elif quantidaderefri==5:
                        print('Insira qual refri você deseja alterar:')
                        print('[1] ', nomerefri1 ,'= R$', precorefri1)
                        print('[2] ', nomerefri2 ,'= R$', precorefri2)
                        print('[3] ', nomerefri3 ,'= R$', precorefri3)
                        print('[4] ', nomerefri4 ,'= R$', precorefri4)
                        print('[5] ', nomerefri5 ,'= R$', precorefri5)
                        refrimudanca=int(input('Coloque o número do refri ao lado:'))
                        if refrimudanca==1:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri1+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri1=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri1=float(input('Insira o novo preço de '+nomerefri1+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==2:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri2+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri2=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri2=float(input('Insira o novo preço de '+nomerefri2+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==3:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri3+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri3=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri3=float(input('Insira o novo preço de '+nomerefri3+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==4:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri4+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri4=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri4=float(input('Insira o novo preço de '+nomerefri4+': '))
                                print('-------------------------------------------------------') 
                        elif refrimudanca==5:
                            nomeoupreco=int(input('Deseja alterar o nome ou o preço de '+nomerefri5+' ? [Usar 1 para nome ou 2 para preço]:'))
                            if nomeoupreco==1:
                                nomerefri5=str(input('Insira o nome do novo produto:'))
                                print('-------------------------------------------------------') 
                            if nomeoupreco==2:
                                precorefri5=float(input('Insira o novo preço de '+nomerefri5+': '))
                                print('-------------------------------------------------------')  
                        else:
                            print("Selecione um número válido!")       
                elif menu_adm==6:
                    print("Um excelente dia Administrador!")
            elif produtos==1:       
                if produtos == 1 and quantidaderefri==1:
                    print("[1]", nomerefri1," = R$", precorefri1)
                elif produtos == 1 and quantidaderefri==2:
                    print("[1]", nomerefri1," = R$", precorefri1)
                    print("[2]", nomerefri2," = R$", precorefri2)
                elif produtos == 1 and quantidaderefri==3:
                    print("[1]", nomerefri1," = R$", precorefri1)
                    print("[2]", nomerefri2," = R$", precorefri2)
                    print("[3]", nomerefri3," = R$", precorefri3)
                elif produtos == 1 and quantidaderefri==4:
                    print("[1]", nomerefri1," = R$", precorefri1)
                    print("[2]", nomerefri2," = R$", precorefri2)
                    print("[3]", nomerefri3," = R$", precorefri3)
                    print("[4]", nomerefri4," = R$", precorefri4)
                elif produtos == 1 and quantidaderefri==4:
                    print("[1]", nomerefri1," = R$", precorefri1)
                    print("[2]", nomerefri2," = R$", precorefri2)
                    print("[3]", nomerefri3," = R$", precorefri3)
                    print("[4]", nomerefri4," = R$", precorefri4)
                    print("[5]", nomerefri5," = R$", precorefri5)
                nova_selecao=int(input("Coloque o número da bebida que deseja reestocar ou retirar: "))                                   
                if nova_selecao==1 and (5 >= quantidaderefri >= 1):
                    nova_quantidade=int(input("Digite quantas novas unidades você deseja acrescentar ou retirar: "))
                    print('-------------------------------------------------------')
                    quantidaderefri1=quantidaderefri1+nova_quantidade
                    print("O novo estoque de:")
                    print("[1]", nomerefri1) 
                    print("São de: ", quantidaderefri1,"unidades")
                elif nova_selecao==2 and (5 >= quantidaderefri >= 2):
                    nova_quantidade=int(input("Digite quantas novas unidades você deseja acrescentar ou retirar: "))
                    print('-------------------------------------------------------')
                    quantidaderefri2=quantidaderefri2+nova_quantidade
                    print("O novo estoque de:")
                    print("[2]", nomerefri2) 
                    print("São de: ", quantidaderefri2,"unidades")
                elif nova_selecao==3 and (5 >= quantidaderefri >= 3):
                    nova_quantidade=int(input("Digite quantas novas unidades você deseja acrescentar ou retirar: "))
                    print('-------------------------------------------------------')
                    quantidaderefri3=quantidaderefri3+nova_quantidade
                    print("O novo estoque de:")
                    print("[3]", nomerefri3) 
                    print("São de: ", quantidaderefri3,"unidades")
                elif nova_selecao==4 and (5 >= quantidaderefri >= 4):
                    nova_quantidade=int(input("Digite quantas novas unidades você deseja acrescentar ou retirar: "))
                    print('-------------------------------------------------------')
                    quantidaderefri4=quantidaderefri4+nova_quantidade
                    print("O novo estoque de:")
                    print("[4]", nomerefri4) 
                    print("São de: ", quantidaderefri4,"unidades")
                elif nova_selecao==5 and quantidaderefri == 5:
                    nova_quantidade=int(input("Digite quantas novas unidades você deseja acrescentar ou retirar: "))
                    print('-------------------------------------------------------')
                    quantidaderefri5=quantidaderefri5+nova_quantidade
                    print("O novo estoque de:")
                    print("[5]", nomerefri5) 
                    print("São de: ", quantidaderefri5,"unidades")
        elif refri >= 1 and refri <= 5:
            if refri == 1 and quantidaderefri >= 1 and quantidaderefri <= 5 and quantidaderefri1 > 0:
                valor = precorefri1
            elif refri == 2 and quantidaderefri >= 2 and quantidaderefri <= 5 and quantidaderefri2 > 0:
                valor = precorefri2
            elif refri == 3 and quantidaderefri >= 3 and quantidaderefri <= 5 and quantidaderefri3 > 0:
                valor = precorefri3
            elif refri == 4 and quantidaderefri == 5 and quantidaderefri4 > 0:
                valor = precorefri4
            elif refri == 5 and quantidaderefri == 5 and quantidaderefri5 > 0:
                valor = precorefri5
            else:
                if quantidaderefri == 1 and (quantidaderefri1 <= 0):
                    print('-------------------------------------------------------')
                    print("Estamos sem estoque desta bebida") 
                elif quantidaderefri == 2 and (quantidaderefri1 <= 0 or quantidaderefri2 <= 0):
                    print('-------------------------------------------------------')
                    print("Estamos sem estoque desta bebida")
                elif quantidaderefri == 3 and (quantidaderefri1 <= 0 or quantidaderefri2 <= 0 or quantidaderefri3 <= 0):
                    print('-------------------------------------------------------')
                    print("Estamos sem estoque desta bebida")
                elif quantidaderefri == 4 and (quantidaderefri1 <= 0 or quantidaderefri2 <= 0 or quantidaderefri3 <= 0 or quantidaderefri4 <= 0):
                    print('-------------------------------------------------------')
                    print("Estamos sem estoque desta bebida")
                elif quantidaderefri == 5 and (quantidaderefri1 <= 0 or quantidaderefri2 <= 0 or quantidaderefri3 <= 0 or quantidaderefri4 <= 0 or quantidaderefri5 <= 0):
                    print('-------------------------------------------------------')
                    print("Estamos sem estoque desta bebida")
                elif quantidaderefri==1 and (refri<=2 or refri>=0):
                    print('-------------------------------------------------------')
                    print("Escolha um número válido!")
                elif quantidaderefri==2 and (refri<=3 or refri>=0):
                    print('-------------------------------------------------------')
                    print("Escolha um número válido!")
                elif quantidaderefri==3 and (refri<=4 or refri>=0):
                    print('-------------------------------------------------------')
                    print("Escolha um número válido!")
                elif quantidaderefri==4 and (refri<=5 or refri>=0):
                    print('-------------------------------------------------------')
                    print("Escolha um número válido!")
                elif quantidaderefri==5 and (refri>=0):
                    print('-------------------------------------------------------')
                    print("Escolha um número válido!")
                continue
            print('-------------------------------------------------------')
            print("O custo a ser pago é de", valor,"reais")
            print('-------------------------------------------------------')
            print("Você deseja realizar o pagamento de qual forma:")
            print("[1] Moedas")
            print("[2] Cédulas")
            print("[3] Moedas e Cédulas")
            pagamento=int(input("Insira a forma a qual você deseja comprar ao lado: "))
            print('-------------------------------------------------------')
            totalmoedas5cent=addmoedas5cent+moedasiniciais5cent+insmoedas5cent+moedas5cent
            totalmoedas10cent=addmoedas10cent+moedasiniciais10cent+insmoedas10cent+moedas10cent
            totalmoedas25cent=addmoedas25cent+moedasiniciais25cent+insmoedas25cent+moedas25cent
            totalmoedas50cent=addmoedas50cent+moedasiniciais50cent+insmoedas50cent+moedas50cent
            totalmoedas1real=addmoedas1real+moedasiniciais1real+insmoedas1real+moedas1real
            totalmoedas=totalmoedas5cent+totalmoedas10cent+totalmoedas25cent+totalmoedas1real
            totalcedula2reais=addcedula2reais+cedulainiciais2reais+inscedula2reais+cedula2reais
            totalcedula5reais=addcedula5reais+cedulainiciais5reais+inscedula5reais+cedula5reais
            totalcedula10reais=addcedula10reais+cedulainiciais10reais+inscedula10reais+cedula10reais
            totalcedula20reais=addcedula20reais+cedulainiciais20reais+inscedula20reais+cedula20reais
            totalcedula50reais=addcedula50reais+cedulainiciais50reais+inscedula50reais+cedula50reais
            totalcedula100reais=addcedula100reais+cedulainiciais100reais+inscedula100reais+cedula100reais
            totalcedula200reais=addcedula200reais+cedulainiciais200reais+inscedula200reais+cedula200reais 
            totalcedulas=totalcedula2reais+totalcedula5reais+totalcedula10reais+totalcedula20reais+totalcedula50reais+totalcedula100reais+totalcedula200reais  
            if inserindomoedas==2:
                troco_disponivel=(cedula2reais*2+cedula5reais*5+cedula10reais*10+cedula20reais*20+cedula50reais*50+cedula100reais*100+cedula200reais*200)+(moedas5cent*0.05+moedas10cent*0.10+moedas25cent*0.25+moedas50cent*0.5+moedas1real*1)
                if inserindomoedas==2 and (totalmoedas!=0 or totalcedulas!=0):
                    troco_disponivel=(totalcedula2reais*2+totalcedula5reais*5+totalcedula10reais*10+totalcedula20reais*20+totalcedula50reais*50+totalcedula100reais*100+totalcedula200reais*200)+(totalmoedas5cent*0.05+totalmoedas10cent*0.10+totalmoedas25cent*0.25+totalmoedas50cent*0.5+totalmoedas1real*1)
            else:
                troco_disponivel=(totalcedula2reais*2+totalcedula5reais*5+totalcedula10reais*10+totalcedula20reais*20+totalcedula50reais*50+totalcedula100reais*100+totalcedula200reais*200)+(totalmoedas5cent*0.05+totalmoedas10cent*0.10+totalmoedas25cent*0.25+totalmoedas50cent*0.5+totalmoedas1real*1)
            if troco_disponivel==0 and (pagamento==1 or pagamento==2 or pagamento==3):
                print("Sem troco, no momento aceitamos apenas valores inteiros!!")
                print('-------------------------------------------------------')
            else:
                if troco_disponivel>0 and (pagamento==1 or pagamento==2 or pagamento==3):
                    print("Estamos com pouca disponibilidade de troco, no momento preferimos valores inteiros!!")
                    print('-------------------------------------------------------')
                else:
                    print("Escolha um número válido!")
            if pagamento == 1:
                moedas5cent=int(input('Quantidade de moedas de 5 centavos:'))
                moedas10cent=int(input('Quantidade de moedas de 10 centavos:'))
                moedas25cent=int(input('Quantidade de moedas de 25 centavos:'))
                moedas50cent=int(input('Quantidade de moedas de 50 centavos:'))
                moedas1real=int(input('Quantidade de moedas de 1 real:'))
                print('-------------------------------------------------------')
                total_moedas=moedas5cent*0.05+moedas10cent*0.10+moedas25cent*0.25+moedas50cent*0.5+moedas1real*1    
                if total_moedas>valor and troco_disponivel>0:
                    troco=(total_moedas)-valor
                    print('Seu troco é de', round(troco, 2),'reais')
                    if troco>0:
                        totalmoedas5cent=addmoedas5cent+moedasiniciais5cent+insmoedas5cent+moedas5cent
                        totalmoedas10cent=addmoedas10cent+moedasiniciais10cent+insmoedas10cent+moedas10cent
                        totalmoedas25cent=addmoedas25cent+moedasiniciais25cent+insmoedas25cent+moedas25cent
                        totalmoedas50cent=addmoedas50cent+moedasiniciais50cent+insmoedas50cent+moedas50cent
                        totalmoedas1real=addmoedas1real+moedasiniciais1real+insmoedas1real+moedas1real
                        totalcedula2reais=addcedula2reais+cedulainiciais2reais+inscedula2reais+cedula2reais
                        totalcedula5reais=addcedula5reais+cedulainiciais5reais+inscedula5reais+cedula5reais
                        totalcedula10reais=addcedula10reais+cedulainiciais10reais+inscedula10reais+cedula10reais
                        totalcedula20reais=addcedula20reais+cedulainiciais20reais+inscedula20reais+cedula20reais
                        totalcedula50reais=addcedula50reais+cedulainiciais50reais+inscedula50reais+cedula50reais
                        totalcedula100reais=addcedula100reais+cedulainiciais100reais+inscedula100reais+cedula100reais
                        totalcedula200reais=addcedula200reais+cedulainiciais200reais+inscedula200reais+cedula200reais   
                        if troco<=(totalcedula2reais*2+totalcedula5reais*5+totalcedula10reais*10+totalcedula20reais*20+totalcedula50reais*50+totalcedula100reais*100+totalcedula200reais*200)+(totalmoedas5cent*0.05+totalmoedas10cent*0.10+totalmoedas25cent*0.25+totalmoedas50cent*0.5+totalmoedas1real*1):
                            while troco>=200 and totalcedula200reais>0:
                                print("Estamos mandando uma cédula de 200 reais")
                                troco -= 200
                                cedulainiciais200reais-=1
                            while troco>= 100 and totalcedula100reais>0:
                                print("Estamos mandando uma cédula de 100 reais")
                                troco -= 100
                                cedulainiciais100reais-=1
                            while troco>= 50 and totalcedula50reais>0:
                                print("Estamos mandando uma cédula de 50 reais")
                                troco -= 50
                                cedulainiciais50reais-=1
                            while troco>= 20 and totalcedula20reais>0:
                                print("Estamos mandando uma cédula de 20 reais")
                                troco -= 20
                                cedulainiciais20reais-=1
                            while troco>= 10 and totalcedula10reais>0:
                                print("Estamos mandando uma cédula de 10 reais")
                                troco -= 10
                                cedulainiciais10reais-=1
                            while troco>= 5 and totalcedula5reais>0:
                                print("Estamos mandando uma cédula de 5 reais")
                                troco -= 5
                                cedulainiciais5reais-=1
                            while troco>= 2 and totalcedula2reais>0:
                                print("Estamos mandando uma cédula de 2 reais")
                                troco -= 2
                                cedulainiciais2reais-=1
                            while troco >= 1 and totalmoedas1real>0:
                                print("Estamos mandando uma moeda de 1 real")
                                troco -= 1
                                moedasiniciais1real-=1
                            while troco >= 0.5 and totalmoedas50cent>0:
                                print("Estamos mandando uma moeda de 50 centavos")
                                troco -= 0.5
                                moedasiniciais50cent-=1
                            while troco >= 0.25 and totalmoedas25cent>0:
                                print("Estamos mandando uma moeda de 25 centavos")
                                troco -= 0.25
                                moedasiniciais25cent-=1
                            while troco >= 0.10 and totalmoedas10cent>0:
                                print("Estamos mandando uma moeda de 10 centavos")
                                troco -= 0.10
                                moedasiniciais10cent-=1
                            while troco >= 0.05 and totalmoedas5cent>0:
                                print("Estamos mandando uma moeda de 5 centavos")
                                troco -= 0.05
                                moedasiniciais5cent-=1
                            if troco<=0.04:
                                troco=0
                            if troco!=0:  
                                troco_possivel=1
                            else:
                                troco_possivel=0
                troco=(total_moedas)-valor
                if total_moedas >= valor and troco_disponivel>=troco and troco_possivel==0 or total_moedas == valor and troco_possivel==0:
                    print('Pagamento concluido com sucesso!')
                    print('Bebida sendo entregue!')
                    if moedas5cent>0:
                        moedasiniciais5cent=moedas5cent+moedasiniciais5cent
                    if moedas10cent>0:
                        moedasiniciais5cent=moedas10cent+moedasiniciais10cent
                    if moedas25cent>0:
                        moedasiniciais5cent=moedas25cent+moedasiniciais25cent
                    if moedas50cent>0:
                        moedasiniciais50cent=moedas50cent+moedasiniciais50cent
                    if moedas1real>0:
                        moedasiniciais1real=moedas1real+moedasiniciais1real
                    if cedula2reais>0:
                        cedulainiciais2reais=cedula2reais+cedulainiciais2reais
                    if cedula5reais>0:
                        cedulainiciais5reais=cedula5reais+cedulainiciais5reais
                    if cedula10reais>0:
                        cedulainiciais10reais=cedula10reais+cedulainiciais10reais
                    if cedula20reais>0:
                        cedulainiciais20reais=cedula20reais+cedulainiciais20reais
                    if cedula50reais>0:
                        cedulainiciais50reais=cedula50reais+cedulainiciais50reais
                    if cedula100reais>0:
                        cedulainiciais100reais=cedula100reais+cedulainiciais100reais
                    if cedula200reais>0:
                        cedulainiciais200reais=cedula200reais+cedulainiciais200reais
                    if refri==1:
                        quantidaderefri1=quantidaderefri1-1
                        print("Agora temos em estoque", quantidaderefri1, "de", nomerefri1)
                    elif refri==2:
                        quantidaderefri2=quantidaderefri2-1
                        print("Agora temos em estoque", quantidaderefri2, "de", nomerefri2)
                    elif refri==3:
                        quantidaderefri3=quantidaderefri3-1
                        print("Agora temos em estoque", quantidaderefri3, "de", nomerefri3)
                    elif refri==4:
                        quantidaderefri4=quantidaderefri4-1
                        print("Agora temos em estoque", quantidaderefri4, "de", nomerefri4)
                    elif refri==5:
                        quantidaderefri5=quantidaderefri5-1
                        print("Agora temos em estoque", quantidaderefri5, "de", nomerefri5) 
                if total_moedas<valor or troco_disponivel<=0 and troco_disponivel<troco or troco_possivel==1:
                    if total_moedas<valor:
                        print('Valor insuficiente! Seu dinheiro será devolvido!')
                    elif troco_possivel==1:
                        print('Não temos o troco necessário para te devolver! Devolvendo seu dinheiro')
                    else:
                        print("Infelizmente estamos sem troco para seu pagamento, então retornaremos os valores inseridos!")
                    if moedas5cent>0 and (inserindomoedas!=1 or totaladdmoedas5cent==0):
                        print("Moedas de 5 centavos = ", moedas5cent)
                        moedas5cent=moedas5cent-moedas5cent
                    else:
                        if moedas5cent>0:
                            print("Moedas de 5 centavos = ", moedas5cent)
                            totaladdmoedas5cent=totaladdmoedas5cent-moedas5cent
                    if moedas10cent>0 and (inserindomoedas!=1 or totaladdmoedas10cent==0):
                        print("Moedas de 10 centavos = ", moedas10cent)
                        moedas10cent=moedas10cent-moedas10cent
                    else:
                        if moedas10cent>0:
                            print("Moedas de 10 centavos = ", moedas10cent)
                            totaladdmoedas10cent=totaladdmoedas10cent-moedas10cent
                    if moedas25cent>0 and (inserindomoedas!=1 or totaladdmoedas25cent==0):
                        print("Moedas de 25 centavos = ", moedas25cent)
                        moedas25cent=moedas25cent-moedas25cent
                    else:
                        if moedas25cent>0:
                            print("Moedas de 25 centavos = ", moedas25cent)
                            totaladdmoedas25cent=totaladdmoedas25cent-moedas25cent
                    if moedas50cent>0 and (inserindomoedas!=1 or totaladdmoedas50cent==0):
                        print("Moedas de 50 centavos = ", moedas50cent)
                        moedas50cent=moedas50cent-moedas50cent
                    else:
                        if moedas50cent>0:
                            print("Moedas de 50 centavos = ", moedas50cent)
                            totaladdmoedas50cent=totaladdmoedas50cent-moedas50cent
                    if moedas1real>0 and (inserindomoedas!=1 or totaladdmoedas1real==0):
                        print("Moedas de 1 real = ", moedas1real)
                        moedas1real=moedas1real-moedas1real
                    else:
                        if moedas1real>0:
                            print("Moedas de 1 real = ", moedas1real)
                            totaladdmoedas1real=totaladdmoedas1real-moedas1real
                    if cedula2reais>0 and (inserindomoedas!=1 or totaladdcedula2reais==0):
                        print("Cédulas de 2 reais = ", cedula2reais)
                        cedula2reais=cedula2reais-cedula2reais
                    else:
                        if cedula2reais>0:
                            print("Cédulas de 2 reais = ", cedula2reais)
                            totaladdcedula2reais=totaladdcedula2reais-cedula2reais
                    if cedula5reais>0 and (inserindomoedas!=1 or totaladdcedula5reais==0):
                        print("Cédulas de 5 reais = ", cedula5reais)
                        cedula5reais=cedula5reais-cedula5reais
                    else:
                        if cedula5reais>0:
                            print("Cédulas de 5 reais = ", cedula5reais)
                            totaladdcedula5reais=totaladdcedula5reais-cedula5reais
                    if cedula10reais>0 and (inserindomoedas!=1 or totaladdcedula10reais==0):
                        print("Cédulas de 10 reais = ", cedula10reais)
                        cedula10reais=cedula10reais-cedula10reais
                    else:
                        if cedula10reais>0:
                            print("Cédulas de 10 reais = ", cedula10reais)
                            totaladdcedula10reais=totaladdcedula10reais-cedula10reais
                    if cedula20reais>0 and (inserindomoedas!=1 or totaladdcedula20reais==0):
                        print("Cédulas de 20 reais = ", cedula20reais)
                        cedula20reais=cedula20reais-cedula20reais
                    else:
                        if cedula20reais>0:
                            print("Cédulas de 20 reais = ", cedula20reais)
                            totaladdcedula20reais=totaladdcedula20reais-cedula20reais
                    if cedula50reais>0 and (inserindomoedas!=1 or totaladdcedula50reais==0):
                        print("Cédulas de 50 reais = ", cedula50reais)
                        cedula50reais=cedula50reais-cedula50reais
                    else:
                        if cedula50reais>0:
                            print("Cédulas de 50 reais = ", cedula50reais)
                            totaladdcedula50reais=totaladdcedula50reais-cedula50reais
                    if cedula100reais>0 and (inserindomoedas!=1 or totaladdcedula100reais==0):
                        print("Cédulas de 100 reais = ", cedula100reais)
                        cedula100reais=cedula100reais-cedula100reais
                    else:
                        if cedula100reais>0:
                            print("Cédulas de 100 reais = ", cedula100reais)
                            totaladdcedula100reais=totaladdcedula100reais-cedula100reais
                    if cedula200reais>0 and (inserindomoedas!=1 or totaladdcedula200reais==0):
                        print("Cédulas de 200 reais = ", cedula200reais)
                        cedula200reais=cedula200reais-cedula200reais
                    else:
                        if cedula200reais>0:
                            print("Cédulas de 200 reais = ", cedula200reais)
                            totaladdcedula200reais=totaladdcedula200reais-cedula200reais
                    print("Tenha um ótimo dia!")
                else:
                    print('Obrigado por comprar conosco!')
            elif pagamento == 2:
                cedula2reais=int(input('Quantidade de cédulas de 2 reais:'))
                cedula5reais=int(input('Quantidade de cédulas de 5 reais:'))
                cedula10reais=int(input('Quantidade de cédulas de 10 reais:'))
                cedula20reais=int(input('Quantidade de cédulas de 20 reais:'))
                cedula50reais=int(input('Quantidade de cédulas de 50 reais:'))
                cedula100reais=int(input('Quantidade de cédulas de 100 reais:'))
                cedula200reais=int(input('Quantidade de cédulas de 200 reais:'))
                print('-------------------------------------------------------')
                total_cedula=cedula2reais*2+cedula5reais*5+cedula10reais*10+cedula20reais*20+cedula50reais*50+cedula100reais*100+cedula200reais*200   
                if total_cedula>valor and troco_disponivel>0:
                    troco=(total_cedula)-valor
                    print('Seu troco é de', round(troco, 2),'reais')
                    if troco>0:
                        totalmoedas5cent=addmoedas5cent+moedasiniciais5cent+insmoedas5cent+moedas5cent
                        totalmoedas10cent=addmoedas10cent+moedasiniciais10cent+insmoedas10cent+moedas10cent
                        totalmoedas25cent=addmoedas25cent+moedasiniciais25cent+insmoedas25cent+moedas25cent
                        totalmoedas50cent=addmoedas50cent+moedasiniciais50cent+insmoedas50cent+moedas50cent
                        totalmoedas1real=addmoedas1real+moedasiniciais1real+insmoedas1real+moedas1real
                        totalcedula2reais=addcedula2reais+cedulainiciais2reais+inscedula2reais+cedula2reais
                        totalcedula5reais=addcedula5reais+cedulainiciais5reais+inscedula5reais+cedula5reais
                        totalcedula10reais=addcedula10reais+cedulainiciais10reais+inscedula10reais+cedula10reais
                        totalcedula20reais=addcedula20reais+cedulainiciais20reais+inscedula20reais+cedula20reais
                        totalcedula50reais=addcedula50reais+cedulainiciais50reais+inscedula50reais+cedula50reais
                        totalcedula100reais=addcedula100reais+cedulainiciais100reais+inscedula100reais+cedula100reais
                        totalcedula200reais=addcedula200reais+cedulainiciais200reais+inscedula200reais+cedula200reais   
                        if troco<=(totalcedula2reais*2+totalcedula5reais*5+totalcedula10reais*10+totalcedula20reais*20+totalcedula50reais*50+totalcedula100reais*100+totalcedula200reais*200)+(totalmoedas5cent*0.05+totalmoedas10cent*0.10+totalmoedas25cent*0.25+totalmoedas50cent*0.5+totalmoedas1real*1):
                            while troco>=200 and totalcedula200reais>0:
                                print("Estamos mandando uma cédula de 200 reais")
                                troco -= 200
                                cedulainiciais200reais-=1
                            while troco>= 100 and totalcedula100reais>0:
                                print("Estamos mandando uma cédula de 100 reais")
                                troco -= 100
                                cedulainiciais100reais-=1
                            while troco>= 50 and totalcedula50reais>0:
                                print("Estamos mandando uma cédula de 50 reais")
                                troco -= 50
                                cedulainiciais50reais-=1
                            while troco>= 20 and totalcedula20reais>0:
                                print("Estamos mandando uma cédula de 20 reais")
                                troco -= 20
                                cedulainiciais20reais-=1
                            while troco>= 10 and totalcedula10reais>0:
                                print("Estamos mandando uma cédula de 10 reais")
                                troco -= 10
                                cedulainiciais10reais-=1
                            while troco>= 5 and totalcedula5reais>0:
                                print("Estamos mandando uma cédula de 5 reais")
                                troco -= 5
                                cedulainiciais5reais-=1
                            while troco>= 2 and totalcedula2reais>0:
                                print("Estamos mandando uma cédula de 2 reais")
                                troco -= 2
                                cedulainiciais2reais-=1
                            while troco >= 1 and totalmoedas1real>0:
                                print("Estamos mandando uma moeda de 1 real")
                                troco -= 1
                                moedasiniciais1real-=1
                            while troco >= 0.5 and totalmoedas50cent>0:
                                print("Estamos mandando uma moeda de 50 centavos")
                                troco -= 0.5
                                moedasiniciais50cent-=1
                            while troco >= 0.25 and totalmoedas25cent>0:
                                print("Estamos mandando uma moeda de 25 centavos")
                                troco -= 0.25
                                moedasiniciais25cent-=1
                            while troco >= 0.10 and totalmoedas10cent>0:
                                print("Estamos mandando uma moeda de 10 centavos")
                                troco -= 0.10
                                moedasiniciais10cent-=1
                            while troco >= 0.05 and totalmoedas5cent>0:
                                print("Estamos mandando uma moeda de 5 centavos")
                                troco -= 0.05
                                moedasiniciais5cent-=1
                            if troco<=0.04:
                                troco=0
                            if troco!=0:  
                                troco_possivel=1
                            else:
                                troco_possivel=0
                troco=(total_cedula)-valor
                if total_cedula>=valor and troco_disponivel>=troco and troco_possivel==0 or total_cedula==valor and troco_possivel==0:
                    print('Pagamento concluido com sucesso!')
                    print('Bebida sendo entregue!')
                    if moedas5cent>0:
                        moedasiniciais5cent=moedas5cent+moedasiniciais5cent
                    if moedas10cent>0:
                        moedasiniciais5cent=moedas10cent+moedasiniciais10cent
                    if moedas25cent>0:
                        moedasiniciais5cent=moedas25cent+moedasiniciais25cent
                    if moedas50cent>0:
                        moedasiniciais50cent=moedas50cent+moedasiniciais50cent
                    if moedas1real>0:
                        moedasiniciais1real=moedas1real+moedasiniciais1real
                    if cedula2reais>0:
                        cedulainiciais2reais=cedula2reais+cedulainiciais2reais
                    if cedula5reais>0:
                        cedulainiciais5reais=cedula5reais+cedulainiciais5reais
                    if cedula10reais>0:
                        cedulainiciais10reais=cedula10reais+cedulainiciais10reais
                    if cedula20reais>0:
                        cedulainiciais20reais=cedula20reais+cedulainiciais20reais
                    if cedula50reais>0:
                        cedulainiciais50reais=cedula50reais+cedulainiciais50reais
                    if cedula100reais>0:
                        cedulainiciais100reais=cedula100reais+cedulainiciais100reais
                    if cedula200reais>0:
                        cedulainiciais200reais=cedula200reais+cedulainiciais200reais
                    if refri==1:
                        quantidaderefri1=quantidaderefri1-1
                        print("Agora temos em estoque", quantidaderefri1, "de", nomerefri1)
                    elif refri==2:
                        quantidaderefri2=quantidaderefri2-1
                        print("Agora temos em estoque", quantidaderefri2, "de", nomerefri2)
                    elif refri==3:
                        quantidaderefri3=quantidaderefri3-1
                        print("Agora temos em estoque", quantidaderefri3, "de", nomerefri3)
                    elif refri==4:
                        quantidaderefri4=quantidaderefri4-1
                        print("Agora temos em estoque", quantidaderefri4, "de", nomerefri4)
                    elif refri==5:
                        quantidaderefri5=quantidaderefri5-1
                        print("Agora temos em estoque", quantidaderefri5, "de", nomerefri5) 
                if total_cedula<valor or troco_disponivel<=0 and troco_disponivel<troco or troco_possivel==1:
                    if total_cedula<valor:
                        print('Valor insuficiente! Seu dinheiro será devolvido!')
                    elif troco_possivel==1:
                        print('Não temos o troco necessário para te devolver! Devolvendo seu dinheiro')
                    else:
                        print("Infelizmente estamos sem troco para seu pagamento, então retornaremos os valores inseridos!")
                    if moedas5cent>0 and (inserindomoedas!=1 or totaladdmoedas5cent==0):
                        print("Moedas de 5 centavos = ", moedas5cent)
                        moedas5cent=moedas5cent-moedas5cent
                    else:
                        if moedas5cent>0:
                            print("Moedas de 5 centavos = ", moedas5cent)
                            totaladdmoedas5cent=totaladdmoedas5cent-moedas5cent
                    if moedas10cent>0 and (inserindomoedas!=1 or totaladdmoedas10cent==0):
                        print("Moedas de 10 centavos = ", moedas10cent)
                        moedas10cent=moedas10cent-moedas10cent
                    else:
                        if moedas10cent>0:
                            print("Moedas de 10 centavos = ", moedas10cent)
                            totaladdmoedas10cent=totaladdmoedas10cent-moedas10cent
                    if moedas25cent>0 and (inserindomoedas!=1 or totaladdmoedas25cent==0):
                        print("Moedas de 25 centavos = ", moedas25cent)
                        moedas25cent=moedas25cent-moedas25cent
                    else:
                        if moedas25cent>0:
                            print("Moedas de 25 centavos = ", moedas25cent)
                            totaladdmoedas25cent=totaladdmoedas25cent-moedas25cent
                    if moedas50cent>0 and (inserindomoedas!=1 or totaladdmoedas50cent==0):
                        print("Moedas de 50 centavos = ", moedas50cent)
                        moedas50cent=moedas50cent-moedas50cent
                    else:
                        if moedas50cent>0:
                            print("Moedas de 50 centavos = ", moedas50cent)
                            totaladdmoedas50cent=totaladdmoedas50cent-moedas50cent
                    if moedas1real>0 and (inserindomoedas!=1 or totaladdmoedas1real==0):
                        print("Moedas de 1 real = ", moedas1real)
                        moedas1real=moedas1real-moedas1real
                    else:
                        if moedas1real>0:
                            print("Moedas de 1 real = ", moedas1real)
                            totaladdmoedas1real=totaladdmoedas1real-moedas1real
                    if cedula2reais>0 and (inserindomoedas!=1 or totaladdcedula2reais==0):
                        print("Cédulas de 2 reais = ", cedula2reais)
                        cedula2reais=cedula2reais-cedula2reais
                    else:
                        if cedula2reais>0:
                            print("Cédulas de 2 reais = ", cedula2reais)
                            totaladdcedula2reais=totaladdcedula2reais-cedula2reais
                    if cedula5reais>0 and (inserindomoedas!=1 or totaladdcedula5reais==0):
                        print("Cédulas de 5 reais = ", cedula5reais)
                        cedula5reais=cedula5reais-cedula5reais
                    else:
                        if cedula5reais>0:
                            print("Cédulas de 5 reais = ", cedula5reais)
                            totaladdcedula5reais=totaladdcedula5reais-cedula5reais
                    if cedula10reais>0 and (inserindomoedas!=1 or totaladdcedula10reais==0):
                        print("Cédulas de 10 reais = ", cedula10reais)
                        cedula10reais=cedula10reais-cedula10reais
                    else:
                        if cedula10reais>0:
                            print("Cédulas de 10 reais = ", cedula10reais)
                            totaladdcedula10reais=totaladdcedula10reais-cedula10reais
                    if cedula20reais>0 and (inserindomoedas!=1 or totaladdcedula20reais==0):
                        print("Cédulas de 20 reais = ", cedula20reais)
                        cedula20reais=cedula20reais-cedula20reais
                    else:
                        if cedula20reais>0:
                            print("Cédulas de 20 reais = ", cedula20reais)
                            totaladdcedula20reais=totaladdcedula20reais-cedula20reais
                    if cedula50reais>0 and (inserindomoedas!=1 or totaladdcedula50reais==0):
                        print("Cédulas de 50 reais = ", cedula50reais)
                        cedula50reais=cedula50reais-cedula50reais
                    else:
                        if cedula50reais>0:
                            print("Cédulas de 50 reais = ", cedula50reais)
                            totaladdcedula50reais=totaladdcedula50reais-cedula50reais
                    if cedula100reais>0 and (inserindomoedas!=1 or totaladdcedula100reais==0):
                        print("Cédulas de 100 reais = ", cedula100reais)
                        cedula100reais=cedula100reais-cedula100reais
                    else:
                        if cedula100reais>0:
                            print("Cédulas de 100 reais = ", cedula100reais)
                            totaladdcedula100reais=totaladdcedula100reais-cedula100reais
                    if cedula200reais>0 and (inserindomoedas!=1 or totaladdcedula200reais==0):
                        print("Cédulas de 200 reais = ", cedula200reais)
                        cedula200reais=cedula200reais-cedula200reais
                    else:
                        if cedula200reais>0:
                            print("Cédulas de 200 reais = ", cedula200reais)
                            totaladdcedula200reais=totaladdcedula200reais-cedula200reais
                    print("Tenha um ótimo dia!")
                else:
                    print('Obrigado por comprar conosco!')
            elif pagamento == 3:
                print("Insira as moedas!")
                print('-------------------------------------------------------')
                moedas5cent=int(input('Quantidade de moedas de 5 centavos:'))
                moedas10cent=int(input('Quantidade de moedas de 10 centavos:'))
                moedas25cent=int(input('Quantidade de moedas de 25 centavos:'))
                moedas50cent=int(input('Quantidade de moedas de 50 centavos:'))
                moedas1real=int(input('Quantidade de moedas de 1 real:'))
                print('-------------------------------------------------------')
                print("Agora insira as cédulas!")
                print('-------------------------------------------------------')
                cedula2reais=int(input('Quantidade de cédulas de 2 reais:'))
                cedula5reais=int(input('Quantidade de cédulas de 5 reais:'))
                cedula10reais=int(input('Quantidade de cédulas de 10 reais:'))
                cedula20reais=int(input('Quantidade de cédulas de 20 reais:'))
                cedula50reais=int(input('Quantidade de cédulas de 50 reais:'))
                cedula100reais=int(input('Quantidade de cédulas de 100 reais:'))
                cedula200reais=int(input('Quantidade de cédulas de 200 reais:'))
                print('-------------------------------------------------------')
                total_notasemoedas=(cedula2reais*2+cedula5reais*5+cedula10reais*10+cedula20reais*20+cedula50reais*50+cedula100reais*100+cedula200reais*200)+(moedas5cent*0.05+moedas10cent*0.10+moedas25cent*0.25+moedas50cent*0.5+moedas1real*1)
                if total_notasemoedas>valor and troco_disponivel>0:
                    troco=(total_notasemoedas)-valor
                    print('Seu troco é de', round(troco, 2),'reais')
                    if troco>0:
                        totalmoedas5cent=addmoedas5cent+moedasiniciais5cent+insmoedas5cent+moedas5cent
                        totalmoedas10cent=addmoedas10cent+moedasiniciais10cent+insmoedas10cent+moedas10cent
                        totalmoedas25cent=addmoedas25cent+moedasiniciais25cent+insmoedas25cent+moedas25cent
                        totalmoedas50cent=addmoedas50cent+moedasiniciais50cent+insmoedas50cent+moedas50cent
                        totalmoedas1real=addmoedas1real+moedasiniciais1real+insmoedas1real+moedas1real
                        totalcedula2reais=addcedula2reais+cedulainiciais2reais+inscedula2reais+cedula2reais
                        totalcedula5reais=addcedula5reais+cedulainiciais5reais+inscedula5reais+cedula5reais
                        totalcedula10reais=addcedula10reais+cedulainiciais10reais+inscedula10reais+cedula10reais
                        totalcedula20reais=addcedula20reais+cedulainiciais20reais+inscedula20reais+cedula20reais
                        totalcedula50reais=addcedula50reais+cedulainiciais50reais+inscedula50reais+cedula50reais
                        totalcedula100reais=addcedula100reais+cedulainiciais100reais+inscedula100reais+cedula100reais
                        totalcedula200reais=addcedula200reais+cedulainiciais200reais+inscedula200reais+cedula200reais
                        if troco<=(totalcedula2reais*2+totalcedula5reais*5+totalcedula10reais*10+totalcedula20reais*20+totalcedula50reais*50+totalcedula100reais*100+totalcedula200reais*200)+(totalmoedas5cent*0.05+totalmoedas10cent*0.10+totalmoedas25cent*0.25+totalmoedas50cent*0.5+totalmoedas1real*1):
                            while troco>=200 and totalcedula200reais>0:
                                print("Estamos mandando uma cédula de 200 reais")
                                troco -= 200
                                cedulainiciais200reais-=1
                            while troco>= 100 and totalcedula100reais>0:
                                print("Estamos mandando uma cédula de 100 reais")
                                troco -= 100
                                cedulainiciais100reais-=1
                            while troco>= 50 and totalcedula50reais>0:
                                print("Estamos mandando uma cédula de 50 reais")
                                troco -= 50
                                cedulainiciais50reais-=1
                            while troco>= 20 and totalcedula20reais>0:
                                print("Estamos mandando uma cédula de 20 reais")
                                troco -= 20
                                cedulainiciais20reais-=1
                            while troco>= 10 and totalcedula10reais>0:
                                print("Estamos mandando uma cédula de 10 reais")
                                troco -= 10
                                cedulainiciais10reais-=1
                            while troco>= 5 and totalcedula5reais>0:
                                print("Estamos mandando uma cédula de 5 reais")
                                troco -= 5
                                cedulainiciais5reais-=1
                            while troco>= 2 and totalcedula2reais>0:
                                print("Estamos mandando uma cédula de 2 reais")
                                troco -= 2
                                cedulainiciais2reais-=1
                            while troco >= 1 and totalmoedas1real>0:
                                print("Estamos mandando uma moeda de 1 real")
                                troco -= 1
                                moedasiniciais1real-=1
                            while troco >= 0.5 and totalmoedas50cent>0:
                                print("Estamos mandando uma moeda de 50 centavos")
                                troco -= 0.5
                                moedasiniciais50cent-=1
                            while troco >= 0.25 and totalmoedas25cent>0:
                                print("Estamos mandando uma moeda de 25 centavos")
                                troco -= 0.25
                                moedasiniciais25cent-=1
                            while troco >= 0.10 and totalmoedas10cent>0:
                                print("Estamos mandando uma moeda de 10 centavos")
                                troco -= 0.10
                                moedasiniciais10cent-=1
                            while troco >= 0.05 and totalmoedas5cent>0:
                                print("Estamos mandando uma moeda de 5 centavos")
                                troco -= 0.05
                                moedasiniciais5cent-=1
                            if troco<=0.04:
                                troco=0
                            if troco!=0:  
                                troco_possivel=1
                            else:
                                troco_possivel=0
                troco=(total_notasemoedas)-valor
                if total_notasemoedas >= valor and troco_disponivel>=troco and troco_possivel==0 or total_notasemoedas == valor and troco_possivel==0:
                    print('Pagamento concluido com sucesso!')
                    print('Bebida sendo entregue!')
                    if moedas5cent>0:
                        moedasiniciais5cent=moedas5cent+moedasiniciais5cent
                    if moedas10cent>0:
                        moedasiniciais5cent=moedas10cent+moedasiniciais10cent
                    if moedas25cent>0:
                        moedasiniciais5cent=moedas25cent+moedasiniciais25cent
                    if moedas50cent>0:
                        moedasiniciais50cent=moedas50cent+moedasiniciais50cent
                    if moedas1real>0:
                        moedasiniciais1real=moedas1real+moedasiniciais1real
                    if cedula2reais>0:
                        cedulainiciais2reais=cedula2reais+cedulainiciais2reais
                    if cedula5reais>0:
                        cedulainiciais5reais=cedula5reais+cedulainiciais5reais
                    if cedula10reais>0:
                        cedulainiciais10reais=cedula10reais+cedulainiciais10reais
                    if cedula20reais>0:
                        cedulainiciais20reais=cedula20reais+cedulainiciais20reais
                    if cedula50reais>0:
                        cedulainiciais50reais=cedula50reais+cedulainiciais50reais
                    if cedula100reais>0:
                        cedulainiciais100reais=cedula100reais+cedulainiciais100reais
                    if cedula200reais>0:
                        cedulainiciais200reais=cedula200reais+cedulainiciais200reais
                    if refri==1:
                        quantidaderefri1=quantidaderefri1-1
                        print("Agora temos em estoque", quantidaderefri1, "de", nomerefri1)
                    elif refri==2:
                        quantidaderefri2=quantidaderefri2-1
                        print("Agora temos em estoque", quantidaderefri2, "de", nomerefri2)
                    elif refri==3:
                        quantidaderefri3=quantidaderefri3-1
                        print("Agora temos em estoque", quantidaderefri3, "de", nomerefri3)
                    elif refri==4:
                        quantidaderefri4=quantidaderefri4-1
                        print("Agora temos em estoque", quantidaderefri4, "de", nomerefri4)
                    elif refri==5:
                        quantidaderefri5=quantidaderefri5-1
                        print("Agora temos em estoque", quantidaderefri5, "de", nomerefri5) 
                if total_notasemoedas<valor or troco_disponivel<=0 and troco_disponivel<troco or troco_possivel==1:
                    if total_notasemoedas<valor:
                        print('Valor insuficiente! Seu dinheiro será devolvido!')
                    elif troco_possivel==1:
                        print('Não temos o troco necessário para te devolver! Devolvendo seu dinheiro')
                    else:
                        print("Infelizmente estamos sem troco para seu pagamento, então retornaremos os valores inseridos!")
                    if moedas5cent>0 and (inserindomoedas!=1 or totaladdmoedas5cent==0):
                        print("Moedas de 5 centavos = ", moedas5cent)
                        moedas5cent=moedas5cent-moedas5cent
                    else:
                        if moedas5cent>0:
                            print("Moedas de 5 centavos = ", moedas5cent)
                            totaladdmoedas5cent=totaladdmoedas5cent-moedas5cent
                    if moedas10cent>0 and (inserindomoedas!=1 or totaladdmoedas10cent==0):
                        print("Moedas de 10 centavos = ", moedas10cent)
                        moedas10cent=moedas10cent-moedas10cent
                    else:
                        if moedas10cent>0:
                            print("Moedas de 10 centavos = ", moedas10cent)
                            totaladdmoedas10cent=totaladdmoedas10cent-moedas10cent
                    if moedas25cent>0 and (inserindomoedas!=1 or totaladdmoedas25cent==0):
                        print("Moedas de 25 centavos = ", moedas25cent)
                        moedas25cent=moedas25cent-moedas25cent
                    else:
                        if moedas25cent>0:
                            print("Moedas de 25 centavos = ", moedas25cent)
                            totaladdmoedas25cent=totaladdmoedas25cent-moedas25cent
                    if moedas50cent>0 and (inserindomoedas!=1 or totaladdmoedas50cent==0):
                        print("Moedas de 50 centavos = ", moedas50cent)
                        moedas50cent=moedas50cent-moedas50cent
                    else:
                        if moedas50cent>0:
                            print("Moedas de 50 centavos = ", moedas50cent)
                            totaladdmoedas50cent=totaladdmoedas50cent-moedas50cent
                    if moedas1real>0 and (inserindomoedas!=1 or totaladdmoedas1real==0):
                        print("Moedas de 1 real = ", moedas1real)
                        moedas1real=moedas1real-moedas1real
                    else:
                        if moedas1real>0:
                            print("Moedas de 1 real = ", moedas1real)
                            totaladdmoedas1real=totaladdmoedas1real-moedas1real
                    if cedula2reais>0 and (inserindomoedas!=1 or totaladdcedula2reais==0):
                        print("Cédulas de 2 reais = ", cedula2reais)
                        cedula2reais=cedula2reais-cedula2reais
                    else:
                        if cedula2reais>0:
                            print("Cédulas de 2 reais = ", cedula2reais)
                            totaladdcedula2reais=totaladdcedula2reais-cedula2reais
                    if cedula5reais>0 and (inserindomoedas!=1 or totaladdcedula5reais==0):
                        print("Cédulas de 5 reais = ", cedula5reais)
                        cedula5reais=cedula5reais-cedula5reais
                    else:
                        if cedula5reais>0:
                            print("Cédulas de 5 reais = ", cedula5reais)
                            totaladdcedula5reais=totaladdcedula5reais-cedula5reais
                    if cedula10reais>0 and (inserindomoedas!=1 or totaladdcedula10reais==0):
                        print("Cédulas de 10 reais = ", cedula10reais)
                        cedula10reais=cedula10reais-cedula10reais
                    else:
                        if cedula10reais>0:
                            print("Cédulas de 10 reais = ", cedula10reais)
                            totaladdcedula10reais=totaladdcedula10reais-cedula10reais
                    if cedula20reais>0 and (inserindomoedas!=1 or totaladdcedula20reais==0):
                        print("Cédulas de 20 reais = ", cedula20reais)
                        cedula20reais=cedula20reais-cedula20reais
                    else:
                        if cedula20reais>0:
                            print("Cédulas de 20 reais = ", cedula20reais)
                            totaladdcedula20reais=totaladdcedula20reais-cedula20reais
                    if cedula50reais>0 and (inserindomoedas!=1 or totaladdcedula50reais==0):
                        print("Cédulas de 50 reais = ", cedula50reais)
                        cedula50reais=cedula50reais-cedula50reais
                    else:
                        if cedula50reais>0:
                            print("Cédulas de 50 reais = ", cedula50reais)
                            totaladdcedula50reais=totaladdcedula50reais-cedula50reais
                    if cedula100reais>0 and (inserindomoedas!=1 or totaladdcedula100reais==0):
                        print("Cédulas de 100 reais = ", cedula100reais)
                        cedula100reais=cedula100reais-cedula100reais
                    else:
                        if cedula100reais>0:
                            print("Cédulas de 100 reais = ", cedula100reais)
                            totaladdcedula100reais=totaladdcedula100reais-cedula100reais
                    if cedula200reais>0 and (inserindomoedas!=1 or totaladdcedula200reais==0):
                        print("Cédulas de 200 reais = ", cedula200reais)
                        cedula200reais=cedula200reais-cedula200reais
                    else:
                        if cedula200reais>0:
                            print("Cédulas de 200 reais = ", cedula200reais)
                            totaladdcedula200reais=totaladdcedula200reais-cedula200reais
                    print("Tenha um ótimo dia!")
                else:
                    print('Obrigado por comprar conosco!')
        else:
            print('-------------------------------------------------------')
            print("Escolha um número válido!")
