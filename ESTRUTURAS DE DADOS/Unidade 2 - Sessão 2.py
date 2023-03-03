# COMANDOS DOS MECANISMOS DE BUSCAS

# ALGORITMOS DE BUSCAS

nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()

print('Marcela' in nomes)
print('Roberto' in nomes)
# True
# False

# Usamos o operador (in) para verificar se dois nomes constavam na lista.
# No primeiro, obtivemos True; e no segundo, False.

# BUSCA LINEAR (OU BUSCA SEQUENCIAL)

# Uma busca linear (ou exaustiva) simplesmente percorre os elementos da sequência procurando aquele de destino.

# A busca começa por uma das extremidades da sequência e vai percorrendo até encontrar (ou não) o valor desejado.
# Uma pesquisa linear examina todos os elementos da sequência até encontrar o de destino, o que pode ser muito custoso computacionalmente.

# Para implementar a busca linear:
# Precisamos de uma estrutura de repetição (for) para percorrer a sequência.
# E uma estrutura de decisão (if) para verificar se o valor em uma determinada posição é o que procuramos.

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

import random
lista = random.sample(range(1000), 50)
print(sorted(lista))

executar_busca_linear(lista, 10)
# [52, 73, 95, 98, 99, 103, 123, 152, 158, 173, 259, 269, 294, 313, 318, 344, 346, 348, 363, 387, 407, 410, 414, 433, 470, 497, 520, 530, 536, 558, 573, 588, 620, 645, 677, 712, 713, 716, 720, 727, 728, 771, 790, 801, 865, 898, 941, 967, 970, 979]


# Criamos a função "executar_busca_linear" que recebe uma lista e um valor a ser localizado.
# Criamos a estrutura de repetição que percorrerá cada elemento da lista pela comparação com o valor buscado.
# Caso este seja localizado, então a função retorna o valor booleano True; caso não seja encontrado, então retorna False.

# Para testarmos a função criamos o código, por meio da biblioteca (random).
# Criamos uma lista de 50 valores com números inteiros randômicos que variam entre 0 e 1000;
# Invocamos a função, passando a lista e um valor a ser localizado.
# Cada execução desse código gerará uma lista diferente, e o resultado poderá alterar.
# Nossa função é capaz de determinar se um valor está ou não presente em uma sequência.

# Se quiséssemos também saber sua posição na sequência:
# As estruturas de dados do tipo sequência possuem a função index(): sequencia.index(valor).
# A função index() espera como parâmetro o valor a ser procurado na sequência.

vogais = 'aeiou'

resultado = vogais.index('e')
print(resultado)
# 1

# Para implementar nossa própria versão de busca por index com utilização da busca linear:
# Podemos iterar sobre a lista e quando o elemento for encontrado, retornar seu índice.
# Caso não seja encontrado, então a função deve retornar None.

# Vale ressaltar a importância dos tipos de valores que serão usados para realizar a busca.
# Dada uma lista numérica, somente podem ser localizados valores do mesmo tipo.
# O mesmo para uma sequência de caracteres, que só pode localizar letras, palavras ou ainda uma string vazia.
# O tipo None não pode ser localizado em nenhuma lista – se tentar passar como parâmetro, poderá receber um erro.

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None

vogais = 'aeiou'

resultado = procurar_valor(lista=vogais, valor='o')

if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")
# Valor encontrado na posição 3
  
# Criamos a função "procurar_valor" a fim de retornar a posição de um valor, caso ele seja encontrado.
# Criamos uma lista com as vogais e invocamos a função "procurar_valor", passando a lista e um valor a ser procurado.
# Testamos se existe valor na variável "resultado", caso o valor guardado em "resultado" for None, então o else é acionado.

# Buscando o valor "0" na lista de vogais.
# A lista tem tamanho 5 (número de vogais), sendo representada com os índices 0 a 4.

# Observe que o valor "o" foi encontrado na posição 3 da lista.
# Foi necessário percorrer os índices 0, 1, 2 e 3 até chegar à vogal procurada.
# Assim funciona a busca linear (sequencial): todas as posições são visitadas até que se encontre o elemento buscado.
# Caso a busca fosse por um valor que não está na lista, o valor retornado seria None.

# Acabamos de implementar uma versão da função index.
# Será que é melhor que a função index() das sequências em Python?
# Se tentarmos executar a função index(), passando como parâmetro um valor que não está na lista, teremos um erro como resultado: "ValueError".
# Nesta versão caso o valor não esteja na lista, não será retornado um erro, mas o valor None.

# COMPLEXIDADE

# A função procurar_valor tem um comportamento diferente da função index() para os valores não encontrados.
# Essa não é uma característica que pode ser levada em consideração para determinar que um algoritmo é melhor que o outro.

