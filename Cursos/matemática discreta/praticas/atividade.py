import os

def imprimirLista(opcoes):
    print("Menu de opções: ")
    for index, opcao in enumerate(opcoes):
        print(f"{index+1} - {opcao}")

votos = [0, 0, 0, 0, 0, 0]
opcoes = ["Python", "C++", "Java", "Rust", "C#", "Outro"]

while True:

    imprimirLista(opcoes)
    voto = int(input("Digite o número correspondente à linguagem de programação (1 a 6), ou 0 para encerrar a votação: "))
    
    if voto == 0:
        break
    elif voto >= 1 and voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 6 ou 0 para encerrar a votação.")
    
    os.system('cls')

total_votos = sum(votos)

os.system('cls')

print("Linguagem    Votos    %")
print("------------------- ----- ---")
for i in range(6):
    percentual = (votos[i] / total_votos) * 100
    print(f"{opcoes[i]:<12} {votos[i]:<8} {percentual:.0f}%")

print("------------------- ----- ---")
print(f"Total       {total_votos}")
