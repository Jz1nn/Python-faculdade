# ENUNCIADO
# Implementar uma solução que envolve o cálculo do imposto de renda, baseado nos dados do ano de 2020. O programa deve receber um salário, com base no valor informado, e algoritmo deve verificar em qual faixa do imposto esse valor se enquadra, quando encontrar a faixa, o programa imprime o valor a ser deduzido.

salario = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto.")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
else:
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")

# Além de criar uma solução que exibe o valor do desconto, também seja impresso o valor do salário com o desconto aplicado.

salario = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto.")
    print(f"Salário a receber = {salario}")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
    print(f"Salário a receber = {salario - 142.80}")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
    print(f"Salário a receber = {salario - 354.80}")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
    print(f"Salário a receber = {salario - 636.13}")
else:
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")
    print(f"Salário a receber = {salario - 869.36}")