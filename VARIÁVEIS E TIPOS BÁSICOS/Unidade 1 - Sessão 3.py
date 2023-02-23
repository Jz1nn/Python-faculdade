# FUNÇÕES

# Funções ja utilizadas:
# print(): imprimir um valor na tela.
# enumerate(): retornar a posição de um valor em uma sequência.
# input(): capturar um valor digitado no teclado.
# int() e float(): converter um valor no tipo inteiro ou float.
# range(): criar uma sequência numérica.
# type(): saber qual o tipo de um objeto (variável).


# FUNÇÃO eval()

a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")


# FUNÇÃO DEFINIDA PELO USUÁRIO

# Sintaxe de uma função:

# def nome_funcao():
    # bloco de comandos

# Os nomes das funções devem estar em minúsculas, com as palavras separadas por underline, conforme necessário, para melhorar a legibilidade. Os nomes de variáveis seguem a mesma convenção que os nomes de funções. Nomes com mixedCase (mistura de maiúsculas e minúsculas) são permitidos apenas em contextos em que o nome já existe com o formato recomendado.

def imprimir_mensagem(disciplina, curso):
        print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}")
    
imprimir_mensagem("Python", "ADS")

#  A função recebe duas variáveis locais.  São variáveis que existem somente dentro da função.

def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em python desenvolvida na disciplina: {disciplina}, dp curso {curso}.")

resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")

# Para que o resultado de uma função possa ser guardado em uma variável, a função precisa ter o comando "return". A instrução "return", retorna um valor de uma função.

def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}."

mensagem = imprimir_mensagem("Python", "ADS")
print(mensagem)

# Vamos implementar uma função que recebe uma data no formato dd/mm/aaaa e converte o mês para extenso. Então, ao se receber a data 10/05/2020, a função deverá retornar: 10 de maio de 2020.

def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
    # split() "quebra" a string a cada espaço em branco, criando uma lista e elementos.

    d, m, a = data.split('/')
    # Usamos novamente a função split(), mas agora passando como parâmetro o caractere '/', isso quer dizer que a string será cortada sempre que ele aparecer. Nessa linha também usamos a atribuição múltipla. Ao cortar a string 'dd/mm/aaaa', temos uma lista com três elementos: ['dd', 'mm', 'aaaa'], ao usar a atribuição múltipla, cada valor da lista é guardado dentro de uma variável, na ordem em que foram declaradas. Então d = 'dd', m = 'mm', a = 'aaaa'. O número de variáveis tem que ser adequado ao tamanho da lista, senão ocorrerá um erro.

    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    # Aqui estamos fazendo a conversão do mês para extenso. Veja que buscamos na lista "mes" a posição m - 1, pois, a posição inicia em 0. Por exemplo, para o mês 5, o valor "maio", estará na quarta posição a lista "mes".

    return f'{d} de {mes_extenso} de {a}'
    # Retornamos a mensagem, agora com o mês em extenso.

print(converter_mes_para_extenso('10/05/2021'))

# Invocamos a função, passando como parâmetro a data a ser convertida.

# FUNÇÕES COM PARÂMETROS DEFINIDOS E INDEFINIDOS

# Sobre os argumentos que uma função pode receber, para nosso estudo, vamos classificar em seis grupos:

# Parâmetro posicional, obrigatório, sem valor default (padrão).
# Parâmetro posicional, obrigatório, com valor default (padrão).
# Parâmetro nominal, obrigatório, sem valor default (padrão).
# Parâmetro nominal, obrigatório, com valor default (padrão).
# Parâmetro posicional e não obrigatório (args).
# Parâmetro nominal e não obrigatório (kwargs).

# O grupo de parâmetros 1, temos os parâmetros que vão depender da ordem em que forem passados, por isso são chamados de posicionais (a posição influencia o resultado). Os parâmetros desse grupo são obrigatórios, ou seja, tentar um invocar a função, sem passar os parâmetros, acarreta um erro. Além disso, os parâmetros não possuem valor default.

def somar(a, b):
    return a + b

r = somar(2)
print(r)

