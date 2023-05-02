import datetime

data_public = datetime.datetime.now()
data_public_str = data_public.strftime("%Y")
data_public_str = int(data_public_str) # Será utilizado para que seja adicionado um ano novo a cada ano que se passe!

print('Bem vindo ao BOTECO FORMULA 1')
pontos_campeonato = {1: 10, 2: 8, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0} # Posição: Pontos
nova_pontuacao = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}# Posição: Pontos

while True:

    posicoes = []
    campeonato = []
    ano_selecao = input('Digite o ano do campeonato de Formula 1: ')

    if ano_selecao.isdigit(): # Vai verificar se é um dígito, para continuar em looping! Caso não seja ele vai cair no else, onde lá ele voltará para esta opção
        ano_selecao = int(ano_selecao) # Transformando a string em inteiro
        quantidade_corridas = (input('Digite quantas corridas tiveram no ano (23 corridas no máx): '))
        if quantidade_corridas.isdigit():
            quantidade_corridas = int(quantidade_corridas)
            if 2003<=ano_selecao<=2009 and quantidade_corridas<=23:
                for corridas in range(quantidade_corridas):
                    while 1==1:
                        posicao = input(f'Digite a posição do piloto na corrida {quantidade_corridas-len(campeonato)}(máx 20 posição): ')
                        if posicao.isdigit():
                            posicao = int(posicao)
                            if posicao<=20:
                                pontuacao_final = posicao # Foi igualado uma variável a selecão da pessoa, para que possa ser calculado tanto da forma de antigamente quanto da atualidade!
                                pontuacao_final = nova_pontuacao[pontuacao_final]
                                posicoes.append(pontuacao_final)
                                posicao = pontos_campeonato[posicao]
                                campeonato.append(posicao)
                                if quantidade_corridas == len(campeonato): # Elas devem ter o mesmo valor, pois a quantidade de vezes inseridas na quantidade_corridas deve ser igual as do campeonato já que foram inseridos os valores todas as vezes que entravam nela!
                                    for pontos in range(len(campeonato)):
                                        numero_corrida = pontos
                                        pontos = campeonato[pontos]
                                        print(f'Corrida {numero_corrida+1} = {pontos} pontos')
                                    print(f'Pontuação total de: {sum(campeonato)}')
                                    print(f'A pontuação final hoje em dia deste piloto seria de: {sum(posicoes)}')
                                break
                            else:
                                print('Selecione uma posição válida!')
                                continue
                        else:
                            print('Digite o número da posição, não a escreva!')
                            continue

            elif 2010<=ano_selecao<=data_public_str and quantidade_corridas<=23:
                for corridas in range(quantidade_corridas):
                    while True:
                        posicao = input(f'Digite a posição do piloto na corrida {quantidade_corridas-len(campeonato)}(máx 20 posição): ')
                        if posicao.isdigit():
                            posicao = int(posicao)
                            if posicao<=20:
                                posicao = nova_pontuacao[posicao]
                                campeonato.append(posicao)
                                if quantidade_corridas == len(campeonato):
                                    for pontos in range(len(campeonato)):
                                        numero_corrida = pontos
                                        pontos = campeonato[pontos]
                                        print(f'Corrida {numero_corrida+1} = {pontos} pontos')
                                    print(f'Pontuação total de: {sum(campeonato)}')
                                break
                            else:
                                print('Selecione uma posição válida!')
                                continue
                        else:
                            print('Digite o número da posição, não a escreva!')
                            continue
            else:
                print('Por favor, escolha até no máx 23 corridas! São o número de corridas da atualidade da formula 1!')
        else:
            print('Por favor, escolha uma quantidade de corridas válida!')

    else:
        print('Por favor, selecione um número válido!')
        continue
