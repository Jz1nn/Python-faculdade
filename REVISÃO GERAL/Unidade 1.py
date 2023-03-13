# UNIDADE 1

### SESSÃO 1
# VARIÁVEIS E TIPOS BÁSICOS

x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True

# type() = saber tipo de dado contido na variável

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

# input() = faz a leitura do valor digitado

print(f"Olá {nome}, bem vindo a disciplina de programação.")

# print(f"texto {variável} texto") = unir texto escrito pelo programa + variável digitada pelo usuário

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

# Ordem de precedências das operações:
# 1. Parênteses, interno x externo
# 2. Exponenciação
# 3. Multiplicação e divisão
# 4. Soma e subtração

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

x = float(x) # Conversão da string para o tipo numérico

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")

# Uma equação do segundo grau possui a fórmula: y = a*x**2 + b*x + c, onde a, b, c são constantes
# Considerando os valores a = 2, b = 0.5 e c = 1
# input() retorna uma string, independente do que o usuário digitou, sempre será string


# DESAFIO

# Você foi designado para atender um cliente que fabrica peças automotivas e criar um protótipo da solução que ele necessita. O cliente relata que tem aumentado o número de peças e que gostaria de uma solução que fosse capaz de prever quantas peças serão vendidas em um determinado mês. Esse resultado é importante para ele, uma vez que dependendo da quantidade, ele precisa contratar mais funcionários, reforçar seu estoque e prever horas extras

# O cliente enviou para você o relatório de vendas dos últimos 6 meses. Agora você precisa analisar o gráfico, pensar no algoritmo que, a partir das informações no gráfico, seja capaz de prever quantas peças serão vendidas em um determinado mês. Por exemplo, considerando o mês de janeiro como o primeiro mês, ele vendeu x peças, em fevereiro (segundo mês) ele vendeu n peças, quantas peças ele vai vender no mês 10, e no mês 11 e no mês 32? Por se tratar de um protótipo, você deve utilizar somente as informações que lhe foram cedidas, não precisa, nesse momento, analisar o comportamento de fatores externos, por exemplo, comportamento da bolsa de valores, tendência de mercado, etc

# MES   RESULTADO   AUMENTO
# 1       200         -
# 2       400         200
# 3       600         200
# 4       800         200
# 5       1000        200
# 6       1200        200

# O aumento é constante, podemos usar uma função do primeiro grau para prever qual será o resultado em qualquer mês. A função será r = c * mes, onde, r é o resultado que queremos, c é a constante de crescimento e mes é a variável de entrada. Dessa forma, ao obter um mês qualquer (2, 4, 30, etc) podemos dizer qual o resultado

# Formula:

# mes = 2; c = 200 -> r = 200 * 2 = 400 (Valor correto para o mês 2)
# mes = 3; c = 200 -> r = 200 * 3 = 600 (Valor correto para o mês 3)
# mes = 4; c = 200 -> r = 200 * 4 = 800 (Valor correto para o mês 4)
# mes = 5; c = 200 -> r = 200 * 5 = 1000 (Valor correto para o mês 5)

c = 200 # constante

mes = input("Digite o mês que deseja saber o resultado: ") # input() capturar valor digitado
mes = int(mes) # conversão srt para numérico

r = c * mes # função de primeiro grau

print(f"A quantidade de peças para o mês {mes} será {r}")
# Digite o mês que deseja saber o resultado: 42
# A quantidade de peças para o mês 42 será 8400


### SESSÃO 2
# CONDICIONAIS

a = 5
b = 10

if a < b:
    print("a é maior que b")
    r = a + b
    print(r)

# ESTRUTURA CONDICIONAL SIMPLES

a = 5
b = 10

if a < b:
    print("a é menor que b")
    r = a + b
    print(r)
else:
    print("a é maior que b")
    r = a - b
    print(r)

# ESTRUTURA CONDICIONAL COMPOSTA

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

# elif = estrutura encadeada


# ESTRUTURA AND, OR, NOT
# and = true quando os dois argumentos forem verdadeiros 
# or = true quando pelo menos um argumento for verdadeiro
# not = inverter o valor do argumento. Se o argumento for verdadeiro, transformará em falso e vice-versa

# EXEMPLO: Um aluno só pode ser aprovado caso ele tenha menos de 5 faltas e média final superior a 7.

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

# primeiro é usado a função input() e será convertido para inteiro com a função int()
# prioridade operações Booleanas:
# not
# and
# or

A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)
# True
# False


# WHILE E FOR

