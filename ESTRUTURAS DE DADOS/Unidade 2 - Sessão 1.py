# ESTRUTURAS DE DADOS

# Existem objetos que são usados para armazenar mais de um valor, também chamados de estruturas de dados.
# Cada objeto é capaz de armazenar um tipo de estrutura de dados, particularidade essa que habilita funções diferentes para cada tipo.
# Portanto, a escolha da estrutura depende do problema a ser resolvido.

# Objetos do tipo sequência: texto, listas e tuplas.
# Objetos do tipo set (conjunto).
# Objetos do tipo mapping (dicionário).
# Objetos do tipo array NumPy.

# OBJETOS DO TIPO SEQUÊNCIA:

# Os objetos do tipo sequência são estruturas de dados capazes de armazenar mais de um valor.
# Essas estruturas de dados representam sequências finitas indexadas por números não negativos.
# O primeiro elemento de uma sequência ocupa o índice 0; o segundo, 1; o último elemento, a posição n - 1, em que n é capacidade de armazenamento da sequência.

# SEQUÊNCIA DE CARACTERES:

# Um texto é um objeto da classe str (strings), que é um tipo de sequência.
# Os objetos da classe str possuem todas as operações, mas são objetos imutáveis, razão pela qual não é possível atribuir um novo valor a uma posição específica.

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeira letras são: {texto[0:6]}")

# A operação len() permite saber o tamanho da sequência.
# O operador 'in', por sua vez, permite saber se um determinado valor está ou não na sequência.
# O operador count permite contar a quantidade de ocorrências de um valor. E a notação com colchetes permite fatiar a sequência, exibindo somente partes dela.
# Por fim, pedimos para exibir da posição 0 até a 5, pois o valor 6 não é incluído.

# A classe str possui vários outros métodos:
# Podemos usar a função lower() para tornar um objeto str com letras minúsculas.
# A função upper(), que transforma para maiúsculo.
# A função replace() pode ser usada para substituir um caractere por outro.

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(texto.upper())
print(texto.replace("i", 'XX'))

# APRENDENDO PYTHON NA DISCIPLINA DE LINGUAGEM DE PROGRAMAÇÃO.
# Aprendendo Python na dXXscXXplXXna de lXXnguagem de programação.


# A FUNÇÃO split():

# Usada para "cortar" um texto e transformá-lo em uma lista.
# Essa função pode ser usada sem nenhum parâmetro: texto.split().
# A string será cortada a cada espaço em branco que for encontrado.
# Caso seja passado um parâmetro: texto.split(","), então o corte será feito no parâmetro especificado.

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n") # A função len() (length) para saber a quantidade de parâmetros que foram passados.

# texto = Aprendendo Python na disciplina de linguagem de programação.
# Tamanho do texto = 60

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

# palavras = ['Aprendendo', 'Python', 'na', 'disciplina', 'de', 'linguagem', 'de', 'programação.']
# Tamanho de palavras = 8

# Usamos a função split() para cortar o texto e guardamos o resultado em uma variável chamada "palavras".
# O texto tem tamanho 60, possui uma sequência de 60 caracteres. 
# Já o tamanho da variável "palavras" é 8, ao cortar o texto, criamos uma lista com as palavras.
# A função split(), usada dessa forma, corta um texto em cada espaço em branco.


# Exercício de análise de texto:

# Dado um texto sobre strings.
# Queremos saber quantas vezes o autor menciona a palavra string ou strings.

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

# Tamanho do texto = 348
# Tamanho da lista de palavras = 58
# Quantidade de vezes que string ou strings aparecem = 4

# Criamos uma variável chamada "texto" que recebe uma citação.
# Aplicamos a função lower() a essa string para que todo o texto fique com letras minúsculas e guardamos o resultado dessa transformação, dentro da própria variável, sobrescrevendo, assim, o texto original.

# Fazemos uma série encadeada de transformações usando a função replace(), que age substituindo o primeiro parâmetro pelo segundo.
# No primeiro replace(",", ""), substituímos todas as vírgulas por nada. Então, na verdade, estamos apagando as vírgulas do texto sem colocar algo no lugar.
# No último replace("\n", " "), substituímos as quebras de linhas por um espaço em branco.

# Criamos uma lista ao aplicar a função split() ao texto.
# Sempre que houver um espaço em branco, a string será cortada, criando um novo elemento na lista.
# Criamos uma lista com 58 elementos.

# Usamos a função count() para contar tanto a palavra "string" no singular quanto o seu plural "strings".
# A função retorna um número inteiro, somamos os resultados e os exibimos.


# LISTAS

# Lista é uma estrutura de dados do tipo sequencial que possui como principal característica ser mutável.
# Novos valores podem ser adicionados ou removidos da sequência.

# Usando um par de colchetes para denotar uma lista vazia: lista1 = []
# Usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a', 'b', 'c']
# Usando uma "list comprehension": [x for x in iterable]
# Usando o construtor de tipo: list()

# Os objetos do tipo sequência são indexados.
# Cada elemento ocupa uma posição que começa em 0.
# Um objeto com 5 elementos terá índices que variam entre 0 e 4.
# O primeiro elemento ocupa a posição 0; o segundo, a posição 1; o terceiro, a posição 2; o quarto, a posição 3; e o quinto, a posição 4.

vogais = ['a', 'e', 'i', 'o', 'u'] # Também poderia ter sido criada usando aspas duplas.

for vogal in vogais:
    print(f'posição = {vogais.index(vogal)}, valor = {vogal}')
# Posição = 0, valor = a
# Posição = 1, valor = e
# Posição = 2, valor = i
# Posição = 3, valor = o
# Posição = 4, valor = u

# Criamos uma lista chamada de "vogais".
# Por meio da estrutura de repetição, imprimimos cada elemento da lista juntamente com seu índice.
# A sequência possui a função index, que retorna a posição de um valor na sequência.


vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")
# Tipo do objeto vogais = <class 'list'>
# Posição = 0, valor = a
# Posição = 1, valor = e
# Posição = 2, valor = i
# Posição = 3, valor = o
# Posição = 4, valor = u


# Repetimos o exemplo com algumas alterações:
# Criar uma lista vazia.
# Mesmo estando vazia, ao imprimir o tipo do objeto, o resultado é "class list", pois o colchete é a sintaxe para a construção de listas.

# A função append(), adiciona um novo valor ao final da lista.
# Na sintaxe usamos vogais.append(valor), significa que a função append() é do objeto lista.

# Substituímos o contador manual ("p") pela função enumerate().
# Usado para percorrer um objeto iterável retornando a posição e o valor.

# Na estrutura de repetição precisamos usar as variáveis p e x.
# A primeira guarda a posição e a segunda guarda o valor.
# Usamos o nome x propositalmente para perceber que o nome da variável é de livre escolha.

