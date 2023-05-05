import random


def random_questions(questionario: dict) -> str:
    if digitos == 1:
        questions = random.choice(list(questionario.keys()))
    elif digitos == 2:
        questions = random.choice(list(questionario_dois.keys()))
    return questions

def selecao_menu(questions: dict) -> None:
    pergunta = random_questions(questions)
    resposta = input(pergunta)
    if resposta == questions[pergunta]:
        print('Parabéns, você acertou!')
    else:
        print('Você errou, tente novamente.')

questionario = {
    'Quem ganhou a copa do mundo de 1998?\n ': 'França',
    'Quem descobriu o Brasil?\n ': 'Pedro Alvarez Cabral',
    'Quantos países existem no mundo?\n ': '193',
    'Em que ano ayrton senna morreu?\n': '1994',
    'Quando foi o primeiro campeonato de formula 1?\n ': '1950',
    'Quando CR7 ganhou a primeira bola de ouro?\n ': '2008',
    'Quando foi o primeiro campeonato de formula 1 que Sebastial Vettel foi campeão mundial?\n ': '2010',
    'Quando Felipe Massa perdeu para Lewis Hamilton por 1 ponto(ano):\n ': '2008',
}
questionario_dois = {
    'Quem ganhou a copa de 2014:\n': 'Alemanha',
    'Onde foi a copa de 2014?\n': 'Brasil',
    'De quem é a famosa frase “Penso, logo existo”\n?': 'Descartes',
    'De onde é a invenção do chuveiro elétrico?\n': 'Brasil',
    'Quais o menor e o maior país do mundo?\n': 'Vaticano e Rússia',
    'Qual o nome do presidente do Brasil que ficou conhecido como Jango?\n': 'João Goulart',
    'Qual o livro mais vendido no mundo a seguir à Bíblia?\n': 'Dom Quixote',
    'Quantas casas decimais tem o número pi?\n': 'Infinitas',
    'Atualmente, quantos elementos químicos a tabela periódica possui?\n': '118',
    'Quais os países que têm a maior e a menor expectativa de vida do mundo?\n': 'Japão e Serra Leoa'
}


while True:
    digitos = input('Digite 1 ou 2: ')
    if digitos.isdigit():
        digitos = int(digitos)
        if digitos == 1:
            questions = questionario
        elif digitos == 2:
            questions = questionario_dois
        selecao_menu(questions)
    else:
        print('Escolha um número válido!')