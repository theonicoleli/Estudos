print("Calcule com a altura e circunferência do cilindro de tanque combustível a quantidade de latas de tinta necessárias e o custo para pintar o tanque")
altura = int(input("Digite a altura do seu tanque em metros: "))
circ = int(input("Agora digite a circunferência em metros: "))
area_base = (2*3.14*circ/2*circ/2)
area_lateral = (2*3.14*circ/2*altura)
area_cilindro = area_base + area_lateral
area_total = print("A área total do seu taque de combustível é de: ", area_cilindro,"metros quadrados")
litros = area_cilindro/3
quantidade_latas = litros/5
custo = quantidade_latas*50.00
qnt_lata = int(round(quantidade_latas)) #foi utilizado o round sem valor pra poder arredondar para um valor integral
custos = round(custo,2)
print("A quantidade de latas totais vão ser de: ", qnt_lata,"unidades, já o custo total vai ser de: ", custos,"reais")