Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Aula 01
#1º Exercicio

#nome do funcionario IN
#registro(inteiro) IN
#salario bruto IN
#gestor (booleano) - IN
#desconto (12,8% em cima do salario bruto)
#comissao (16,7% do salario bruto)

#nome e registro na mesma linha - OUT
#salario bruto - OUT
#valor dos descontos - OUT
#valor da comissao - OUT
#salario total - OUT

nome_do_funcionario = input("Informe o seu nome\n")
registro = input("Informe o numero do seu registro\n")
gestor = bool(input("Só preencha se for gestor?"))
salario_bruto = float(input("Informe o seu salário\n"))
desconto = salario_bruto - (salario_bruto - (12.8/100)*salario_bruto)
valor_comissao = salario_bruto - (salario_bruto - (16.8/100)*salario_bruto)
salario_total = salario_bruto - desconto + valor_comissao


print("O funcionário", nome_do_funcionario, "de registro", registro, "\n")
print("É gestor de equipe?", gestor)
print("Tem o salário bruto de ", salario_bruto, "com descontos de ",
  	desconto, "e comissão de ", valor_comissao, "\n")
print("Dando um salário total de R$ ", salario_total)
