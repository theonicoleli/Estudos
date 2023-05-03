while True:   
    nota=input("Digite sua nota: ")
    if nota.isdigit():
        nota = int(nota)
        if nota==0:
            print("Sua nota foi E")
        elif 1<=nota<=35:
            print("Sua nota foi D")
        elif 36<=nota<=60:
            print("Sua nota foi C")
        elif 61<=nota<=85:
            print("Sua nota foi B")
        elif 86<=nota<=100:
            print("Sua nota foi A")
        else:
            print("Digite uma nota válida!")
    else:
        print("Escolha um número válido!")