# Um algoritmo é considerado melhor que o outro quando, para a mesma entrada, utiliza menos recursos computacionais em termos de memória e processamento.
# Um exemplo é a comparação entre os métodos de Cramer e Gauss, usados para resolver equações lineares.
# O método de Cramer pode levar dezenas de milhões de anos para resolver um sistema matricial de 20 linhas por 20 colunas.
# O método de Gauss pode levar alguns segundos.

# Veja a diferença: para a mesma entrada há um algoritmo que é inviável!
# Esse estudo da viabilidade de um algoritmo, em termos de espaço e tempo de processamento, é chamado de análise da complexidade do algoritmo.

# Pense na lista de alunos, em ordem alfabética, de toda a rede Kroton/Cogna.
# Estamos falando de cerca de 1,5 milhões de alunos.
# Dada a necessidade de encontrar um aluno, é mais eficiente procurá-lo pela lista inteira, um por um, ou dividir essa lista ao meio e verificar se o nome buscado está na parte superior ou inferior?

# A análise da complexidade do algoritmo fornece mecanismos para medir o desempenho de um algoritmo em termos de "tamanho do problema versus tempo de execução".
# A análise da complexidade é feita em duas dimensões: espaço e tempo.
# Embora ambas as dimensões influenciem na eficiência de um algoritmo, o tempo que ele leva para executar é tido como a característica mais relevante.

# Essa análise tem de ser feita sem considerar o hardware, pois sabemos que uma solução executada em um processador mais potente certamente levará menos tempo de execução do que se ocorrer em um menos potente.
# Não é esse tipo de medida que a análise da complexidade está interessada em estudar.
# O que interessa saber é qual função matemática expressa o comportamento do tempo, principalmente, para grandes entradas de dados.
# No caso da função "executar_busca_linear", conforme o tamanho da lista aumenta, o tempo necessário para achar um valor pode aumentar, principalmente se este estiver nas posições finais da lista.

# Essa reflexão sobre a posição do valor na lista leva a outros conceitos da análise da complexidade:
# A medida do tempo com relação ao melhor caso, ao pior caso e ao caso médio.
# Usando a busca linear, se o valor procurado estiver nas primeiras posições, temos o melhor cenário de tempo, independentemente do tamanho da lista.
# Assim que o valor for localizado, a execução da função já se encerra.
# Se o valor estiver no meio da lista, temos um cenário mediano de complexidade, pois o tamanho da lista começa a ter influência no tempo da busca.
# Se o valor estiver no final da lista, teremos o pior caso, já que o tamanho da lista influenciará totalmente o tempo de execução.

# A análise da complexidade interessa em medir o desempenho de um algoritmo para grandes entradas, ou seja, para o pior caso.
# A análise da complexidade de um algoritmo tem como um dos grandes objetivos encontrar o comportamento do algoritmo (a função matemática) em relação ao tempo de execução para o pior caso, ao que chamamos de complexidade assintótica.
# A complexidade assintótica é definida pelo crescimento da complexidade para entradas suficientemente grandes.
# O comportamento assintótico de um algoritmo é o mais procurado, já que, para um volume grande de dados, a complexidade torna-se mais importante.
# O algoritmo assintoticamente mais eficiente é melhor para todas as entradas, exceto talvez para entradas relativamente pequenas.

# A complexidade é expressa por uma função matemática f(n), em que n é o tamanho da entrada.
# Para determinar a complexidade:
# A função é dividida em um termo dominante e termos de ordem inferior, pois estes últimos e as contantes são excluídos.
# Vamos supor que a função:
# f(n) = an2 + bn + c (função do segundo grau) é a função de tempo de um determinado algoritmo.
# Para expressar sua complexidade, identifica-se qual é o termo dominante (nesse caso, o parâmetro com maior crescimento é n2).
# Ignoram-se os termos de ordem inferior (nesse caso n) e ignoram-se as constantes (a, b, c).
# Ficamos então, com a função f(n) = n2.
# A função de complexidade para esse algoritmo é denotada pela notação assintótica O(n2), chamada de Big-Oh (Grande-O).

# Toda essa simplificação é embasada em conceitos matemáticos (limites).
# A análise assintótica é um método usado para descrever o comportamento de limites, razão pela qual é adotada pela análise da complexidade.


# BUSCA BINÁRIA

# Outro algoritmo usado para buscar um valor em uma sequência é o de busca binária.
# A primeira grande diferença entre o algoritmo de busca linear e o algoritmo de busca binária é que:
# Com a busca binária, os valores precisam estar ordenados.

