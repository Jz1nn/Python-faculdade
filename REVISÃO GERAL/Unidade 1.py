# VARIÁVEIS E TIPOS BÁSICOS

x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True

# type() = saber tipo de dado contido na variável.

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'bool'>

nome = input("Digite um nome: ")
print(nome)

# input() = faz a leitura do valor digitado.

print(f"Olá {nome}, bem vindo a disciplina de programação.")

# print(f"texto {variável} texto") = unir texto escrito pelo programa + variável digitada pelo usuário.

operacao_1 = 2 + 3 * 5
operacao_2 = (2 + 3) * 5
operacao_3 = 4 / 2 ** 2
operacao_4 = 13 % 3 + 4

print(f"Resultado operacao_1 = {operacao_1}")
print(f"Resultado operacao_2 = {operacao_2}")
print(f"Resultado operacao_3 = {operacao_3}")
print(f"Resultado operacao_4 = {operacao_4}")
# Resultado operacao_1 = 17
# Resultado operacao_2 = 25
# Resultado operacao_3 = 1.0
# Resultado operacao_4 = 5