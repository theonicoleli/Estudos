class Pessoa:
    def __init__(self, nome, idade, profissao, estilomusical):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.estilomusical = estilomusical
    def apresentar(self):
        print(f'Me chamo {self.nome} tenho {self.idade} anos, sou {self.profissao} e curto {self.estilomusical}')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
profissao = str(input('Digite sua profissão: '))
estilomusical = str(input('Digite seu estilo musical: '))

pessoa = Pessoa(nome, idade, profissao, estilomusical)
pessoa.apresentar()

#class Geladeira:
    #def __init__(self, nome, numero):
        #self.nome = nome
        #self.numero = numero
    #def apresentar(self):
        #print(f'O nome de sua geladeira é {self.nome} o número é {self.numero}')

#nome = str(input('Digite o nome de sua geladeira: '))
#numero = int(input('Digite o número de sua geladeira: '))

#geladeira = Geladeira(nome, numero)
#geladeira.apresentar()