#Fazendo o jogo: PEDRA, PAPEL OU TESOURA
import random

while True:
    
    print("Jogo - Pedra, Papel ou Tesoura!")
    possiveis_variaveis = ['Pedra', 'Papel', 'Tesoura']
    pontos_vencer = int(input("Quantas rodadas para ser o vencedor? "))

    maquina_pontos=0   # Pontos para vencer a partida
    jogador_pontos=0   # Pontos para vencer a partida

    while pontos_vencer>0:
        pontos_vencer-=1
        
        def possibilidades():
            return random.choice(possiveis_variaveis)  # Fazer com que a lista seja diferente para cada jogada

        selecao_jogador = int(input("1) Pedra\n2) Papel\n3) Tesoura\nDigite o número da seleção ao lado: "))
        selecao_maquina = possibilidades()

        if selecao_jogador==1 and selecao_maquina=='Pedra' or  selecao_jogador==2 and selecao_maquina=='Papel' or  selecao_jogador==3 and selecao_maquina=='Tesoura':
            print('Jogo Empatado!')
        elif selecao_jogador==1 and selecao_maquina=='Papel':
            print('Máquina venceu! Papel ganha de Pedra!')
            maquina_pontos+=1
        elif selecao_jogador==2 and selecao_maquina=='Tesoura':
            print('Máquina venceu! Tesoura ganha de Papel!')
            maquina_pontos+=1
        elif selecao_jogador==3 and selecao_maquina=='Papel':
            print('Você venceu! Tesoura ganha de Papel!')
            jogador_pontos+=1
        elif selecao_jogador==2 and selecao_maquina=='Pedra':
            print('Você venceu! Papel ganha de Pedra!')
            jogador_pontos+=1
        elif selecao_jogador==1 and selecao_maquina=='Tesoura':
            print('Você venceu! Pedra ganha de Tesoura!')
            jogador_pontos+=1
        elif selecao_jogador==3 and selecao_maquina=='Pedra':
            print('Maquina venceu! Pedra ganha de Tesoura!')
            maquina_pontos+=1
        else:
            print('Escolha um número válido!')
            pontos_vencer+=1

    if pontos_vencer==0:
        print('='*50)
        if maquina_pontos>jogador_pontos:
            print('A Maquina venceu!')
        elif maquina_pontos==jogador_pontos:
            print('Empatou!')
        elif maquina_pontos<jogador_pontos:
            print('Você venceu a Máquina!')
        print('='*50)