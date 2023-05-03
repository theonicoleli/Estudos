while True:    
    quantidade_viagens = 10
    selecao_avioes = int(input('Digite 1 para Avião Pequeno, 2 para Médio ou 3 para Grande: '))
    tempo_total = 0
    for viagem in range(quantidade_viagens):
        viagem = int(input('Digite o tempo que levou em horas desta viagem: '))
        tempo_total += viagem
    if quantidade_viagens > 0:
        tempo_medio = tempo_total / quantidade_viagens
        if selecao_avioes==1:
            print('O tempo médio da viagem com o avião pequeno é de ', round(tempo_medio, 2),'horas')
        elif selecao_avioes==2:
            print('O tempo médio da viagem com o avião médio é de ', round(tempo_medio, 2),'horas')
        elif selecao_avioes==3:
            print('O tempo médio da viagem com o avião grande é de ', round(tempo_medio, 2),'horas')
    else:
        print('Nenhuma viagem foi registrada.')