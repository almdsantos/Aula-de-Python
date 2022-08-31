#Declaração de variáveis

eymael = 0
levyFidelix = 0
caboDaciolo = 0
votoNulo = 0
votoBranco = 0


escolha = 0
controle = "S"
nind = 0

while(controle.lower()=="s"):
    print("1 - Eymael")
    print("2 - Levy Fidelix")
    print("3 - Cabo Daciolo")
    print("4 - Voto nulo")
    print("5 - Voto em branco")
    
    escolha = int(input("Digite o número do seu candidato"))
    if (escolha == 1):
             eymael = eymael + 1
             nind = nind + 1
             
    elif (escolha == 2):
            levyFidelix = levyFidelix + 1
            nind = nind + 1
            
    elif (escolha == 3):
            caboDaciolo = caboDaciolo + 1
            nind = nind + 1
        
    elif (escolha == 4):
            votoNulo = votoNulo + 1
            nind = nind + 1
            
    elif (escolha == 5):
            votoBranco = votoBranco + 1
            nind = nind + 1
            
    else:
        print("Voto inválido")
            
    print("Deseja continuar?")
    print("Digite S para continuar")
    print("ou pressione qualquer outra tecla para parar")
    controle = input()
    
    if (controle != "S"):
        print("Número de pessoas pesquisadas = ", nind)
            
        if (eymael == 0):
            print("Candidato Eymael não recebeu votos")
        else:
            eymael = (eymael / nind) * 100
            print("Quantidade de votos para Eymael = ", eymael, "%")
                    
        if (levyFidelix == 0):
            print("Candidato Levy Fidelix não recebeu votos")
        else:
            levyFidelix = (levyFidelix / nind) * 100
            print("Quantidade de votos para Levy Fidelix = ", levyFidelix, "%")
                    
        if (caboDaciolo == 0):
            print("Candidato Cabo Daciolo não recebeu votos")
        else:
            caboDaciolo = (caboDaciolo / nind) * 100
            print("Quantidade de votos para Cabo Daciolo = ", caboDaciolo, "%")
                    
        if (votoNulo == 0):
            print("Sem votos nulo")
        else:
            votoNulo = (votoNulo / nind) * 100
            print("Quantidade de votos Nulo = ", votoNulo, "%")
                    
        if (votoBranco == 0):
            print("Sem votos nulo")
        else:
            votoBranco = (votoBranco / nind) * 100
            print("Quantidade de Votos em Branco = ", votoBranco, "%")

        
    
    
    
    
    
    
    
     