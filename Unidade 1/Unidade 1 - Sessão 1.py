# VARIÁVEIS E TIPOS BÁSICOS DE DADOS EM PYTHON

x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True

# Para saber o tipo de dado que uma variável guarda, podemos imprimir seu tipo usando a função type().

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))

# A função "input() faz a leitura de um valor digitado.

nome = input("Digite um nome: ")
print(nome)

# Para unir um texto escrito pelo programa + variável digitado pelo usuário:
# print(f"texto {variável} texto").

print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")

# Ordem de precedências das operações.
#1. Primeiro resolvem-se os parênteses, do mais interno para o mais externo.
#2. Exponenciação.
#3. Multiplicação e divisão.
#4. Soma e subtração.
 

# Qual o resultado armazenado na variável operacao_1: 25 ou 17? 
operacao_1 = 2 + 3 * 5

# Qual o resultado armazenado na variável operacao_2: 25 ou 17? 
operacao_2 = (2 + 3) * 5

# Qual o resultado armazenado na variável operacao_3: 4 ou 1?
operacao_3 = 4 / 2 ** 2

# Qual o resultado armazenado na variável operacao_4: 1 ou 5?
operacao_4 = 13 % 3 + 4

print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")

# Uma equação do segundo grau possui a fórmula: y = a*x**2 + b*x + c, onde a, b, c são constantes.
# Considerando os valores a = 2, b = 0.5 e c = 1.

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

# "TypeError" quer dizer que alguma variável não está com o tipo adequado para a situação.
# A mensagem nos diz que não é permitida a operação de potenciação (**) entre um tipo string e inteiro.
# Portanto, o erro é porque estamos tentando fazer uma operação matemática entre string e um tipo numérico.
# Ao usar a função input(), ela retorna uma string, independente do que o usuário digitou, sempre será string.

# Aqui fazemos a conversão da string para o tipo numérico.
x = float(x)

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")