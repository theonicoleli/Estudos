#Criando uma lista
list = []
def menu():
    new_quanty=int(input('Escolha uma quantidade de novos números para sua lista: ')) # Quantidade de números que a pessoa deseja
    number = 0 # Quantidade de números iniciais
    while number < new_quanty:
        new_number=int(input('Escolha um número para lista: '))
        list.append(new_number)
        number+=1
        print(list)
menu()
counter=0
while counter==0:
    new_op=int(input('Ok, sua seção de inseridos foi finalizada, deseja realizar outra operação [1 para SIM e 2 para NÃO] '))
    number=list
    if new_op==1:
       chooses=int(input('1) Deseja rever quais foram os números listados\n2) Deseja adicionar novos números\n3) Deseja remover números\n4) Deseja alterar algum dos números\nEscolha sua opção digitando o número dela:'))
       if chooses==1:
          print(list)
       elif chooses==2:
          print(list,"\nA cima esta sua lista atual!")
          menu()
       elif chooses==3:
          print(list,"\nA cima esta sua lista atual!")
          new_quanty=int(input('Digite a posição do número ao qual você deseja retirar: '))
          if new_quanty==list[new_quanty-1]:
              list.pop(new_quanty-1)
              print(list)
       elif chooses==4:
           print(list,"\nA cima esta sua lista atual!")
           change=int(input('Digite a posição do número que você deseja alterar: '))
           if change<=len(list):
               new_number=int(input('Digite o novo número: '))
               list[change-1] = new_number
               print(list)
    else:
        print('Ok, agradecemos o seu contato com nossos serviços!\nSua lista segue a baixo\n',list)
        break  