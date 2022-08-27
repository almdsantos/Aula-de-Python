#Aula 02

#Validador de CPF

cpf = input("favor informar o CPF, somente digitos")

if (len(cpf) == 11):
    v11 = int(cpf[0]) * 10
    v12 = int(cpf[1]) * 9
    v13 = int(cpf[2]) * 8
    v14 = int(cpf[3]) * 7
    v15 = int(cpf[4]) * 6
    v16 = int(cpf[5]) * 5
    v17 = int(cpf[6]) * 4
    v18 = int(cpf[7]) * 3
    v19 = int(cpf[8]) * 2
    verificador1 = ((v11+v12+v13+v14+v15+v16+v17+v18+v19) * 10) % 11
    
    v21 = int(cpf[0]) * 11
    v22 = int(cpf[1]) * 10
    v23 = int(cpf[2]) * 9
    v24 = int(cpf[3]) * 8
    v25 = int(cpf[4]) * 7
    v26 = int(cpf[5]) * 6
    v27 = int(cpf[6]) * 5
    v28 = int(cpf[7]) * 4
    v29 = int(cpf[8]) * 3
    v30 = int(cpf[9]) * 2
    verificador2 = ((v21+v22+v23+v24+v25+v26+v27+v28+v29+v30) * 10) % 11
    
    verificador1 = str(verificador1)
    verificador2 = str(verificador2)
    
    if ((verificador1 == cpf[9]) and (verificador2 == cpf[10])) or ((verificador1[1] == cpf[9]) and (verificador2 == cpf[10])):
        print("CPF Válido")
        
    else:
        print("CPF não é válido")
        
else:
    print("Digite um numero válido")