# TypeError: somar() missing 1 required positional argument: 'b'
# A função "somar" foi definida para receber dois parâmetros, porém quando foi invocada, somente um foi passado. "falta 1 argumento posicional obrigatório"
# Deve ser invocada passando os dois argumentos, por exemplo: r = somar(2, 3).

# O grupo de parâmetros 2, também temos os parâmetros posicionais e obrigatórios, porém vamos definir um valor default (padrão), assim, quando a função for invocada, caso nenhum valor seja passado, o valor default é utilizado.

def calcular_desconto(valor, desconto=0): # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #Não aplicar nenhum desconto
valor2 = calcular_desconto(100,0.25) #Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

# Para o conceito de parâmetros posicionais não existe nenhum erro de interpretação associado, ou seja, o interpretador não irá informar o erro, mas pode haver um erro de lógica.

def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrar_pessoa("João", 23, "São Paulo")
# Dados a serem cadastrados:
# Nome: João
# Idade: 23
# Cidade: São Paulo

cadastrar_pessoa("São Paulo", "João", 23)
# Dados a serem cadastrados:
# Nome: São Paulo
# Idade: João
# Cidade: 23

# A posição dos argumentos, na hora de chamar a função, deve ser conhecida e respeitada, pois a passagem dos valores na posição incorreta pode acarretar erros lógicos.

# O grupo de parâmetros 3 é caracterizado por ter parâmetros nominais, ou seja, agora não mais importa a posição dos parâmetros, pois eles serão identificados pelo nome, os parâmetros são obrigatórios, ou seja, na chamada da função é obrigatório passar todos os valores e sem valor default (padrão).

def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
            return texto.lower()

texto = converter_maiuscula(flag_maiuscula=True, texto="João") #Passagem nominal dos parâmetros
print(texto)

# Caso "flag_maiuscula" seja True, a função deve converter o texto recebido em letras maiúsculas, caso contrário, em minúsculas
# Como a função "converter_maiuscula" não possui valores default para os parâmetros, então a função deve ser invocada passando ambos valores.
#  Não houve um erro lógico? Isso acontece porque a chamada foi feita de modo nominal, ou seja, atribuindo os valores às variáveis da função e, nesse caso, a atribuição não é feita de modo posicional.

# O grupo de funções da categoria 4 é similar ao grupo 3: parâmetro nominal, obrigatório, mas nesse grupo os parâmetros podem possuir valor default (padrão).

def converter_minuscula(texto, flag_minuscula=True): # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()

texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")

# O parâmetro flag_minuscula, caso não seja passado na chamada da função, receberá o valor True.
# Na chamada "texto2", passamos somente o texto.
# Para ambas as chamadas o resultado foi o mesmo, devido o valor default atribuído na função. Se não quiséssemos o comportamento default, aí sim precisaríamos passar o parâmetro:
# "texto = converter_minuscula(flag_minuscula=False, texto="LINGUAGEM de Programação")."

# Todas as funções que criamos, sabemos exatamente o número de parâmetros que ela recebe. Mas existem casos em que esses parâmetros podem ser arbitrários, ou seja, a função poderá receber um número diferente de parâmetros a cada invocação.

# O grupo de funções da categoria 5 temos parâmetros posicionais indefinidos, ou seja, a passagem de valores é feita de modo posicional, porém a quantidade não é conhecida.

def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")
        
print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "John")

# Chamada 1
# Quantidade de parâmetros = 4
# Posição = 0, valor = São Paulo
# Posição = 1, valor = 10
# Posição = 2, valor = 23.78
# Posição = 3, valor = João

print("\nChamada 2")
imprimir_parametros(10, "São Paulo")

# Chamada 2
# Quantidade de parâmetros = 2
# Posição = 0, valor = 10
# Posição = 1, valor = São Paulo

# A função "imprimir_parametros" foi definida de modo a obter parâmetros arbitrários. Tal construção é feita, passando como parâmetro o *args.
# O parâmetro não precisa ser chamado de args, mas é uma boa prática. Já o asterisco antes do parâmetro é obrigatório.

