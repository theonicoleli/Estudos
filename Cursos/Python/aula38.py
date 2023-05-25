# Estudo de decoradores com classe!
# Fazer com que tenha várias opções de métodos dentro da classe

class Carros:
    def __init__(self, marca, nome ,idade, kilometrosL, tracao, tipo):
        self.marca = marca
        self.nome = nome
        self.idade = idade
        self.kilometrosL = kilometrosL
        self.tracao = tracao
        self.tipo = tipo

    @classmethod
    def marcas_nome_tracao_kilometrosL_tipo(cls):
        marca_carro = input('Marca do carro: ')
        nome_carro = input('Escreva o modelo de seu carro ao lado: ')
        idade_carro = input('Digite a idade de seu carro em anos ao lado: ')
        tracao = input('Escreva a tração de seu carro: ')
        kilometrosL = input('Escreva quantos km com L seu carro faz: ')
        tipo = input('Escreva o tipo de carro que é (elétrico, híbrido, gasolina): ')
        return cls(marca_carro, nome_carro, idade_carro, kilometrosL, tracao, tipo)

    def salvando_para_venda(self):
        preco_carro = input('Digite o preço de seu carro: ')
        if preco_carro.isdigit():
            self.preco = float(preco_carro)
    
    @staticmethod
    def menu_carros(carro_selecionado):
        print('-=' * 50)
        print('Detalhes do Carro Selecionado:')
        print('Marca:', carro_selecionado.marca)
        print('Modelo do carro:', carro_selecionado.nome)
        print(f'Idade: {carro_selecionado.idade} anos')
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
            novo_carro.salvando_para_venda()
            carros.append(novo_carro)
            continue

        elif adicionar_carro == 2:
            for cont, carro in enumerate(carros):
                print(f'{cont+1})\nMarca: {carro.marca}\nModelo: {carro.nome}')
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

