# Estudo de decoradores com classe!
# Fazer com que tenha várias opções de métodos dentro da classe

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class Carros:
    def __init__(self, marca, nome ,ano, kilometrosL, tracao, tipo, preco):
        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.kilometrosL = kilometrosL
        self.tracao = tracao
        self.tipo = tipo
        self.preco = preco

    @classmethod
    def marcas_nome_tracao_kilometrosL_tipo(cls):
        marca_carro = input('Marca do carro: ')
        nome_carro = input('Escreva o modelo de seu carro ao lado: ')
        
        while True:
            ano_carro = input('Digite o ano de seu carro: ')
            if ano_carro.isdigit():
                ano_carro = int(ano_carro)
                break
            else:
                print('Ano inválido. Por favor, digite um valor numérico válido.')

        tracao = input('Escreva a tração de seu carro: ')
        
        while True:
            kilometrosL = input('Escreva quantos km com L seu carro faz: ')
            if is_float(kilometrosL):
                kilometrosL = float(kilometrosL)
                break
            else:
                print('Valor inválido para quilômetros por litro. Por favor, digite um valor numérico válido.')

        tipo = input('Escreva o tipo de carro que é (elétrico, híbrido, gasolina): ')

        while True:
            preco_carro = input('Digite o preço de seu carro: ')
            if is_float(preco_carro):
                preco_carro = float(preco_carro)
                break
            else:
                print('Valor inválido para quilômetros por litro. Por favor, digite um valor numérico válido.')

        return cls(marca_carro, nome_carro, ano_carro, kilometrosL, tracao, tipo, preco_carro)
    
    @staticmethod
    def menu_carros(carro_selecionado):
        print('-=' * 50)
        print('Detalhes do Carro Selecionado:')
        print('Marca:', carro_selecionado.marca)
        print('Modelo do carro:', carro_selecionado.nome)
        print(f'Ano do carro: {carro_selecionado.ano}')
        print('Kilômetros por Litro:', carro_selecionado.kilometrosL)
        print('Tração:', carro_selecionado.tracao)
        print('Tipo:', carro_selecionado.tipo)
        print(f'Preço: R$ {carro_selecionado.preco}')
        print('-=' * 50)

carros = []


while True:
    adicionar_carro = input('Digite [1] para adicionar carros ou [2] para olhar os carros disponíveis: ')
    if adicionar_carro.isdigit():
        adicionar_carro = int(adicionar_carro)

        if adicionar_carro == 1:
            novo_carro = Carros.marcas_nome_tracao_kilometrosL_tipo()
            carros.append(novo_carro)
            continue

        elif adicionar_carro == 2:
            for cont, carro in enumerate(carros):
                print(f'{cont+1})\nMarca: {carro.marca}\nModelo: {carro.nome}\nPreço: R$ {carro.preco}')
            saber_mais = input('Digite o número do carro que você deseja saber mais: ')
            if saber_mais.isdigit():
                saber_mais = int(saber_mais)
                if 1 <= saber_mais <= len(carros):
                    carro_selecionado = carros[saber_mais - 1]
                    carro_selecionado.menu_carros(carro_selecionado)
                else:
                    print('Selecione um carro válido!')

            else:
                print('Selecione um carro válido!')

        else:
            print('Selecione uma opção válida!')
        
    else:
        print('Selecione uma opção válida!')

