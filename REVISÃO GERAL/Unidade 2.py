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
# O construtor interpreta como iterável e cria um conjunto em que cada caractere é um elemento (eliminando valores duplicados)


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

# Criado função que gera o relatório das peças aptas a serem vendidas. Criados 2 objetos set> "componentes_verificados" e "componentes_com_defeito"
# len() = saber quantos itens há em cada conjunto
# difference() = obter os itens que estão em componentes_verificados, mas não em componentes_com_defeito
# Também poderia ser feito com o sinal de subtração: componentes_ok = componentes_verificados - componentes_com_defeito


# OBJETOS DO TIPO MAPPING

# Objetos do tipo MAPPING possuem um mapeamento entre uma chave e um valor. O dicionário em um exemplo de objeto que possui essa propriedade, sendo considerado uma estrutura de dados desse tipo. dicionário é um objeto mutável, permitindo a atribuição de um novo valor a uma chave já existente

# Formas de construir dicionários:
# dicionario1 = {} # usando um par de chaves para denotar um DICT vazio
# dicionario2 = {'one': 1, 'two': 2, 'three': 3} # usando um par de elementos (chave : valor) separados por vírgulas
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
# 1: dicionário vazio, criado chaves e atribuindo valores
# 2: dicionário com chaves e valores
# 3: dict() = criar o dicionário passando como parâmetro uma lista de tuplas: dict([(tupla 1), (tupla 2)]), cada tupla é uma combinação de chave e valor
# 4: dict(zip([])) = construtor dict e função zip para combinar valores de diferentes sequências e retornar um iterável de duplas. 1º elemento é referente ao primeiro elemento da sequência 1 e assim por diante

# Testado se as construções produzem o mesmo objeto

# nome_dicionario[chave] = acessar um valor do dicionário
# nome_dicionario[chave] = novo_valor # atribuir novo valor

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


















