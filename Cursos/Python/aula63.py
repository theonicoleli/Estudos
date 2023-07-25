# Estudos de try except, else e finally

# Em seu código pode conter quantos except você desejar
# Pode-se utilizar try e finally sem necessariamente precisar do except
# Else só poder ser inserido caso o código tenha o except já incluso
# Finally só pode ser inserido 1 vez no código assim como o else

try:
    a = 37
    b = 33
    c = 2
    print('Estou no TRY')
    d = a+b/c

except ZeroDivisionError:
    print('Divisão por zero')

except (TypeError, IndexError) as error:
    print(error)
    print(f'A letra não informada gerou o erro: {error.__class__.__name__}')

except Exception:
    print('ERRO DESCONHECIDO')

else:
    print('Código sem erros!')

finally:
    print('Boa tarde!')