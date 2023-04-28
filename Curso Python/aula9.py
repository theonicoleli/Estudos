while True:  
    avioes = ['Pequeno','Medio', 'Grande']
    selecao_avioes = input("Digite 1 para Avião Pequeno, 2 para Avião Médio ou 3 para Avião Grande: ")
    if selecao_avioes.isdigit():
        selecao_avioes = int(selecao_avioes)
        if 1<=selecao_avioes<=3:
            avioes = avioes[selecao_avioes-1]
            viagens = int(input("Digite quantas viagens foram feitas: "))
            tempo_viagens = []
            for aviao in range(viagens):
                tempo_viagem = float(input("Digite em horas quanto tempo levou a viagem: "))
                tempo_viagens.append(tempo_viagem)
            tempo_medio= sum(tempo_viagens)/viagens
            print("O tempo médio para percorrer esta viagem com o", avioes,'é de' , round(tempo_medio,2),"horas!")
    else:
        print("Escolha um número válido!")