def verificar_palindromo(texto) -> str:

    texto = texto.lower().replace(" ", "") #aqui deixamos a palavra toda com letras minúsculas e retiramos espaços
    tamanho = len(texto)
    for i in range(tamanho // 2):
        if texto[i] != texto[tamanho - 1 - i]:
            return False
    return True

# Exemplo de uso
while True:
    palavra = input('Digite uma palavra ou [1] para sair: ')
    if palavra.isdigit():
        palavra = int(palavra)
        if palavra == 1:
            print('Obrigado pelo teste!')
            break
        else:
            continue
    elif verificar_palindromo(palavra):
        print(f"{palavra} é um palíndromo")
    else:
        print(f"{palavra} não é um palíndromo")