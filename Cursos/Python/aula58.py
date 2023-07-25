def txt_LPL(filename):
    with open(filename, 'r') as file:
        lines = [
            line
            for line in file
        ]
        for line in lines:
            yield line

file = input('Digite o nome do arquivo a ser lido: ')
txt = txt_LPL(file)
for line in txt:
    print(line)