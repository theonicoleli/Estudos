import pandas as pd
import numpy as np

table = pd.DataFrame()
lista = "Ricardo Théo João Pedro Felipe José Maria".split()
table["Nomes".rjust(5)] = lista
table["Quantidade".rjust(5)] = 0
table["Idade".rjust(5)] = 0
table.iloc[6,1] = 4
for names in range(len(lista)):
    table.iloc[names, 1] = 1 if names!=6 else 4
for idade in range(len(lista)):
    table.iloc[idade, 2] = 18 if idade!=6 else 23
print(table)