# Usamos a função built-in "len()" (length) para saber a quantidade de parâmetros que foram passados.Como se trata de parâmetros posicionais não definidos, conseguimos acessar a posição e o valor do argumento, usando a estrutura de repetição "for" e a função "enumerate()". 

# Nas chamadas feitas, cada uma com uma quantidade diferente de argumentos, mas veja na saída que os argumentos seguem a ordem posicional, ou seja, o primeiro vai para a posição 0, o segundo para a 1 e assim por diante.


# O grupo de funções da categoria 6 é similar ao grupo 5: porém agora a passagem é feita de modo nominal e não posicional, o que nos permite acessar tanto o valor do parâmetro quanto o nome da variável que o armazena.

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)

    # Estamos imprimindo o tipo de objeto recebido, você pode ver na saída que é um "dict" (dicionário), o qual estudaremos nas próximas aulas.

    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros(cidade="Itabuna", idade=33, nome="John")

# Chamada 1
# Tipo de objeto recebido = <class 'dict'>

# Quantidade de parâmetros = 3
# variável = cidade, valor = São Paulo
# variável = idade, valor = 33
# variável = nome, valor = João

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)

# Chamada 2
# Tipo de objeto recebido = <class 'dict'>

# Quantidade de parâmetros = 2
# variável = desconto, valor = 10
# variável = valor, valor = 100

# A função "imprimir_parametros" foi definida de modo a obter parâmetros nominais arbitrários. Tal construção é feita, passando como parâmetro o "**kwargs". 
# O parâmetro não precisa ser chamado de kwargs, mas é uma boa prática. Já os dois asteriscos antes do parâmetro é obrigatório.
# Usamos a função built-in "len()" (length) para saber a quantidade de parâmetros que foram passados.
# Como se trata de parâmetros nominais não definidos, conseguimos acessar o (nome) da variável em que estão atribuídos o (valor) e o próprio "valor" do argumento, usando a estrutura de repetição "for" e a função "items()".

# A função "items" não é built-in, ela pertence aos objetos do tipo dicionário, por isso a chamada é feita como "kwargs.items()" (ou seja, (objeto.função)).
# Agora observe as chamadas feitas, cada uma com uma quantidade diferente de argumentos, mas veja na saída que os argumentos estão associados ao nome da variável que foi passado.


# FUNÇÕES ANÔNIMAS EM PYTHON

# A expressão "lambda" (às vezes chamadas de formas lambda) são usadas para criar funções anônimas.
# Uma função anônima é uma função que não é construída com o "def" e, por isso, não possui nome. 
# Esse tipo de construção é útil, quando a função faz somente uma ação e é usada uma única vez.

(lambda x: x+1)(x=3)

# Criamos uma função que recebe como parâmetro um valor e retorna esse valor somado a 1. 
# Para criar essa função anônima, usamos a palavra reservada "lambda" passando como parâmetro "x".
# O dois pontos é o que separa a definição da função anônima da sua ação.
# Após os dois pontos, é feito o cálculo matemático x + 1. 
# Na frente da função, já a invocamos passando como parâmetro o valor x=3.

# A função anônima pode ser construída para receber mais de um parâmetro.

(lambda x, y: x + y)(x=3, y=2)

# Criamos uma função anônima que recebe como parâmetro dois valores e retorna a soma deles.
# Para criar essa função anônima, usamos a palavra reservada "lambda" passando como parâmetro "x, y". 
# Após os dois pontos, é feito o cálculo matemático x + y. 
# Na frente da função, já a invocamos passando como parâmetro o valor x=3 e y=2.

# A linguagem Python, nos permite atribuir a uma variável uma função anônima, dessa forma, para invocar a função, fazemos a chamada da variável.

somar = lambda x, y: x + y
somar(x=5, y=3)

# Criamos uma função anônima que recebe como parâmetro dois valores e retorna a soma deles.
# Essa função foi atribuída a uma variável chamada "somar".
# Fazemos a chamada da função através do nome da variável, passando os parâmetros que ela requer.