# while = número de repetições não conhecido

numero = 1
while numero != 0:
    numero = int(input("Digite um número: ")) # converter string para int
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")
    # Digite um número: 7
    # Número ímpar!
    # Digite um número: 

# for = "c" percorre a string assumindo seu conteúdo

nome = "John"
for c in nome:
    print(c)
    # J
    # O
    # H
    # N

nome = "John"
for i, c in enumerate(nome):
    print(f"posição = {i}, valor = {c}")
    # posição = 0, valor = J
    # posição = 1, valor = o
    # posição = 2, valor = h
    # posição = 3, valor = n

# enumerate() retorna a posição de cada item dentro da sequência
# para capturar a posição e o valor, é usado duas variáveis de controle
# a variável "i" é usada para capturar a posição e a variável "c" cada caractere da palavra


# RANGE, BREAK E CONTINUE

# for = requer uma sequência para percorrer a iteração
# para criar uma sequência numérica de iteração é usado range()

for x in range(5):
    print(x)
    # 0
    # 1
    # 2
    # 3
    # 4 

# "x" é a variável de controle, a cada iteração o valor é alterado.
# range() = usado para criar um iterável numérico (objeto iterável) para que a repetição aconteça

# Método 1:

for i in range(10):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
# Método 2:

for i in range(0, 5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
# Método 3:

for i in range(0, 20, 2):
    print(i)
    # 0
    # 2
    # 4
    # 6
    # 8
    # 10
    # 12
    # 14
    # 16
    # 18

# range() pode ser usado de três formas:
# 1. Passando um único argumento para representar a quantidade de vezes que deve repetir
# 2. Passando dois argumentos, início e fim (NÃO INCLUÍDO) que é o valor da variável de controle
# 3. Passando três argumentos, início; fim (NÃO INCLUÍDO) da variável de controle; incremento (ex:"2" = 2,4,6,8)


# break e continue = break para execução de uma estrutura de repetição, continue pula algumas execuções, dependendo da condição

disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)
    #L
    #i
    #n
    #g
    #u

# Após a primeira letra "a", a estrutura foi interrompida

disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)
    #L
    #i
    #n
    #g
    #u
    #g
    #e
    #m

    #d
    #e

    #p
    #r
    #o
    #g
    #r
    #m
    #ç
    #ã
    #o

# Foi impresso todas as letras, exceto vogais "a", sempre que forem encontradas, será pulado, mas que a repetição prossiga para o próximo valor

# EXEMPLO:

# Criar uma solução que procura pelas vogais "a", "e" em um texto
# Toda vez que essas vogais forem encontradas, informar que foi encontrada e qual posição do texto está

texto = """A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado"""

for i, c in enumerate(texto):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print(f"vogal '{c}' encontrada na posição {i}")
    else:
        continue

# "i" variável que percorre o texto e lê a posição, "c" variável que assume cada caractere


# DESAFIO

# Implementar uma solução que envolve o cálculo do imposto de renda, baseado nos dados do ano de 2020
# O programa deve receber um salário com base no valor informado, e o algoritmo deve verificar em qual faixa do imposto esse valor se enquadra
# Quando encontrar a faixa, o programa imprime o valor a ser deduzido

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
# O colaborador isento de imposto.

# Valor do salário com o desconto aplicado

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
# Digite o salário do colaborador: 1300
# O colaborador isento de imposto.
# Salário a receber = 1300.0

### SESSÃO 3
# FUNÇÕES

# print(): imprimir um valor na tela
# enumerate(): retornar a posição de um valor em uma sequência
# input(): capturar um valor digitado no teclado
# int() e float(): converter um valor no tipo inteiro ou float
# range(): criar uma sequência numérica
# type(): saber qual o tipo do objeto(variável)

a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear(a * x + b): \n")

print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")
    # A entrada do usuário a * x + b é do tipo <class 'str'>
    # Resultado da equação para x = 0 é 1
    # Resultado da equação para x = 1 é 3
    # Resultado da equação para x = 2 é 5
    # Resultado da equação para x = 3 é 7
    # Resultado da equação para x = 4 é 9

# eval() = recebe como entrada uma string (sequência de caracteres), que nesse caso é uma equação linear. Essa entrada é analisada e avaliada como uma expressão Python pela função eval(). Para cada valor de x, a fórmula é executada como uma expressão matemática e retorna um valor diferente


# FUNÇÃO DEFINIDA PELO USUÁRIO

# def nome_funcao():
    # bloco de comandos

