# Implemente um algoritmo em Python para permitir a aposta de 5
# jogadores em um bolão da Copa do Mundo. Cada jogador indicará o
# resultado dos 3 primeiros jogos do Brasil, no seguinte formato:
# Jogo 1: 2 x 0
# Jogo 2: 5 x 1
# Jogo 3: 3 x 0


n_jogadores = 5
n_jogos = 3
n_times = 2
placares = [0] * n_jogadores

for jogador in range(n_jogadores):
    placares[jogador] = [0] * n_jogos
    for jogo in range(n_jogos):
        placares[jogador][jogo] = [0] * n_times

for jogador in range(n_jogadores):
    print('Aposta do jogador ',jogador, ':')
    for jogo in range(n_jogos):
        print('Aposta do jogo ', jogo, ':')
        for time in range(n_times):
            print('Número de gols do time ', time, ':')
            placares[jogador][jogo][time] = int(input('Digite o # de gols: '))

print(placares)
