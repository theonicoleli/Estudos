# 10) Faça um menu que só encerre quando o usuário solicitar (opção de sair) que seja interativo e com as
# devidas validações de possíveis erros de entrada do usuário. O objetivo é fazer a operação entre 2 conjuntos,
# ou seja, crie uma forma de pedir dois conjuntos para o usuário (conjuntos A e B – posteriormente esses
# conjuntos podem ser alterados pelo usuário). As opções de operações são:


print('Bem vindo!')
print('Para podermos dar continuidade, será preciso que você construa seus dois conjuntos')

conjunto_a = set()
conjunto_b = set()

for n in range(2):
    conjunto_atual = conjunto_a if n == 0 else conjunto_b
    while True:
        numero = input("Digite um número (ou 'sair' para parar de adicionar números a este conjunto): ")
        if numero.lower() == 'sair':
            print(f"{'Conjunto A final:' if n==0 else 'Conjunto B final:'} {conjunto_a if n==0 else conjunto_b}")
            break
        
        try:
            numero = int(numero)
            conjunto_atual.add(numero)
        except ValueError:
            print("Entrada inválida. Digite um número válido ou 'sair' para parar.")

while True:
    opcao = input("Segue as operações possíveis a baixo:\n"
                "1) União\n2) Intersecção\n3) Diferença\n4) Produto cartesiano"
                "\n5) Verificação subconjunto (submenu: subconjunto ou subconjunto próprio)\n"
                "sair) \nDigite ao lado a opção desejada: ")
    
    if opcao.lower() == 'sair':
        print('Ok... saindo!')
        break

    try:
        opcao = int(opcao)

        selection = input('Digite:\n1) A em relação a B \n2) B em relação a A\n')
        if selection.isdigit():
            selection = int(selection)
        
            if opcao == 1:
                print(f"{conjunto_a.union(conjunto_b) if selection == 1 else conjunto_b.union(conjunto_a)}")

            elif opcao == 2:
                print(f"{conjunto_a.intersection(conjunto_b) if selection == 1 else conjunto_b.intersection(conjunto_a)}")

            elif opcao == 3:
                print(f"{conjunto_a.difference(conjunto_b) if selection == 1 else conjunto_b.difference(conjunto_a)}")
            
            elif opcao == 4:
                produto_cartesiano = {(a, b) for a in conjunto_a for b in conjunto_b}
                print(f"O produto cartesiano é : {produto_cartesiano}")

            elif opcao == 5:
                print(f"{conjunto_a.issubset(conjunto_b) if selection == 1 else conjunto_b.issubset(conjunto_a)}")
        
        else:
            print('Digite um valor válido!')

    except ValueError:
        print('Digite uma opção válida!')