# Os nomes das funções devem estar em minúsculas, com as palavras separadas por underline, conforme necessário. Nomes com mixedCase (mistura de maiúsculas e minúsculas) são permitidos apenas em contextos em que o nome já existe com o formato recomendado. Nomes com mixedCase (mistura de maiúsculas e minúsculas) são permitidos apenas em contextos em que o nome já existe com o formato recomendado

def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso {curso}.")

imprimir_mensagem("Python", "ADS") # recebe duas variáveis locais. São variáveis que existem somente dentro da função
# Minha primeira função em Python desenvolvida na disciplina: Python, do curso ADS.

def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em python desenvolvida na disciplina: {disciplina}, dp curso {curso}.")

resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")
# Resultado = None

def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}."

mensagem = imprimir_mensagem("Python", "ADS")
print(mensagem)
# Minha primeira função em Python desenvolvida na disciplina: Python, do curso: ADS.

# return = para guardar o resultado de uma variável, a instrução "return" retorna um valor de uma função


# Função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso. Data: 10/05/2020

def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
    # split() = quebra a string a cada espaço em branco, criando lista de elementos

    d, m, a = data.split('/')
    # split() com parâmetro o caractere '/' = a string será cortada sempre que ele aparecer
    # Ao cortar a string 'dd/mm/aaaa', temos uma lista com 3 elementos: ['dd', 'mm', 'aaaa'], ao usar a atribuição múltipla, cada valor da lista é guardado dentro de uma variável na ordem em que foram declaradas: d = 'dd', m = 'mm', a = 'aaaa'. O número de variáveis deve ser adequado ao tamanho da lista, senão ocorrerá um erro

    mes_extenso = mes[int(m) - 1] # mês 1 está na posição 0
    # Conversão do mês para extenso. Buscado na lista 'mes' posição m - 1, pois o inicio é 0 ex: março (mes 3) está na posição 2 (janeiro{0}, fevereiro{1}, março{2})

    return f'{d} de {mes_extenso} de {a}'
    # Retornado mensagem com mês por extenso

print(converter_mes_para_extenso('10/05/2020'))
# 10 de maio de 2020


# FUNÇÕES COM PARÂMETROS DEFINIDOS E INDEFINIDOS

def somar(a, b):
    return a + b

# r = somar(2) # ERRO # função foi definida para receber 2 parâmetros, mas quando foi invocada só foi passado 1 parâmetro
r = somar(2, 3)
print(r)
# 5

# Parâmetro posicional, valor obrigatório, sem valor default = os parâmetros vão depender da ordem que forem passados, por isso sao chamados de posicionais (posição influencia o resultado). Os parâmetros são obrigatórios e não possuem valor default

def calcular_desconto(valor, desconto=0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) # sem desconto
valor2 = calcular_desconto(100,0.25) # desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")
# Primeiro valor a ser pago = 100
# Segundo valor a ser pago = 75.0

# Parâmetro posicional, valor obrigatório, com valor default = quando a posição for invocada, caso nenhum valor seja passado, será utilizado o valor default

def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrar_pessoa("John", 23, "Itabuna")
# Dados a serem cadastrados:
# Nome: John
# Idade: 23
# Cidade: Itabuna

cadastrar_pessoa("Itabuna", "John", 23)
# Dados a serem cadastrados:
# Nome: Itabuna
# Idade: John
# Cidade: 23

# Parâmetro nominal, valor obrigatório, sem valor default = a posição dos argumentos na hora de chamar a função deve ser conhecida e respeitada, caso não esteja na posição correta acarretará em erros lógicos

def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
    
texto = converter_maiuscula(flag_maiuscula=True, texto="John") # passagem nominal
print(texto)
# JOHN

# Parâmetro nominal, valor obrigatório, sem valor default = não importa a posição dos parâmetros pois são identificados pelo nome,  os parâmetros são obrigatórios. Na chamada da função é obrigatório passar todos os valores e sem valor default
# Caso "flag_maiuscula" seja True, a função converte o texto recebido em letras maiúsculas, caso contrário minúsculas. Como a função "converter_maiuscula" não possui valor default para os parâmetros, então a função deve ser invocada passando ambos valores. Neste caso a atribuição não é feita de modo posicional

def converter_minuscula(texto, flag_minuscula=True): # parâmetro "flag_minuscula" possui valor True como default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()
    
texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")
# Texto 1 = linguagem de programação
# Texto 2 = linguagem de programação

