# raise - lançando exceções (erros)
#https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def zero_error(d):
    if d == 0:
        raise ZeroDivisionError('Você tentou fazer uma divisão por Zero.')
    return True

def int_float_error(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'O valor inserido deve ser "int" ou "float".'
            f'"{tipo_n.__name__}" foi enviado.'
        )
    return True


def divisao(n, d):
    int_float_error(n)
    int_float_error(d)
    zero_error(d)
    return n/d

#print(divisao(3, 0)) Erro pela divisão de zero
#print(divisao(3, 'd')) Erro devido a string do 'd'
#print(divisao('p', 3)) Erro devido a string do 'p'
#print(divisao('p', 0)) Erro devido a string do 'p'
#print(divisao('p', 's')) Erro devido as strings
#print(divisao(0, 0)) Erro pela divisão de zero
#print(divisao(10, 5)) Codigo funcional