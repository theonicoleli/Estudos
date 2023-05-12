while True:
    frase = input('Digite a frase: ')
    if not frase.isdigit():
        frase = frase.lower()
        frase = str(frase)
        vogais = frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u")
        espacos = frase.count(" ")
        print(f'A quantidade de vogais de sua frase são {vogais}, já a quantidade de espaços são {espacos}')
    else:
        print('Digite uma frase, não um número!')