# UNIDADE 2

### SESSÃO 1
# ESTRUTURAS DE DADOS

# Objetos são usados ​​para armazenar várias estruturas de dados e permitem funções diferentes para cada tipo. A escolha da estrutura depende do problema
# Tipo sequência: texto, listas e tuplas
# Tipo set (conjunto)
# Tipo mapping (dicionário)
# Tipo array NumPy


# OBJETOS DO TIPO SEQUÊNCIA

# Objetos sequenciais armazenam múltiplos valores e representam sequências finitas indexadas por números não negativos. A primeira posição da sequência é representada pelo índice 0 e a última posição é representada pelo índice n-1, onde 'n' é a capacidade de armazenamento da sequência. Ex: [0, 1, 2, 3, 4, 5... n... n-1]

# SEQUÊNCIA DE CARACTERES:

# Texto é um objeto da classe str (string) e possuem todas as operações. Não é possível atribuir um novo valor a uma posição específica em objetos str, porque eles são imutáveis

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
    # Tamanho do texto = 60
    # Python in texto = False
    # Quantidade de y no texto = 1
    # As 5 primeiras letras são: Aprend

# len() = saber o tamanho da sequência
# in = saber se um determinado valor está ou não na sequência
# count = contar a quantidade de ocorrências de um valor, o ('') permite fatiar a sequência, exibindo partes dela
# texto[0:6] = exibir posição 0 a 5, o 6 não é incluído


# Outras métodos da classe str:
# lower() = transformar um objeto str para letras minúsculas
# upper() = transformar em maiúsculo
# replace() = substituir um caractere por outro

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(texto.upper())
print(texto.replace("i", 'XX'))
    # APRENDENDO PYTHON NA DISCIPLINA DE LINGUAGEM DE PROGRAMAÇÃO.
    # Aprendendo Python na dXXscXXplXXna de lXXnguagem de programação.


# split() = cortar um texto e transformá-lo em lista. Pode ser usada sem nenhum parâmetro: texto.split(), a str será cortada a cada espaço em branco que for encontrado
# Se for passado um parâmetro: texto.split(","), o corte será feito no parâmetro especificado

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")
    # texto = Aprendendo Python na disciplina de linguagem de programação.
    # Tamanho do texto = 60

    # palavras = ['Aprendendo', 'Python', 'na', 'disciplina', 'de', 'linguagem', 'de', 'programação.']
    # Tamanho de palavras = 8

# O "texto" tem tamanho 60, pois possui uma sequência de 60 caracteres
# split() = cortar o texto em cada espaço em branco e guarda o resultado na variável "palavras"
# O tamanho da variável "palavras" é 8, ao cortar o texto é criado uma lista com as palavras


# ANÁLISE DE TEXTO:

# Saber quantas vezes é mencionado a palavra "string" ou "strings":

texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor."""

print(f"Tamanho do texto = {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace(")", "").replace("(", "").replace("\n", "")
lista_palavras = texto.split()

print(f"texto = {texto}")
print(f"Tamanho da lista em palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total}")
    # Tamanho do texto = 323
    # texto = Operadores de StringPython oferece operadores para processar texto ou seja valores de stringAssim como os números as strings podem ser comparadas usando operadores de comparação:== != < > e assim por dianteO operador == por exemplo retorna True se as strings nos dois lados do operador tiverem o mesmo valor
    # Tamanho da lista de palavras = 50
    # Quantidade de vezes que string ou strings aparecem = 2

# Criado variável "texto", aplicado função lower() à string para que todo o conteúdo fique em letras minúsculas e guarde o resultado dentro da própria variável, sobrescrevendo o texto original
# replace() = feito série encadeada de transformações, substituindo o 1º parâmetro pelo 2º. (",", "") substituindo todas as vírgulas por nada e assim por diante. ("\n", "") as quebras de linha por um espaço em branco
# texto.split() = criar lista aplicando a função ao texto. Sempre que houver um espaço em branco, a string será cortada, criando um novo elemento na lista. Criado lista com 58 elementos na variável "lista_palavras"
# count() = contar tanto a palavra "string" no singular quanto no plural "strings". A função retorna um número inteiro, é somado os resultados e é exibido


# LISTAS

# Uma lista é uma estrutura de dados sequencial que é mutável, ou seja, novos valores podem ser acrescentados ou removidos da sequência.

# Formas de construir listas:
# lista1 = [] # par de colchetes para lista vazia
# lista = ['a', 'b', 'c'] # par de colchetes e elementos separados por vírgulas
# list comprehension = [x for x in iterable]
# list() = construtor

# Objetos do tipo sequência são indexados, cada elemento ocupa uma posição que começa em 0. Um objeto de 5 elementos tem índices que variam entre 0 e 4. [0,1,2,3,4] = 5 elementos

vogais = ['a', 'e', 'i', 'o', 'u'] # pode ser criado usando ""

for vogal in vogais:
    print(f'posição = {vogais.index(vogal)}, valor = {vogal}')
    # posição = 0, valor = a
    # posição = 1, valor = e
    # posição = 2, valor = i
    # posição = 3, valor = o
    # posição = 4, valor = u

# Criado lista "vogais" e usando uma estrutura de repetição, é impresso cada elemento da lista e seu índice usando a função {vogais.index()}

vogais = []

print(f"Tipo de vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")
    # Tipo de vogais = <class 'list'>
    # Posição = 0, valor = a
    # Posição = 1, valor = e
    # Posição = 2, valor = i
    # Posição = 3, valor = o
    # Posição = 4, valor = u

# Criado lista vazia, por conta do [] mesmo estando vazia, o tipo da classe é "list", pois o [] é sintaxe para construção de listas
# append() = adiciona um novo valor ao final da lista. vogais.append(valor) significa que é do objeto lista
# enumerate() = percorre um objeto iterável e retorna um objeto que gera tuplas contendo um índice e o valor correspondente em cada iteração
# for p, x in = na estrutura de repetição é usado variáveis 'p' e 'x', a 1º guarda a posição e a 2º o valor. O nome da variável x é opcional

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas)
print("abacate" in frutas)
print("abacate" not in frutas)
print(min(frutas))
print(max(notas))
print(frutas.count("maça"))
print(frutas + notas)
print(2 * frutas)
    # True
    # False
    # True
    # banana
    # 10
    # 2
    # ['maça', 'banana', 'uva', 'mamão', 'maça', 8.7, 5.2, 10, 3.5]
    # ['maça', 'banana', 'uva', 'mamão', 'maça', 'maça', 'banana', 'uva', 'mamão', 'maça']

# Testado se valores "maça" e "abacate" estavam na lista e os resultados foram True e False. Testado se "abacate" NÃO ESTÁ na lista e o resultado foi True.
# min() e max() = saber o menor e o maior valor de cada lista. O mínimo da lista de palavras é feito pela ordem alfabética
# frutas.count("maça") = contar quantas vezes a palavra maça aparece na lista
# Concatenado as duas listas e multiplicado por 2 a lista de frutas, no resultado foi criado uma cópia da lista e adicionada no final


# A construção da lista apresenta semelhanças com a construção de arrays e é um objeto muito versátil, pois permite a mistura de vários tipos de dados durante a sua criação

# Fatiamento (slice):

lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]
print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i}, \t valor = {item} -----------------> tipo individual = {type(item)}")

print("\nExemplos de slices:\n")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])
    # Tamanho da lista = 6
    # Posição = 0,     valor = Python -----------------> tipo individual = <class 'str'>
    # Posição = 1,     valor = 30.61 -----------------> tipo individual = <class 'float'>
    # Posição = 2,     valor = Java -----------------> tipo individual = <class 'str'>
    # Posição = 3,     valor = 51 -----------------> tipo individual = <class 'int'>
    # Posição = 4,     valor = ['a', 'b', 20] -----------------> tipo individual = <class 'list'>
    # Posição = 5,     valor = maça -----------------> tipo individual = <class 'str'>

    # Exemplos de slices:
    # lista[1] =  30.61
    # lista[0:2] =  ['Python', 30.61]
    # lista[:2] =  ['Python', 30.61]
    # lista[3:5] =  [51, ['a', 'b', 20]]
    # lista[3:6] =  [51, ['a', 'b', 20], 'maça']
    # lista[3:] =  [51, ['a', 'b', 20], 'maça']
    # lista[-2] =  ['a', 'b', 20]
    # lista[-1] =  maça
    # lista[4][1] =  b

# Criado LISTA que possui: texto, número (float e int) e lista (lista dentro de outra lista)
# É possível colocar uma estrutura de dados dentro de outra, mesmo que não sejam do mesmo tipo.É possível inserir um dicionário dentro de uma lista
# enumerate() = indica conteúdo de cada índice

# Exemplos de slices:
# lista [1] = valor da posição 1 da lista
# lista[0:2] = valores que estão entre posição 0 e 2 (limite superior não incluído): valores das posições 0 e 1 
# lista[:2] = um dos limites não informado: considera o limite máximo. [:2] = não informado limite inferior, 0 a 2 (2 não incluído)
# lista[3:5] = valores que estão entre posição 3 (incluído) e 5 (não incluído). Limite inferior sempre incluído
# lista[3:6] = valores que estão entre posição 3 e 5, para usar todos os elementos da lista, incluindo o ultimo, deve fazer o slice com o limite superior do tamanho da lista [:6] # tamanho da lista: 6
# lista[3:] = não informar o limite superior pega todos os elementos da lista até o último
# lista[-2] = slice usando índice negativo é interpretado de trás pra frente: índice -2 quer dizer o penúltimo elemento da lista
# lista[-1] = índice -1 representa o último elemento da lista
# lista[4][1] = o índice 5 da lista há uma outra lista, usado mais um colchete para conseguir acessar um elemento específico dessa lista interna


# LIST COMPREHENSION (COMPREENSÕES DE LISTA)

# listcomp = técnica utilizada para criar uma nova lista a partir de um objeto iterável. É útil quando se deseja transformar ou filtrar as informações de uma sequência original para criar uma nova sequência

# Lista de palavras e quero padronizá-la em minúsculo:

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
    # linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # MESMO RESULTADO

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)
    # Antes da listcomp =  ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']
    # Depois da listcomp =  ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']

# Criado lista chamada "linguagens" contendo linguagens de programação. split() cria uma lista com base em um texto
# linguagens = []: é usado [] porque se trata da criação de uma lista, dentro do [] há uma variável "item" que representa cada valor da lista original
# item.lower() for item in linguagens = transformado cada valor da lista em minúsculo e guardado na mesma variável, sobrescrevendo a original

# Listcomp é uma forma de escrever "for"
# Outra opção:

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

print("\nDepois da listcomp = ", linguagens)

# Listcomp para construir uma lista com somente as linguagens que possuem a palavra "Java"

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)
    # ['Java', 'JavaScript']

# Listcomp usa uma estrutura "if" para criar um filtro. Apenas as variáveis que contêm "Java" serão incluídas na nova lista. Dois itens da lista original satisfazem esse critério
# x in s = "x está em s?". Java está em JavaScript

# Filtro que retorna só palavras idênticas:
# linguagens_java = [item for item in linguagens if "Java" == item]

# Outro método com mais instruções:

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java  = []

for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

        print(linguagens_java)
        # ['Java', 'JavaScript']
    

# MAP() E FILTER()

# map() = usada para aplicar uma função a cada item de um objeto iterável. map() requer a passagem de dois argumentos: a função e o objeto iterável.

print("Exemplo 1")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")
    # Exemplo 1
    # A nova lista é = <map object at 0x0000012336F1AAA0>
    # Agora sim, a nova lista é = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']

print("\n\nExemplo 2")
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x*x, numeros))
print(f"Lista com número elevado a ele mesmo = {quadrados}\n")
    # Exemplo 2
    # Lista com número elevado a ele mesmo = [0, 1, 4, 9, 16, 25]

# Exemplo 1: map() = criado lista e transformado cada palavra da lista em letras minúsculas. Usado função "lambda" porque o primeiro parâmetro deve ser uma função
# <map object...> = map() retorna um objeto iterável, para ver o resultado é necessário transformar o objeto em uma lista usando o "list()" para fazer a conversão

# Exemplo 2: criado lista numérica e usado a função "lambda()" para elevar cada número da lista a ele mesmo (quadrado do número). Feito conversão do resultado da função "map()" para o tipo "list()"


# filter() = tem as mesmas características da função map(), mas ao invés de usar a função para transformar valores da lista, é usado para filtrar

numeros = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# range() = cria um objeto numérico iterável
# list() = transforma o objeto em uma lista com números de 0 a 20 (limite superior não incluído)
# filter() = cria nova lista e com a utilização da expressão "lambda()" retorna somente os valores pares


# TUPLAS

# Pertencem ao grupo de objetos de dados do tipo sequência. Listas e tuplas são tipos diferentes de sequências, a diferença é que as listas são mutáveis (possível atribuir valores a posições usando a notação de índice): lista[2] = 'maça'. Nas TUPLAS não é possível (são imutáveis)

# Formas de construir tuplas:
# tupla1 = () # par de parênteses para tupla vazia
# tupla2 = ('a', 'b', 'c') # par de parênteses e elementos separados por vírgulas
# tuple() = construtor

# Criar tupla chamada "vogais" e por meio da estrutura de repetição, imprimir cada elemento da tupla. Usado variável auxiliar "p" para indicar a posição que o elemento ocupa na tupla

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo de objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")
    # Tipo de objeto vogais = <class 'tuple'>
    # Posição = 0, valor = a
    # Posição = 1, valor = e
    # Posição = 2, valor = i
    # Posição = 3, valor = o
    # Posição = 4, valor = u

# Embora possam parecer semelhantes, há diferenças entre LISTAS E TUPLAS. Em alguns casos mais de uma estrutura pode ser usada para resolver o problema, enquanto em outros apenas uma é adequada. Embora os objetos possam ter operações em comum, cada objeto tem suas próprias operações e métodos específicos

# USANDO FUNÇÃO APPEND() EM UMA TUPLA:

vogais = ()

vogais.append('a')
    # AttributeError: 'tuple' object has no attribute 'append'

vogais = ('a', 'e', 'i', 'o', 'u')

for item in enumerate(vogais):
    print(item)
    # print(tuple(enumerate(vogais)))
    # print(list(enumerate(vogais)))

    # (0, 'a')
    # (1, 'e')
    # (2, 'i')
    # (3, 'o')
    # (4, 'u')

# AttributeError... = tupla não possui operação "append()". A tupla é imutável, é usado em casos que a ordem dos elementos é importante e não pode ser alterada (objeto tuple garante essa característica)

# enumerate() = usada normalmente em estruturas de repetição, retorna uma tupla. O primeiro é o índice da posição e o segundo é o elemento do valor
# Para cada item de um enumerate() é impresso uma tupla

# Comentado duas formas de ver o resultado da função enumerate(): 1º usado construtor tuple() para transformar o resultado em uma tupla (feito tupla de tuplas), o 2º usado construtor list() para transformar o resultado em uma lista de tuplas


# OBJETOS DO TIPO SET

# O objeto do tipo SET habilita operações matemáticas de conjuntos: união, intersecção, diferença, etc. Pode ser usado em testes de associação e remoção de valores duplicados de uma sequência

# Operações de sequências que pode ser usado na estrutura SET: len(s), x in s, x not in s

# add(valor) = além das operações anteriores, é possível adicionar um novo elemento a um conjunto
# remove(valor) = remover elemento a um conjunto


# Formas de construir objetos tipo SET:
# set1 = {'a', 'b', 'c'} # par de chaves e elementos separados por vírgulas
# set(iterable) = construtor
# Não é possível criar um SET vazio: set = {}. Essa é uma forma de construção de um dicionário

# set (iterable) = obrigatoriamente deve passar um objeto iterável para ser transformado em conjunto. O objeto pode ser uma lista, uma tupla ou uma string (tipo de sequência)

vogais_1 = {'aeiou'} # sem o construtor
print(type(vogais_1), vogais)

vogais_2 = set('aeiouaaaaa') # construtor com string
print(type(vogais_2), vogais_2)

vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print(type(vogais_3), vogais_3)

vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print(type(vogais_4), vogais_4)

print(set('banana'))
    # <class 'set'> {'aeiou'}
    # <class 'set'> {'a', 'e', 'i', 'u', 'o'}
    # <class 'set'> {'a', 'e', 'i', 'u', 'o'}
    # <class 'set'> {'a', 'e', 'i', 'u', 'o'}
    # {'n', 'b', 'a'}

# Construção de objetos do tipo SET. Com exceção do 1º (não foi usado construtor set()), os demais resultam na mesma estrutura

# Exemplo 2: passado parâmetro de uma sequência de caracteres 'aeiouaaaaa' (repetindo a vogal 'a')
# O construtor interpreta como iterável e cria um conjunto em que cada caractere é um elemento (eliminando valores duplicados), por isso a string banana, são eliminados os 'a' duplicados


# Exemplo da utilidade do objeto SET:
# Uma loja de informática recebeu componentes usados de um computador para avaliar se estão com defeito. As peças que não estiverem com defeito podem ser colocadas à venda

def create_report():
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])

    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)

    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")

    print("Os componentes que podem ser vendidos são:")
    for item in componentes_ok:
        print(item)

create_report()
    # Foram verificados 23 componentes.
    # 4 componentes apresentaram defeito.
    # Os componentes que podem ser vendidos são:
    # mouse
    # cpu
    # impressora
    # cooler
    # joystick
    # caixas de som
    # placa de captura
    # gabinete
    # microfone
    # placa de vídeo
    # webcam
    # hub
    # dissipador de calor
    # teclado
    # estabilizador
    # placa mãe
    # no-break
    # memória ram
    # modem

# Criado função que gera o relatório das peças aptas a serem vendidas. Criados 2 objetos set: "componentes_verificados" e "componentes_com_defeito"
# len() = saber quantos itens há em cada conjunto
# difference() = obter os itens que estão em componentes_verificados, mas não em componentes_com_defeito
# Também poderia ser feito com o sinal de subtração: componentes_ok = componentes_verificados - componentes_com_defeito


# OBJETOS DO TIPO MAPPING

# Objetos do tipo MAPPING possuem um mapeamento entre uma chave e um valor. O dicionário em um exemplo de objeto que possui essa propriedade, sendo considerado uma estrutura de dados desse tipo. Dicionário é um objeto mutável, permitindo a atribuição de um novo valor a uma chave já existente

# Formas de construir dicionários:
# dicionario1 = {} # par de chaves para denotar um DICT vazio
# dicionario2 = {'one': 1, 'two': 2, 'three': 3} # par de elementos (chave : valor) separados por vírgulas
# dict() = construtor

# EXEMPLOS:

# dicionário vazio, com atribuição posterior de chave e valor
dici_1 = {}
dici_1['nome'] = "John"
dici_1['idade'] = 23

# chave : valor
dici_2 = {'nome': 'John', 'idade': 23}

# dicionário com lista de tuplas cada tupla representa um par (chave : valor)
dici_3 = dict([('nome', "John"), ('idade', 23)])

# zip() e duas listas, uma com chaves e outra com valores
dici_4 = dict(zip(['nome', 'idade'], ["John", 23]))

print(dici_1 == dici_2 == dici_3 == dici_4) # testar se as diferentes construções resultam em objetos iguais
    # True

# Criado 4 sintaxes distintas para criar e atribuir valores a um dicionário:
# 1: dicionário vazio, criado chaves e atribuído valores posteriormente
# 2: dicionário com chaves e valores
# 3: dict() = criar o dicionário passando como parâmetro uma lista de tuplas: dict([(tupla 1), (tupla 2)]), cada tupla é uma combinação de chave e valor
# 4: dict(zip([])) = construtor dict e função zip para combinar valores de diferentes sequências e retornar um iterável de duplas. 1º elemento é referente ao primeiro elemento da sequência 1 e assim por diante

# Testado se as construções produzem o mesmo objeto

# nome_dicionario[chave] = acessar um valor do dicionário
# nome_dicionario[chave] = novo_valor ## atribuir novo valor

# Uma única chave de um dicionário pode estar associada a vários valores por meio de uma lista, tupla ou outro dicionário (podendo acessar elementos internos)


# keys() = retorna uma lista com todas as chaves de um dict
# values() = retorna uma lista com todos os valores
# items() = retorna uma lista de tuplas, cada uma é um par chave-valor

cadastro = {
    'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
    'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
    'idade' : [25, 33, 37, 18]
    }

print("len(cadastro) = ", len(cadastro))

print("\n cadastro.keys() = \n", cadastro.keys())
print("\n cadastro.values() = \n", cadastro.values())
print("\n cadastro.items() = \n", cadastro.items())

print("\n cadastro['nome'] = ", cadastro['nome'])
print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])
    # len(cadastro) =  3

    # cadastro.keys() =
    # dict_keys(['nome', 'cidade', 'idade'])

    # cadastro.values() =
    # dict_values([['João', 'Ana', 'Pedro', 'Marcela'], ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'], [25, 33, 37, 18]])

    # cadastro.items() =
    # dict_items([('nome', ['João', 'Ana', 'Pedro', 'Marcela']), ('cidade', ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba']), ('idade', [25, 33, 37, 18])])

    # cadastro['nome'] =  ['João', 'Ana', 'Pedro', 'Marcela']
    # cadastro['nome'][2] =  Pedro
    # cadastro['idade'][2:] =  [37, 18]

# Criado dict que cada chave está associada a uma lista de valores
# len() = diz que o dict possui tamanho 3, pois conta quantas chaves existem no dict
# cadastro.keys() = retorna uma lista com todas as chaves do dict
# cadastro.values() = retorna uma lista com os valores, como os valores também sao listas, temos uma lista de listas
# cadastro.items() = retorna uma lista de tuplas, cada uma é composta pela chave e valor
# cadastro['nome'] = acessa o valor atribuído à chave 'nome' (lista de nomes)
# cadastro['nome'][2] = acessa o valor na posição 2 da lista atribuída à chave 'nome'
# cadastro['idade'][2:] = acessa os valores da posição 2 até o final da lista atribuída a chave 'idade'


# len() = retorna quantas chaves um dict possui. Para saber o total de elementos somando quantos há em cada chave: como é possível acessar os valores de cada chave, basta contar quantos eles são

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f"\n\nQuantidade de elementos do dicionário = {qtde_itens}")
    # 4
    # 4
    # 4
    # Quantidade de elementos do dicionário = 12

# Impresso a quantidade de elementos atribuídos a cada chave. Caso tivesse centenas de chaves, independentemente de quantas chaves e valores existam, é possível criar uma LIST COMPREHENSION
# Foi usado a função "len()" para cada chave, criando uma lista de valores inteiros. Foi aplicado a função "sum()" para somar e obter a quantidade total de itens


# OBJETOS DO TIPO ARRAY NUMPY

# A biblioteca NumPy contém:
# Objeto de matriz (array) N-dimensional
# Funções sofisticadas
# Ferramentas para integrar o código C/C++ e Fortran
# Recursos de álgebra linear, transformação de Fourier e números aleatórios

# NumPy é a melhor biblioteca para trabalhar com dados tabulares (matrizes), recurso essencial para desenvolver soluções de inteligência artificial para imagens

# pip install numpy = é preciso instalar a biblioteca NumPy usando esse comando
# import numpy = além de instalar, sempre que for usar recursos da biblioteca, é necessário importar a biblioteca para o projeto

import numpy

matriz_1_1 = numpy.array([1, 2, 3]) # matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # matriz 2 linhas e 3 colunas

print(type(matriz_1_1))

print('matriz_1_1 = ', matriz_1_1)
print('matriz_2_2 = \n', matriz_2_2)
print('matriz_3_2 = \n', matriz_3_2)
print('matriz_2_3 = \n', matriz_2_3)
    # <class 'numpy.ndarray'>
    # matriz_1_1 =  [1 2 3]
    # matriz_2_2 =
    #  [[1 2]
    #  [3 4]]
    # matriz_3_2 =
    #  [[1 2]
    #  [3 4]
    #  [5 6]]
    # matriz_2_3 =
    #  [[1 2 3]
    #  [4 5 6]]

# Criado várias formas de matrizes com a biblioteca NumPy:
# importado a biblioteca para usar seus objetos e funções
# numpy.array(forma) = criar matriz, em que "forma" são listas que representam as linhas e colunas
# Criado matrizes, respectivamente, com 3 linhas 2 colunas e 2 linhas e 3 colunas
# A diferença de uma construção para outra é que para construir 3 lias com 2 colunas, foi usado 3 listas internas com 2 valores, e para construir 2 linhas com 3 colunas, foi usado 2 listas com 3 valores cada

# Construções de matrizes usadas em álgebra linear ja prontas com um único comando:

m1 = numpy.zeros((3, 3)) # matriz 3 x 3 somente com zero
m2 = numpy.ones((2,2)) # matriz 2 x 2 somente com um
m3 = numpy.eye(4) # matriz 4 x 4 identidade
m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) # Cria uma matriz 2 x 5 com números inteiros.

print('\n numpy.zeros((3x 3)) = \n', numpy.zeros((3, 3)))
print('\n numpy.ones((2,2)) = \n', numpy.ones((2,2)))
print('\n numpy.eye(4) = \n', numpy.eye(4))
print('\n m4 = \n', m4)

print(f"Soma dos valores em m4 = {m4.sum()}")
print(f"Valor mínimo em m4 = {m4.min()}")
print(f"Valor máximo em m4 = {m4.max()}")
print(f"Média dos valores em m4 = {m4.mean()}")
    # numpy.zeros((3x 3)) =
    # [[0. 0. 0.]
    # [0. 0. 0.]
    # [0. 0. 0.]]
    # numpy.ones((2,2)) =
    # [[1. 1.]
    # [1. 1.]]
    # numpy.eye(4) =
    # [[1. 0. 0. 0.]
    # [0. 1. 0. 0.]
    # [0. 0. 1. 0.]
    # [0. 0. 0. 1.]]
    # m4 =
    # [[84 88 85 94 81]
    # [37 60 80  5 62]]
    # Soma dos valores em m4 = 676
    # Valor mínimo em m4 = 5
    # Valor máximo em m4 = 94
    # Média dos valores em m4 = 67.6

# Criado matrizes somente com 0, com 1 e matriz identidade (1 na diagonal principal) usando comandos específicos
# A matriz 'm4' foi criada usando a função que gera números inteiros aleatórios
# reshape() = para transformá-los em uma matriz com 2 linhas e 5 colunas
# usado funções que extraem informações estatísticas básicas de um conjunto numérico


# DESAFIO

# Crie uma função que receba dois dicionários contendo informações de candidatos inscritos em um concurso que foi adiado e que ainda precisam ser avisados da alteração. Cada dicionário possui três chaves: nome, email e enviado. A chave nome é associada a uma lista de nomes, a chave email é associada a uma lista de e-mails e a chave enviado é associada a uma lista de valores booleanos que indica se o e-mail correspondente já foi enviado ou não. A função deve retornar uma lista com os e-mails que ainda não foram enviados. 

# Exemplo:
dict_x = {
'nome': ['nome_1'],
'email': ['email_1'],
'enviado': [False]
}

# Considere que os dados passados para a função são:

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

# RESOLUÇÃO:

def extrair_lista_email(dict_1, dict_2):
    lista_1 = list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    print(f"Amostra da lista 1 = {lista_1[0]}")

    lista_2 = list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))

    dados = lista_1 + lista_2

    print(f"\nAmostra de dados = \n{dados[:2]}\n\n")

    # Lista com email de quem ainda não recebeu o aviso
    emails = [item[1] for item in dados if not item[2]]

    return emails

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

emails = extrair_lista_email(dict_1=dados_1, dict_2=dados_2)
print(f"E-mails a serem enviados = \n {emails}")
    # Amostra da lista 1 = ('Sonia Weber', 'Lorem.ipsum@cursusvestibulumMauris.com', False)

    # Amostra de dados =
    # [('Sonia Weber', 'Lorem.ipsum@cursusvestibulumMauris.com', False), ('Daryl Lowe', 'auctor@magnis.org', False)]


    # E-mails a serem enviados =
    #  ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu', 'at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'dolor.tempus.non@ipsum.net', 'felis@urnaconvalliserat.org']

# extrair_lista_email = recebe 2 dicionários de dados como parâmetro
# lista_1 = lista de tuplas para poder fazer a extração. Cada uma composta por (nome, email, enviado) nessa sequência
# zip() = construir uma tupla, passando com parâmetro a lista de nomes, emails e status do enviado e transformado resultado em lista

# Impresso 1 tupla para testar construção
# Criado segunda lista de tuplas, usando dados do 2º dict. Usado '+' para juntar as duas construções e ter uma lista completa de dados
# dados = lista de tuplas, cada item dessa lista é uma TUPLA.

# [item[1] for item in dados if not item[2]] = "item[1]" seleciona o valor que ocupa a posição 1 da tupla (emails).Iterando sobre todos os dados, terá uma lista com todos os emails. "if not item[2]" = posição 2 da tupla deve ser falso, para coletar todos os emails que não foram enviados, esse filtro seleciona somente se o "item[2]" não tiver o valor True

# CONCLUSÃO: com a função zip() foi extraído cada registro do dict, depois com '+' foi juntado todos os dados, e usando listcomp foi criado uma lista com os critérios


### SESSÃO 2
# MECANISMOS DE BUSCA

nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()

print('Marcela' in nomes)
print('Roberto' in nomes)
    # True
    # False

# in = verificar se está na lista


# BUSCA LINEAR (SEQUENCIAL)

# A busca linear/exaustiva percorre os elementos de uma sequência em busca de um valor específico, iniciando por uma das extremidades e examinando todos os elementos até encontrá-lo (ou não). Esse método pode ser computacionalmente custoso

# IMPLEMENTAÇÃO:
# for = estrutura de repetição para percorrer a sequencia
# if = estrutura de decisão para verificar se o valor em uma determinada posição é o que procuramos

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False
    
import random
lista = random.sample(range(1000), 50)
print(sorted(lista))

executar_busca_linear(lista, 10)
    # [63, 70, 99, 114, 137, 164, 174, 224, 236, 243, 263, 300, 301, 309, 310, 333, 336, 350, 351, 371, 375, 397, 400, 418, 463, 521, 525, 540, 561, 563, 573, 582, 593, 612, 649, 669, 690, 717, 727, 744, 806, 865, 881, 901, 922, 936, 940, 947, 962, 994]

# executar_busca_linear = receber uma lista e um valor a ser localizado
# Criado lista de repetição que percorrerá cada elemento da lista pela comparação com o valor buscado. Caso seja localizado, retorna True, caso não, retorna False

# lista = random.sample(range(1000), 50) # criado lista de 50 valores com números inteiros randômicos que variam entre 0 e 1000. Cada execução do código gerará uma lista diferente e o resultado pode alterar
# A função é capaz de determinar se um valor está ou não presente na sequência


# index() = saber a posição na sequência. Estruturas de dados do tipo sequência possuem a função "sequência.index(valor)", que espera como parâmetro o valor a ser procurado na sequência

vogais = 'aeiou'

resultado = vogais.index('e')
print(resultado)
    # 1

# Busca linear com utilização do "index()":
# Iterar sobre a lista e quando for encontrado retornar o índice, caso não encontrar, retornar None
# Em uma lista numérica, só podem ser localizados valores do mesmo tipo. Em uma sequência de caracteres, só podem ser localizadas letras, palavras e uma string vazia. None não pode ser localizado em uma lista, se tentar, ocorrerá um erro

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return [i]
    return None

vogais = 'aeiou'

resultado = procurar_valor(lista=vogais, valor='o')

if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else: print("Valor não encontrado")
    # Valor encontrado na posição [3]

# def procurar_valor(lista, valor) = retornar posição de um valor (se for encontrado)
# vogais = 'aeiou' # criado lista de vogais
# resultado = procurar_valor(lista=vogais, valor='o') # invocado a função passando a lista e o valor a ser procurado
# if resultado != None # testado se o valor existe na variável "resultado". Caso o valor for None, o "else" é acionado
# Valor encontrado na posição [3] = a lista tem tamanho 5, índices de 0 a 4. Valor 'o' foi encontrado na posição 3 da lista (percorrendo os índices 0, 1, 2 e 3)

# Busca linear (sequencial) funciona desta forma: todas as posições são visitadas ate encontrar o elemento buscado, caso a busca for um valor que não está na lista, o resultado é "None"

# Usando a função "index()" e o valor buscado não esteja na lista, retornará um erro. Na função "procurar_valor" se não for encontrado retorna None


# COMPLEXIDADE

# Algoritmos são considerados melhores quando usam menos recursos computacionais em relação a memória e processamento. O método de Cramer para resolver equações lineares pode levar dezenas de milhões de anos para resolver um sistema matricial de 20x20, enquanto o método de Gauss pode levar apenas alguns segundo
# Diante uma lista de 1,5 milhões de nomes, é mais eficiente realizar a busca dividindo a lista ao meio e verificar se o nome buscado está na parte inferior ou superior, que buscar pela lista inteira (um por um)


# BUSCA BINÁRIA

# A diferença entre busca linear e busca binária é que no 2º os valores precisam estar ordenados

# Como realizar:
# 1º Encontra o item no meio da sequência (meio da lista)
# 2º Se o valor procurado for igual ao item do meio, a busca se encerra
# 3º Se não for, verifica se o valor buscado é maior ou menor que o valor central
# 4º Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada); se não for, a busca acontecerá na metade inferior da sequência (a superior é descartada)

# Ao encontrar o valor central de uma sequência, a divide em duas partes, o que justifica o nome de busca binária.

# VALOR BUSCADO = 14
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 
#               m1        m2    m3

# m1 = o algoritmo começa no valor central, mas como o valor buscado não é o central (maior que ele), a busca acontece na metade superior. A metade inferior é descartada
# Diante novo conjunto, localizado valor central (m2), que também não é o valor buscado (maior que ele), a busca acontece na metade superior. A metade inferior é descartada
# m3 = ao localizar o valor central novamente, o valor buscado é encontrado e finalizado o algoritmo

# Lista com 1024 elementos:
# Na 1º iteração do loop, ao encontrar o meio e excluir uma parte, a lista diminui para 512 elementos
# 2º iteração, ao encontrar o meio e excluir uma parte, restam 256 elementos
# 3º = 128, 4º = 64, 5º = 32, 6º = 16, 7º = 8, 8º = 4, 9º = 2, 10º = 1
# Para 1024 elementos, no pior caso, o loop será executado 10 vezes. Enquanto na busca linear, a iteração acontecerá 1024 vezes


# Pseudocódigo para busca binária:

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
    return False

lista = list(range(1, 50))

print(lista)

print('\n',executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    # True
    # False

# Variáveis que contém o primeiro e ultimo índice da lista. Serão atualizadas no loop conforme a condição
    # minimo = 0
    # maximo = len(lista) - 1

# while minimo <= maximo: # não sabemos quantas vezes a repetição será executada. Será executado para todos os casos binários
# meio = (minimo + maximo) // 2 # encontrar o meio da lista
# if valor < lista[meio] # checado se o valor buscado é menor que o valor encontrado no meio da lista. Se for, atualizado o índice "máximo"
# Neste cenário, é excluído a metade superior da lista. Caso o valor não seja menor que o meio da lista, é testado se ele é maior. Se for maior, é atualizado o menor índice e excluindo a metade inferior
# Se o valor procurado não for nem maior nem menor e ainda estiver dentro do loop, então ele é igual e é retornado o valor True. Caso feito todos os testes e não for encontrado o valor, então retorna False

# Testado a função "executar_busca_binaria" usando a função "range()" para criar uma lista numérica de 50 valores ordenados
    # print('\n',executar_busca_binaria(lista=lista, valor=10)) # valor que existe
    # print('\n', executar_busca_binaria(lista=lista, valor=200)) # valor que não existe

# Alterando a função para retornar a posição que o valor ocupa na sequência:

def procurar_valor(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return meio
    return None

vogais = 'aeiou'

resultado = procurar_valor(lista=vogais, valor='o')

if resultado:
    print(f"Valor encontrado na posição {resultado}")
else:
    print(f"Valor não encontrado")
    # Valor encontrado na posição 3

# return meio = guardado valor do "meio" em uma variável e retornado caso valor buscado esteja presente na lista
# Verificado se o valor procurado é igual ao valor da posição do meio da lista, se for menor, o processo se repete considerando que a lista possui metade do tamanho, inicia na posição seguinte do meio
# Se o valor da posição for menor, o processo é repetido, considerando que a lista tem a metade do tamanho e inicia na posição anterior

# No teste:
    # vogais = 'aeiou'
    # resultado = procurar_valor(lista=vogais, valor='o')
# A metade da lista está na posição 2 (i). Será buscado no próximo elemento a partir da metade da lista. Valor 'o' encontrado na posição 3


# DESAFIO
# DEDUP = deduplicação de dados, consiste em eliminar registros duplicados dos dados.

# Implementar uma solução que receba uma lista de CPFs, aplique a transformação "dedup" e retorne apenas a parte numérica dos CPFs. Verificar se os CPFs possuem 11 dígitos e eliminar aqueles que não possuem. Para realizar a deduplicação, você precisa escolher entre um algoritmo de busca linear ou binária. Também é necessário remover os caracteres ponto (.) e traço (-) que frequentemente aparecem nos CPFs antes de verificar se eles possuem 11 dígitos.

# RESOLUÇÃO
# Sera utilizado o algoritmo de busca linear, porque nao é possivel garantir que os CPFs estejam ordenados (exigencia da busca binaria). CPFs possuem numeros, traco e pontos, entao serao tratados como 'strings' para poder usar a funcao 'replace()' e trocar um caractere por outro. Sera usada a funcao len() para verificar se o CPF possui 11 digitos.

# Algoritmo de busca linear:
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Funcao que faz o dedup e os tratamentos do cpf:
def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace('-', '').replace('.', '')
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf)

    return lista_dedup

# Funcao teste:
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)
    # ['11111111111', '22222222222', '33333333333']

# Primeiro foi implementado a funcao de busca linear, onde recebe uma lista e um valor a ser procurado. Nele, toda a lista é percorrida ate encontrar (ou nao) o valor.
# Na segunda solucao, foi implementada a funcao que faz ajustar o CPF, que valida seu tamanho e faz o dedup.

# Foi criada uma estrutura de dados (tipo lista) vazia. Essa lista ira armazenar os valores unicos dos CPFs. Depois foi criado a estrutura de repeticao, que percorre cada CPF da lista original. Foi feita tambem a conversao forcada do CPF para o tipo string, pois ao percorrer a lista, cada elemento pode ser um tipo diferente.

# Foi usado o encadeamento da funcao replace para substituir os caracteres ponto e traco por nada. Apos isso foi chegado se o tamanho do CPF é 11, caso nao seja, nada acontece e o loop passa para a proxima iteracao.
# Entao, foi invocada a funcao de busca, passando como parametro a lista_dedup e o CPF. Essa funcao procura na lista o valor, caso encontre, retorna True, caso nao encontre, retorna False. Queremos os falsos, porque quer dizer que o CPF ainda nao esta na lista correta (por isso foi usado o 'if not').

# Apos isso, foi adicionada à lista_dedup o CPF, ja validado, transformado e com garantia de que nao esta duplicado. Por ultimo, foi feito apenas o teste. Diante a lista ficticia de CPFs, a funcao retorna uma lista com os CPFs validos e sem duplicacao.


### SESSÃO 3
# ALGORITMOS DE ORDENAÇÃO

# Existem duas formas que permitem ordenar uma sequência presente nos objetos da classe list.
# Função built-in sorted() e o método sort().

lista = [10, 4, 1, 15, -3]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('lista = ', lista, '\n')
print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)
print('lista = ', lista)
    # lista =  [-3, 1, 4, 10, 15]

    # lista_ordenada1 =  [-3, 1, 4, 10, 15]
    # lista_ordenada2 =  None
    # lista =  [-3, 1, 4, 10, 15]

# A funcao sorted() retorna uma nova lista ordenada, sem alterar a lista original. O metodo sort() ordena a lista original, sem retornar nada.
# Logo, concluímos que:
# 1) a função built-in sorted() não altera a lista original e faz a ordenação em uma nova lista;
# 2) o método sort() faz a ordenação na lista original com retorno None.

# Os algoritmos de ordenacao consistem em comparar 2 valores, verificar qual é menor e colocar na posicao correta, o que muda é como e quando a comparacao é feita.

lista = [7, 4]
if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)
    # [4, 7]

# O codigo consistem em comparar um valor e seu vizinho, caso o valor da posicao a frente seja menor, deve ser feita a troca das posicoes. Para fazer a troca foi feito usando uma variavel auxiliar criada para guardar temporariamente um dos valores (nesse caso guardando o menor). Entao foi colocado o valor maior na posicao da frente e resgatado o valor menor da variavel auxiliar e colocado na posicao anterior.

# Para fazer a troca usando a atribuicao multipla, ela é feita de maneira posional:
# O primeiro valor apos o sinal de igualdade vai para a primeira variavel, e asism por diante.

lista = [5, -1]
if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]

print(lista)
    # [-1, 5]


# SELECTION SORT (ORDENACAO POR SELECAO)
# Recebe esse nome porque faz a ordenacao escolhendo o menor valor para ocupar determinada posicao. Suponto que em uma fila de pessoas, precisamos colocar por ordem de tamanho, do menor para o maior.

# Pelo algoritmo selection sort, sera procurado em cada uma das pessoas na fila, a menor delas. Quando encontrar a pessoa troca de lugar com a primeira (agora a primeira pessoa da fila esta na posicao correta). Depois, a partir da segunda pessoa, sera procurado a menor pessoa e trocada de lugar com a segunda pessoa da fila. E assim por diante, ate que a fila esteja ordenada.

# A logica do algoritmo é a seguinte:
# 1) Percorrer a lista de traz para frente, procurando o menor valor;
# 2) Trocar o menor valor encontrado com o primeiro valor da lista;
# 3) Repetir o processo, mas agora a partir da segunda posicao da lista;
# Esse processo é repetido ate que a lista esteja ordenada.

def executar_selection_sort(lista):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_selection_sort(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Foi usada uma variavel que guarda o tamanho da lista (n). É necessario 2 estruturas de controle para iterar (para ir atualizando a posicao de insercao quanto para achar o menor valor da lista).
# Foi usada a variavel 'i' para controlar a posicao da insercao e a variavel 'j' para iterar sobre os valores da lista, procurando o menor valor. A busca pelo menor valor é feita com a variavel 'index_menor', que guarda a posicao do menor valor encontrado para a troca dos valores. Quando o valor da posicao i ja for o menor, entao index_menor nao se atualiza pelo j.

# Sera usado outro exemplo, onde sera criado uma lista vazia e dentro de uma estrutura de repeticao, sera usada a funcao 'min()' para a cada iteracao, encontrar o menor valor da sequencia e adicionar na 'lista_ordenada'.
# A cada iteracao, o valor adicionado a nova lista é removido da lista original.

def executar_selection_sort2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_selection_sort2(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]


# BUBBLE SORT (ORDENACAO BOLHA)
# Esse algoritmo faz a ordenacao a partir do inicio da lista, comparando um valor com seu vizinho. Suponto que tenha uma fila de pessoas, e elas precisam ser colocadas por ordem de tamanho, do menor para o maior.

# Usando o bubble sort, a primeira pessoa da fila (pessoa A), pergunta para a segunda pessoa sua altura, se o segundo for menor, entao eles trocam de lugar. Novamente, a pessoa A pergunta para o proximo vizinho qual é sua altura, se for menor, trocam de lugar. E assim por diante, ate que a pessoa A encontre alguem maior, no qual essa nova pessoa vai percorrer a fila ate o final fazendo a mesma pergunta.
# Esse processo é repetido ate que a fila esteja ordenada.

# A logica do algoritmo é a seguinte:
# 1) Percorrer a lista de traz para frente, comparando um valor com seu vizinho;
# 2) Trocar o valor com seu vizinho se o valor for maior que o vizinho;
# 3) Repetir o processo, mas agora a partir da segunda posicao da lista;
# Esse processo é repetido ate que a lista esteja ordenada.

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_bubble_sort(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Foi usada uma variavel que guarda o tamanho da lista (n). É necessario 2 estruturas de controle para iterar (para ir atualizando a posicao de insercao quanto para achar o menor valor da lista).
# Foi usada a variavel 'i' para controlar a posicao da insercao e a variavel 'j' para iterar sobre os valores da lista, procurando o menor valor. A busca pelo menor valor é feita com o auxilio de uma variavel com a qual, quando o menor valor for encontrado, a variavel 'index_menor' recebe o valor da posicao do menor valor encontrado para a troca dos valores. Quando o valor da posicao i ja for o menor, entao index_menor nao se atualiza pelo j.

# Essa versao do selection sort, usa a funcao 'min()' para achar o menor valor da lista e adicionar na lista_ordenada. A cada iteracao, o valor adicionado a nova lista é removido da lista original.


# INSERTION SORT (ORDENAÇÃO POR INSERÇÃO)
# Esse algoritmo faz a ordenacao pela simulacao da insercao de novos valores na lista. Supondo em um jogo de cartas, onde cada jogador comeca com 5 cartas e a cada rodada deve pegar e inserir uma nova carta na mao.

# O jogador deseja deixar as cartas ordenadas, e a cada nova carta precisa inserir na posicao correta. Ele olha a sequencia da esquerda para  adireita procurando a posicao exata para fazer a insercao.

# A logica do algoritmo é a seguinte:
# 1) Percorrer a lista de traz para frente, procurando a posicao correta para inserir o valor;
# 2) Inserir o valor na posicao correta;
# 3) Repetir o processo, mas agora a partir da segunda posicao da lista;
# Esse processo é repetido ate que a lista esteja ordenada.

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_insertion_sort(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Foi usada uma variavel que guarda o tamanho da lista (n). É necessario 2 estruturas de controle para iterar (para ir atualizando a posicao de insercao quanto para achar o menor valor da lista). Na primeira estrutura, foi usado o 'for' para controlar a variavel i, que representa a posicao do valor a ser inserido.

# Sabendo exatamente quantas vezes sera iterado, esse for pode ser usado. O for comeca na posicao 1, porque o algoritmo nao precisa iterar sobre a primeira posicao, pois nao ha nada a esquerda para comparar. Criando a segunda estrutura de repeticao com o while, porque nao se sabe quantas vezes sera necessario iterar para encontrar a posicao correta para inserir o valor.

# O loop acontece enquanto houver elementos para comparar (j >= 0) e enquanto o valor a ser inserido for menor que o valor da posicao anterior (lista[j]) for maior que o valor a ser inserido. Enquanto essas condicoes acontecerem os valores ja existentes vao sendo passados para frente e j vai decrementando. Quando  a posicao for encontrada, o valor é inserido.

# Todas as execucoes de ordenamento anteriores, o tempo de execucao foi instantaneo, pois as listas eram pequenas. Caso fossem muitos valores, o tempo de execucao seria maior. A seguir, serao mostrados outros algoritmos mais rapidos, porem mais complexos.


# MERGE SORT (ORDENAÇÃO POR MESCLAGEM)
# Esse algoritmo faz a ordenacao em duas etapas: divide a lista em sublistas, depois junta (merge) as sublistas ordenadas. Conhecido por usar a estrategia de dividir para conquistar.

# Para resolver um determinado problema, ela chama recursivamente uma ou mais vezes para lidar com subproplemas menores. A recursao é usada para dividir a lista em sublistas, ate que cada sublista tenha apenas um elemento. Apos isso, as sublistas sao mescladas (merge) em uma lista ordenada.

# A logica do algoritmo é a seguinte:
# 1) Dividir a lista em sublistas, ate que cada sublista tenha apenas um elemento;
# 2) Mesclar as sublistas em uma lista ordenada;
# Esse processo é repetido ate que a lista esteja ordenada.

# Suponto que existam 2 fileiras de criancas em ordem de tamanho, ao olhar para  aprimeira crianca de cada fila, é possivel identificar a menor e coloca-la na posicao correta. Fazendo isso com todas as criancas, a fila estara ordenada.

# ORDENANDO A LISTA [10, 9, 5, 8]:
# Comecando pela etapa de divisao, é encontrado o meio da lista e feita uma divisao. Resultando em sublistas [10, 9] e [5, 8] (esquerda e direita). Como essas sublistas possuem mais de um valor, é feita a quebra novamente, resultando em [10] e [9] (esquerda) e [5] e [8] (direita).

# Apos alcancar tamanho minimo da lista, comeca o processo de merge, que faz a juncao de forma ordenada. Comecando pela esquerda, as listas [10] e [9] sao comparadas, gerando a sublista [9, 10]. A sublista [5] e [8] sao comparadas, gerando a sublista [5, 8].

# Apos isso, é feito o novo merge entre essas sublistas de tamanho 2, no topo de cada lista, esta o menor valor de cada uma. Entao, ao olhar para o topo de duas listas, sera visto os valores 9 e 5 (como 5 é menor, ele é o primeiro escolhido para ocupar a posicao 0). Olhando novamente para o topo de cada lista, temos os valores 9 e 8. Como 8 é menor, ele é escolhido para compor a nova lista.
# Olhando novamente, temos somente uma lista, com valor 9 no topo, portanto ele é escolhido, e por fim o valor 10 é selecionado.

# Pontos importantes desse metodo:
# É necessario usar 2 funcoes, uma que divide e uma que junta.
# As sublistas sao fatiamentos da lista original.
# O algoritmo de merce recebe sempre a lista inteira, mas trata de posicoes especificas. Na etapa da divisao, sao feitas sucessivas subdivisoes aplicando a mesma regra, ate que cada sublista tenha apenas um elemento. Na etapa de merge, as sublistas sao mescladas em uma lista ordenada.

def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)
    
def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_merge_sort(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Foi criada a funcao de ordenacao por merge sort, que contem 2 funcoes (uma para dividir as listas e outra para fazer o merge). A funcao que faz a divisao recebe como parametro a lista a ser ordenada.

# Se o tamanho da lista é menor ou igual a 1, significa que a sublista so tem 1 valor e esta ordenada (seu valor é retornado). Caso nao esteja, é encontrado o meio da lista e feita a divisao entre sublistas da direita e esquerda. Esse processo ;e feito ate que se tenha sublistas com apenas 1 elemento.
# A funcao de juncao, recebe as 2 listas e percorre cada uma delas pelo while, considerando cada valor, o que for menor é adicionado a sublista ordenada.


# QUICK SORT (ORDENAÇÃO RÁPIDA)
# Considerando um valor em uma lista ordenada, à direita desse numero, existem somente numeros maior que a ele, e a esquerda somente menores. Esse valor é chamado de pivo, e é a estrategia principal do algoritmo de ordenacao rapida.

# Esse algoritmo usa a estrategia de dividir para conquistar, e divide a lista em sublistas (esquerda e direita), onde cada sublista contem valores menores ou maiores que o pivo.
# Supondo que tenha uma fila de pessoas e elas precisam ser ordenadas por tamanho. É escolhido uma pessoa para usar seu tamanho como comparacao (esse é o pivo), com base nessa pessoa, todos que sao menores a ele devem ir para a esquerda e todos maiores a ele, para a direita. O voluntario esta na posicao ordenada.

# É repetido o procedimento para os menores e maiores. A cada passo, estamos dobrando o numero de pessoas na posicao final. A logica é a seguinte:
# 1) Escolher um pivo;
# 2) Colocar todos os valores menores que o pivo a esquerda e os maiores a direita;
# 3) Repetir o processo para as sublistas menores e maiores.

# Na segunda iteracao, com agora duas listas (direira e esquerda do pivo). Novamente sao escolhidos 2 novos pivos e é feito o mesmo processo de ordenacao. Esse processo é repetido ate que todas as sublistas tenham apenas 1 elemento.
# Na terceira iteracao, temos 4 sublistas, cada uma com 1 elemento. Apos isso, é feito o merge entre elas, e a lista esta ordenada.

def executar_quick_sort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quick_sort(lista, inicio, pivo - 1)
        executar_quick_sort(lista, pivo + 1, fim)
    return lista

def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_quick_sort(lista, 0, len(lista) - 1)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Foram usadas 2 funcoes. A funcao executar_quicksort cria as sublistas, cada uma deve ser criada com base em um pivo. Portanto a caso a posicao de inicio da lista seja menor que o fim (temos mais de 1 elemento), portanto é chamada a funcao executar_particao. Ela faz a comparacao e quando necessario troca os valores de posicao, alem de retornar o indice correto para cada pivo.

# Foi feita a definicao do pivo como o ultimo valor da lista (e mesmo da sublista). Apos isso, foi criada uma variagem de controle par aa separacao da lista da esquerda, ou seja, a lista que guardara os valores menores que o pivo. Foi usado tambem uma estrutura re repeticao para comprar o pivo com todos os valores da lista da direita.
# A cada vez que um valor menor que o pivo é encontrado, é feita a troca dos valores pelas posicoes e a delimitacao da lista dos menores (esquerda) é atualizada.

# O pivo é colocado na sua posicao (limite da esquerda), fazendo a troca com o valor que esta ali. Por fim, a funcao retorna o indice do pivo.

# Outra opcao usando o listcomp é criando uma lista de pivos (agora o pivo é o primeiro valor da lista), uma lista com os valores menores e uma com valores maiores.

def executar_quick_sort2(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    iguais = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor < pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return executar_quick_sort2(menores) + iguais + executar_quick_sort2(maiores)

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_quick_sort2(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]


# DESAFIO
# Diante da solução feita no Desafio 2 onde foi feito o dedup em uma lista de CPFs, retornar somente parte numérica do CPF e verificar se eles possuem 11 dígitos. Agora a lista de CPFs deve ser organizada de forma crescente para facilitar o cadastro. A lista de CPFs pode crescer exponencialmente, escolher os algoritmos mais adequados é importante nesse caso.

# DEVERÁ SER FEITO:
# Realizar as transformações de limpeza e validação nos CPFs (remover ponto e traço, verificar se tem 11 dígitos e não deixar valores duplicados).
# E também realizar a entrega em ordem crescente.


# RESOLUCAO
# Sera usado a busca binaria (pois performa melhor que a linear), apesar que os dados precisam estar ordenados. Os dados serao ordenados implementando algoritmos de ordenacao rapida e merge sort.

# Sabendo que a quantidade de CPFs pode aumentar exponencialmente, a melhor opcao é usar o MERGE-SORT, visto que no pior caso é o que tem menor complexidade de tempo.

# implementacao do MERGE SORT
def executar_merge_sort(lista, inicio=0, fim=None):
    if not fim:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        executar_merge_sort(lista, inicio, meio)
        executar_merge_sort(lista, meio, fim)
        executar_merge(lista, inicio, meio, fim)
    return lista

def executar_merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0
    for p in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[p] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[p] = direita[topo_direita]
            topo_direita += 1

# implementacao da BUSCA BINARIA
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
    return False

# implementar funcao que faz verificacao do cpf, dedup e devolve o resultado
def criar_lista_dedup_ordenada(lista):
    lista = [str(cpf).replace('.','').replace('-','') for cpf in lista]
    lista = [cpf for cpf in lista if len(cpf) == 11]
    lista = executar_merge_sort(lista)
    
    lista_dedup = []
    for cpf in lista:
        if not executar_busca_binaria(lista_dedup, cpf):
            lista_dedup.append(cpf)
    return lista_dedup

# funcao teste
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
lista_ordenada1 = testar_funcao(lista_cpfs)
    # ['11111111111', '22222222222', '33333333333', '44444444444']

# Foram usados algoritmos de ordenacao MERGE SORT e BUSCA BINARIA. No de ordenacao, foi feito um tratamento na variavem fim, para que nao precise ser passada explicitamente na primeira chamada.

# Na funcao criar_lista_dedup_ordenada, foi usado uma listcomp para remover o ponto e o traço do cpf. Apos isso, foi criado novamente um listcomp para guardar somente os CPFs que possuem 11 digitos. Com os cpfs validos, é usada a funcao de ordenacao, que retorna a lista ordenada. Por fim, foi feita a busca binaria para verificar se o valor ja esta na lista, caso nao esteja ele é adicionado.