# Parâmetro nominal, obrigatório, com valor default =
# "flag_minuscula", caso não seja passado na chamada da função, rebe valor True. "texto2" foi passado somente o texto.
# Ambas as chamadas o resultado foi o mesmo, devido ao valor default na função.
# Caso não quisesse o comportamento default, precisaria passar o parâmetro: "texto = converter_minuscula(flag_minuscula=False, texto="LINGUAGEM de Programação")."

# Todas as funções acima sabemos exatamente o número de parâmetros que ela recebe
# Em casos que esses parametros são arbitrários, ou seja: a função pode receber um número diferente de parâmetros a cada invocação

def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    # len() (length) = saber a quantidade de parâmetros que foram passados
    # O parâmetro não precisa ser chamado de args, mas é uma boa prática, mas o asterisco antes do parâmetro é obrigatório

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")
    # Como são parâmetros posicionais não definidos, é possível acessar a posição e o valor do argumento usando a estrutura de repetição "for" e a função "enumerate()"

print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "John")
# Chamada 1
# Quantidade de parâmetros = 4
# Posição = 0, valor = São Paulo
# Posição = 1, valor = 10
# Posição = 2, valor = 23.78
# Posição = 3, valor = John

print("\nChamada 2")
imprimir_parametros(10, "São Paulo")
# Chamada 2
# Quantidade de parâmetros = 2
# Posição = 0, valor = 10
# Posição = 1, valor = São Paulo

# "imprimir_parametros" foi definida a receber parâmetros arbitrários. A construção é feita passando como parâmetro o *args
# Nas chamadas feitas, cada uma com uma quantidade diferente de argumentos, mas a saída os argumentos seguem a ordem posicional. O primeiro para a posição 0, o segundo para a 1 e assim por diante
# Temos parâmetros posicionais indefinidos, a passagem de valores é feita de modo posicional, porém a quantidade não é conhecida

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    # será impresso o tipo do objeto recebido
    # len() = saber a quantidade de parâmetros que foram passados.
    # O parâmetro não precisa ser chamado de kwargs, mas é uma boa prática, mas o asterisco antes do parâmetro é obrigatório

    print(f"Quantidade de parâmetros {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor= {valor}")
        # items() = pertence a objetos tipo dicionário, por isso é a chamada é feita como "kwargs.items()": "objeto.função()"

print("\nChamada 1")
imprimir_parametros(cidade="Itabuna", idade=23, nome="John")
# Chamada 1
# Tipo de objeto recebido = <class 'dict'>
# Quantidade de parâmetros = 3
# variável = cidade, valor = Itabuna
# variável = idade, valor = 23
# variável = nome, valor = John

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)
# Chamada 2
# Tipo de objeto recebido = <class 'dict'>
# Quantidade de parâmetros = 2
# variável = desconto, valor = 10
# variável = valor, valor = 100

# "imprimir_parametros" foi definida para obter parâmetros nominais arbitrários, feita passando o parâmetro **kwargs
# Como são parâmetros posicionais não definidos, conseguimos acessar o "nome" da variável em que estão atribuídos o valor e o próprio "valor" do argumento, usando a estrutura de repetição "for" e a função "items()"
# A passagem é feita de modo nominal e não posicional, o que permite acessar tanto o valor do parâmetro quanto o nome da variável que o armazena


# FUNÇÕES ANÔNIMAS

(lambda x: x+1)(x=3)

# lambda = é usada para criar funções anônimas. Uma função anônima é uma função que não é construída com o "def", por isso não possui nome
# Esse tipo de construção é útil, quando a função faz somente uma ação e é usada uma única vez
# A função recebe como parâmetro um valor "x" e após os 2 pontos retorna esse valor somado a 1. Na frente da função já é invocado passando como parâmetro o valor x=3

(lambda x, y: x + y)(x=3, y=2)

# Criado função anônima que recebe como parâmetro dois valores e retorna a soma deles
# Foi usado a palavra reservada "lambda" e passado como parâmetro "x, y" e pós os 2 pontos é feito o cálculo x + y. Na frente da função já é invocado passando como parâmetro o valor x=3 e y=2
# A função anônima pode ser construída para receber mais de um parâmetro

somar = lambda x, y: x + y
somar(x=5, y=3)

# Podemos atribuir a uma variável uma função anônima, para invocar a função fazemos a chamada da variável
# Foi criado a função anônima e recebeu como parâmetro 2 valores e retorna a soma deles, essa função foi atribuída a uma variável chamada "somar"
# Foi feito a chamada da função através do nome da variável, passando os parâmetros que ela requer