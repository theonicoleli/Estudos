while True:   
    print('Descubra os 2 últimos dígitos de seu cpf')
    cpf = input('Digite os 9 primeiros números do cpf: ')
    ncpf = len(cpf)

    if 9>ncpf>9:
            print('Coloque apenas os 9 primeiros dígitos de seu CPF')

    else:
        digito_nove = cpf[:9] # Tirando os nove primeiros dígitos para multiplicar
        cont_reg = 10
        multiplicacao=0
        for numeros in digito_nove:
            multiplicacao += int(numeros) * cont_reg
            cont_reg-=1
        penultimate_number = (multiplicacao * 10) % 11
        penultimate_number = penultimate_number if penultimate_number<=9 else 0

        cpf = cpf + str(penultimate_number)# Ta somando o valor com a string CPF

        digito_dez = cpf[:10]
        cont_reg_dois = 11
        multiplicacao_dois = 0
        
        for numeros in digito_dez:
            multiplicacao_dois += int(numeros) * cont_reg_dois
            cont_reg_dois-=1
        last_number = (multiplicacao_dois * 10) % 11
        last_number = last_number if last_number<=9 else 0

        cpf = cpf + str(last_number)

        print(f'O penúltimo número de seu cpf é {penultimate_number} e o último número de seu cpf é {last_number}\nSeu cpf completo ficou:\n{cpf}')
        print('='*100)




    
    