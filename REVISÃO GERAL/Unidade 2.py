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