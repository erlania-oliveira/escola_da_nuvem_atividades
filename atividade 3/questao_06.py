'''6- Calculadora de Comissão
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente.
Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.'''

nome = input("Nome do vendedor: ")

try:
    salario_fixo = float(input("Salário fixo: "))
    total_vendas = float(input("Total de vendas: "))

    comissao = total_vendas * 0.15
    total_receber = salario_fixo + comissao

    print(f"TOTAL = R$ {total_receber:.2f}")

except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para salário e vendas.")