# 1º Encontra o item no meio da sequência (meio da lista).
# 2º Se o valor procurado for igual ao item do meio, a busca se encerra.
# 3º Se não for, verifica-se se o valor buscado é maior ou menor que o valor central.
# 4º Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada); se não for, a busca acontecerá na metade inferior da sequência (a superior é descartada).

# O algoritmo, ao encontrar o valor central de uma sequência, a divide em duas partes, o que justifica o nome de busca binária.

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
#             m1        m2    m3

# O algoritmo começa encontrando o valor central, ao qual damos o nome de m1.
# Como o valor buscado não é o central, sendo maior que ele, então a busca passa a acontecer na metade superior.
# Dado o novo conjunto, novamente é localizado o valor central, o qual chamamos de m2, que também é diferente do valor buscado, sendo menor que este.
# Mais uma vez a metade superior é considerada e, ao localizar o valor central, agora sim trata-se do valor procurado, razão pela qual o algoritmo encerra.
# Usamos retângulos para representar os conjuntos de dados após serem feitos os testes com os valores centrais. Como pode ser observado, cada vez mais o conjunto a ser procurado diminui.

# Suponha que tenhamos uma lista com 1024 elementos.
# Na primeira iteração do loop, ao encontrar o meio e excluir uma parte, a lista a ser buscada já é diminuída para 512.
# Na segunda iteração, novamente ao encontrar o meio e excluir uma parte, restam 256 elementos.
# Na terceira iteração, restam 128.
# Na quarta, restam 64.
# Na quinta, restam 32.
# Na sexta, restam 16.
# Na sétima 8.
# Na oitava 4.
# Na nona 2.
# Na décima iteração resta apenas 1 elemento.
# Ou seja, para 1024 elementos, no pior caso, o loop será executado apenas 10 vezes, diferentemente da busca linear, na qual a iteração aconteceria 1024 vezes.

# A busca binária possui complexidade O(log2 N).
# Isso significa que para valores grandes de N (listas grandes), o desempenho desse algoritmo é melhor se comparado à busca sequencial, que tem complexidade O(N).

# Podemos encontrar o seguinte pseudocódigo para a busca binária:

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo: #Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2 # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            maximo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
    return False # Se chegar até aqui, significa que o valor não foi encontrado

lista = list(range(1, 50))

print(lista)

print('\n',executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

# True

# False

# Implementamos o algoritmo da busca binária.
# Inicializamos as variáveis que contêm o primeiro e o último indíce da lista.
# No começo da execução, esses valores são o índice 0 para o mínimo e o último índice, que é o tamanho da lista menos 1.
# Essas variáveis serão atualizadas dentro do loop, conforme condição.

# Usamos o while como estrutura de repetição, pois não sabemos quantas vezes a repetição deverá ser executada.
# Esse while fará com que a execução seja feita para todos os casos binários.
# Usamos uma equação matemática (a média estatística) para encontrar o meio da lista.
# Checamos se o valor que estamos buscando é menor que o valor encontrado no meio da lista.
# Caso seja, atualizamos o índice máximo.

# Nesse cenário, vamos excluir a metade superior da lista original.
# Caso o valor não seja menor que o meio da lista, testamos se ele é maior.
# Se for, então atualizamos o menor índice, excluindo assim a metade inferior.
# Se o valor procurando não for nem menor nem maior e ainda estivermos dentro do loop, então ele é igual, e o valor True é retornado.
# Porém, se já fizemos todos os testes e não encontramos o valor, então é retornado False.

# Testamos a função executar_busca_binaria.
# Usamos a função range() para criar uma lista numérica de 50 valores ordenados.
# Testamos a função, procurando um valor que sabemos que existe e outro que não existe.


# Como podemos alterar nossa função para que, em vez de retornar True ou False, retorne a posição que o valor ocupa da sequência?
# A lógica é a mesma. No entanto, agora vamos retornar a variável "meio", já que esta, se o valor for encontrado, será a posição.

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

# alteramos a função executar_busca_binaria para procurar_valor.
# Esta função fará a busca com o uso do algoritmo binário.
# Alteramos o retorno da função.
# Restamos o funcionamento do algoritmo.

# É verificado se o valor procurado é igual ao valor da posição do meio da lista.
# Se o valor procurado é menor, o processo se repete considerando que a lista possui a metade do tamanho, razão pela qual inicia na posição seguinte do meio.
# Se o valor da posição for menor, o processo é repetido, considerando que a lista tem a metade do tamanho e inicia da posição anterior.

# No caso do teste apresentado, em que se busca a vogal "o":
# A metade da lista está na posição 2, correspondendo ao valor "i", caso no qual será buscado no próximo elemento a partir da metade da lista.
# Assim, o valor "o" é encontrado na posição 3.