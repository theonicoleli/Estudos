salario = float(input("Coloque seu salário ao lado para podermos registrar quanto de desconto vai ser retirado de seu salário: "))
if salario >= 1257.13 and salario <= 2512.08:
    desconto = (salario * 15)/100
    print("O desconto de seu salário será de, ", round(desconto, 2), "reais")
elif salario < 1257.13:
    desconto = 0
    print("Seu salário não possui desconto")
else:
    salario <= 2512.08
    desconto = (salario * 27.5)/100
    print("O desconto de seu salário será de, ", round(desconto, 2), "reais")
salario_limpo = salario - desconto
print("Seu salário limpo será de, ", round(salario_limpo, 2), "reais")
