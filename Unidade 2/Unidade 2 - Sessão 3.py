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

# Temos dois recursos que ordenam uma lista, mas com diferentes comportamentos.
# A função built-in sorted() cria uma nova lista para ordenar e a retorna, razão pela qual, há uma lista ordenada, guardada dentro da variável lista_ordenada1.

# O método sort(), da classe list, não cria uma nova lista.
# Uma vez que faz a ordenação "inplace" (ou seja, dentro da própria lista passada como parâmetro).
# Isso justifica o resultado obtido, que mostra que, dentro da variável lista_ordenada2, está o valor None e, também, o resultado, em que pedimos para imprimir a lista que agora está ordenada!

# Em Python, por padrão, quando uma função faz a alteração inplace, ela deve retornar o valor None.
# Logo, concluímos que:
# 1) a função built-in sorted() não altera a lista original e faz a ordenação em uma nova lista;
# 2) o método sort() faz a ordenação na lista original com retorno None.

# Temos essas duas opções para ordenar uma lista em Python.
# A essência dos algoritmos de ordenação consiste em comparar dois valores, verificar qual é menor e colocar na posição correta.
# O que vai mudar, neste caso, é como e quando a comparação é feita. 

lista = [7, 4]
if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)
    # [4, 7]

# O código mostra como fazer a ordenação em uma lista com dois valores. A ordenação consiste em comparar um valor e seu vizinho.
# Caso o valor da posição mais à frente seja menor, então deve ser feita a troca de posições.
# Para fazer a troca, usamos uma forma mais clássica, na qual uma variável auxiliar é criada para guardar, temporariamente, um dos valores (no nosso caso estamos guardando o menor).
# Colocamos o valor maior na posição da frente e, resgatamos o valor da variável auxiliar colocando-a na posição correta.

# A sintaxe adotada para fazer a troca no código funciona para qualquer linguagem de programação.
# Podemos fazer a troca usando a atribuição múltipla.
# Nesse caso, a atribuição é feita de maneira posicional:
# O primeiro valor após o sinal de igualdade vai para a primeira variável, e assim por diante.



lista = [5, -1]

if lista[0] > lista[1]:
    lista[0], lista[1] = lista [1], lista[0]

print(lista)
    # [-1, 5]

# Ordenar significa comparar e escolher o menor. Fizemos isso para uma lista com dois valores.

# Se tivéssemos três deles?
# Vamos dividir os algoritmos nestes dois grupos, de acordo com a complexidade:

# Complexidade O(N2): neste grupo estão os algoritmos selection sort, bubble sort e insertion sort. Esses algoritmos são lentos para ordenação de grandes listas, porém são mais intuitivos de entender e possuem uma codificação mais simples.

# Complexidade O(N log N): deste grupo, vamos estudar os algoritmos merge sort e quick sort. Tais algoritmos possuem performance superior, porém são um pouco mais complexos de serem implementados.


# SELECTION SORT (ORDENAÇÃO POR SELEÇÃO)

# O algoritmo selection sort recebe esse nome, porque faz a ordenação sempre escolhendo o menor valor para ocupar uma determinada posição.
# Suponha que exista uma fila de pessoas, mas que, por algum motivo, elas precisem ser colocadas por ordem de tamanho, do menor para o maior. Essa ordenação será feita por um supervisor.

# Segundo o algoritmo selection sort, esse supervisor olhará para cada uma das pessoas na fila e procurará a menor delas.
# Quando encontrá-la, essa pessoa trocará de posição com a primeira.
# Agora, a primeira pessoa da fila está na posição correta, pois é a menor.
# Em seguida, o supervisor precisa olhar para as demais e escolher a segunda menor pessoa; quando encontrá-la, a pessoa troca de lugar com a segunda.
# Agora as duas primeiras pessoas da fila estão ordenadas.
# Esse mecanismo é feito até que todos estejam em suas devidas posições.

# Portanto, a lógica do algoritmo é a seguinte:
# Iteração 1: percorre toda a lista, procurando o menor valor para ocupar a posição 0.
# Iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1.
# Iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2.
# Esse processo é repetido N-1 vezes, sendo N o tamanho da lista.

def executar_selection_sort(lista):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_selection_sort(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]

# Temos uma variável que guarda o tamanho da lista (n). Precisamos de duas estruturas de controle para iterar, tanto para ir atualizando a posição de inserção quanto para achar o menor valor da lista.
# Usamos a variável i para controlar a posição de inserção e a variável j para iterar sobre os valores da lista, procurando o menor valor.
# A busca pelo menor valor é feita com o auxílio de uma variável com a qual, quando o menor valor for encontrado, a variável index_menor guardará a posição para a troca dos valores.
# Quando o valor na posição i já for o menor, então index_menor não se atualiza pelo j.
# Usamos a atribuição múltipla para fazer a troca dos valores, quando necessário.


# Versão do selection sort, na qual criamos uma lista vazia, dentro de uma estrutura de repetição, usamos a função built-in min() para, a cada iteração, encontrar o menor valor da sequência e adicioná-lo na lista_ordenada.
# A cada iteração, o valor adicionado à nova lista é removido da lista original.

def executar_selection_sort_2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = executar_selection_sort_2(lista)
print(lista_ordenada)
    # [-1, 3, 5, 8, 9, 10, 11]


# BUBBLE SORT (ORDENAÇÃO POR "BOLHA")

# O algoritmo bubble sort (algoritmo da bolha) recebe esse nome porque faz a ordenação sempre a partir do início da lista, comparando um valor com seu vizinho.

# Suponha que exista uma fila de pessoas, mas que, elas precisem ser colocadas por ordem de tamanho, do menor para o maior.
# Segundo o algoritmo bubble sort, a primeira pessoa da fila (pessoa A), perguntará para o segundo a altura – se o segundo for menor, então eles trocam de lugar.
# Novamente, a pessoa A perguntará para seu próximo vizinho qual é a altura deste – se esta for menor, eles trocam.
# Esse processo é repetido até que a pessoa A encontre alguém que é maior, contexto no qual essa nova pessoa vai percorrer a fila até o final fazendo a mesma pergunta.
# Esse processo é repetido até que todas as pessoas estejam na posição correta.

# A lógica do algoritmo é a seguinte:
# Iteração 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca; se não for, seleciona o próximo e compara, repetindo o processo.
# Iteração 2: seleciona o valor na posição 0 e compara ele com seu vizinho, se for menor troca, senão seleciona o próximo e compara, repetindo o processo.
# Iteração N - 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca; se não for, seleciona o próximo e compara, repetindo o processo.

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada2 = executar_bubble_sort(lista)
print(lista_ordenada2)
    # [-1, 3, 5, 8, 9, 10, 11]

# Temos uma variável que guarda o tamanho da lista (n).
# Precisamos de duas estruturas de controle para iterar, tanto para ir atualizando a posição de inserção quanto para achar o menor valor da lista.
# Usamos a variável i para controlar a posição de inserção e a variável j para iterar sobre os valores da lista, procurando o menor valor.
# A busca pelo menor valor é feita com o auxílio de uma variável com a qual, quando o menor valor for encontrado, a variável index_menor guardará a posição para a troca dos valores.
# Quando o valor na posição i já for o menor, então index_menor não se atualiza pelo j.
# Usamos a atribuição múltipla para fazer a troca dos valores, quando necessário.

# Essa versão do selection sort, na qual criamos uma lista vazia e, dentro de uma estrutura de repetição, usamos a função built-in min() para, a cada iteração, encontrar o menor valor da sequência e adicioná-lo na lista_ordenada.
# A cada iteração, o valor adicionado à nova lista é removido da lista original.


# INSERTION SORT (ORDENAÇÃO POR INSERÇÃO)

# O algoritmo insertion sort (algoritmo de inserção) recebe esse nome porque faz a ordenação pela simulação da inserção de novos valores na lista.
# Imagine um jogo de cartas para a execução do qual cada jogador começa com cinco cartas e, a cada rodada, deve pegar e inserir uma nova carta na mão.
# O jogador opta por deixar as cartas ordenadas em sua mão, razão pela qual, a cada nova carta que precisar inserir, ele olha a sequência da esquerda para a direita, procurando a posição exata para fazer a inserção.

# A lógica do algoritmo é a seguinte:
# Início: A lista possui um único valor, consequentemente, está ordenada.
# Iteração 1: Um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com o valor já existente para saber se precisa ser feita uma troca de posição.
# Iteração 2: Um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com os valores já existentes para saber se precisam ser feitas trocas de posição.
# Iteração N: Um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com todos os valores já existentes (desde o início) para saber se precisam ser feitas trocas de posição.

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir

    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada3 = executar_insertion_sort(lista)
print(lista_ordenada3)
    # [-1, 3, 5, 8, 9, 10, 11]

# Temos uma variável que guarda o tamanho da lista (n).
# Precisamos de duas estruturas de controle para iterar.
# Na primeira estrutura, usamos o for para controlar a variável i, que representa a posição do valor a ser inserido. 
# Uma vez que sabemos exatamente quantas vezes iterar, o for pode ser usado.
# O for começa na posição 1, pois o algoritmo parte do princípio de que a lista possui um valor e um novo precisa ser inserido.
# Inicializamos a variável j, com a posição anterior ao valor a ser inserido.
# Criamos a segunda estrutura de repetição com while, pois não sabemos quantas casas vamos ter de percorrer até encontrar a posição correta de inserção.
# O loop acontecerá enquanto houver elementos para comparar (j >= 0) e o valor da posição anterior (lista[j]) for maior que o valor a ser inserido.
# Enquanto essas condições acontecerem, os valores já existentes vão sendo "passados para frente" (linha 8) e j vai decrementando. Quando a posição for encontrada, o valor é inserido.

# Para todas as ordenações que fizemos até o momento, o tempo de execução foi instantâneo, pois as listas eram pequenas. E, se tivéssemos que ordenar uma lista com muitos valores, certamente perceberíamos uma lentidão na performance. Para suprir essa necessidade, existem algoritmos que, embora performem melhor, demandam um pouco mais de complexidade na implementação.


# MERGE SORT (ORDENAÇÃO POR JUNÇÃO)

# O algoritmo merge sort recebe esse nome porque faz a ordenação em duas etapas:
# 1º divide a lista em sublistas; e 2º junta (merge) as sublistas já ordenadas. Esse algoritmo é conhecido por usar a estratégia "dividir para conquistar".
# Essa estratégia é usada por algoritmos de estrutura recursiva:
# Para resolver um determinado problema, eles se chamam recursivamente uma ou mais vezes para lidar com subproblemas intimamente relacionados.
# Esses algoritmos geralmente seguem uma abordagem de dividir e conquistar: eles dividem o problema em vários subproblemas semelhantes ao problema original, mas menores em tamanho, resolvem os subproblemas recursivamente e depois combinam essas soluções para criar uma solução para o problema original.

# O paradigma de dividir e conquistar envolve três etapas em cada nível da recursão:
# 1º dividir o problema em vários subproblemas;
# 2º conquistar os subproblemas, resolvendo-os recursivamente – se os tamanhos dos subproblemas forem pequenos o suficiente, apenas resolva os subproblemas de maneira direta;
# 3º combine as soluções dos subproblemas na solução do problema original.

# Etapa de divisão:
# Com base na lista original, encontre o meio e separe-a em duas listas: esquerda_1 e direita_2.
# Com base na sublista esquerda_1, se a quantidade de elementos for maior que 1, encontre o meio e separe-a em duas listas: esquerda_1_1 e direta_1_1.
# Com base na sublista esquerda_1_1, se a quantidade de elementos for maior que 1, encontre o meio e separe-a em duas listas: esquerda_1_2 e direta_1_2.
# Repita o processo até encontrar uma lista com tamanho 1.
# Chame a etapa de merge.
# Repita o processo para todas as sublistas.

# Para entender a etapa de junção do merge sort, suponha que você está vendo duas fileiras de crianças em ordem de tamanho. Ao olhar para a primeira criança de cada fila, é possível identificar qual é a menor e, então, colocá-la na posição correta. Fazendo isso sucessivamente, teremos uma fila ordenada com base nas duas anteriores.


# ORDENANDO A LISTA [10, 9, 5, 8]:

# Começando pela etapa de divisão, é encontrado o meio da lista e é feita uma divisão, o que resulta nas sublistas [10, 9] do lado esquerdo e [5, 8] do lado direito.
# Como as sublistas possuem mais que um valor, então é feita uma quebra novamente – a sublista da esquerda gera duas novas listas [10] e [9]; e a sublista da direita, as novas listas [5] e [8].

# Alcançado o tamanho mínimo da lista, é hora de começar o processo de merge, que fará a junção de forma ordenada.
# Começando pela esquerda, as listas [10] e [9] são comparadas, gerando a sublista [9, 10].
# Do outro lado, as listas [5] e [8] são comparadas, gerando a sublista [5, 8].

# Agora é hora de fazer o novo merge entre essas sublistas de tamanho 2. 
# Podemos pensar nessas listas como pilhas ordenadas, no topo das quais está o menor valor de cada uma.
# Então, ao olhar para o topo de duas pilhas, vemos os valores 9 e 5 – como 5 é menor, ele é o primeiro escolhido para ocupar a posição 0.
# Olhando novamente para essa pilha, agora temos no topo os valores 9 e 8 – como 8 é menor, então ele é o segundo escolhido para compor a nova lista.
# Olhando novamente, agora temos somente uma pilha, em cujo topo está o valor 9, razão pela qual ele é escolhido e, por fim, o valor 10 é selecionado.
# Como não existem mais merges para serem feitos, o algoritmo encerra.


# Esse algoritmo possui mais complexidade de código.
# Primeiro ponto: vamos precisar de duas funções, uma que divide e outra que junta.
# Segundo ponto: a divisão é feita de maneira lógica, ou seja, as sublistas são "fatiamentos" da lista original.
# O algoritmo de merge vai sempre receber a lista inteira, mas tratará de posições específicas.
# Terceiro ponto: na etapa de divisão, serão feitas sucessivas subdivisões aplicando-se a mesma regra, tarefa para cuja realização vamos usar a técnica de recursão, fazendo chamadas recursivas a função de divisão.

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
lista_ordenada4 = executar_merge_sort(lista)
print(lista_ordenada4)
    # [-1, 3, 5, 8, 9, 10, 11]

# Criamos nossa função de ordenação por merge sort, que são duas funções, uma para dividir as listas (executar_merge_sort) e outra para fazer o merge (executar_merge).

# A função que faz a divisão recebe como parâmetro a lista a ser ordenada.
# Se o tamanho da lista é menor ou igual 1, isso significa que a sublista só tem 1 valor e está ordenada, razão pela qual seu valor é retornado; caso não seja, então é encontrado o meio da lista e feita a divisão entre sublistas da direita e da esquerda.
# Esse processo é feito recursivamente até que se tenha sublistas de tamanho 1.

# A função de junção, ao receber duas listas, percorre cada uma delas pelo while, e considerando cada valor, o que for menor é adicionado à sublista ordenada.


# QUICKSORT (ORDENAÇÃO RÁPIDA)

# Dado um valor em uma lista ordenada, à direita desse número existem somente números maiores que ele; e à esquerda, somente os menores.

# Esse valor, chamado de pivô, é a estratégia central no algoritmo quicksort.
# O algoritmo quicksort também trabalha com a estratégia de dividir para conquistar, pois, a partir do pivô, quebrará uma lista em sublistas (direita e esquerda) – a cada escolha do pivô e a cada quebra da lista, o processo de ordenação vai acontecendo.

# Suponha uma fila de pessoas que, por algum motivo, precisam ser ordenadas por ordem de tamanho.
# Pede-se para uma pessoa da fila se voluntariar para ter seu tamanho comparado (esse é o pivô).
# Com base nesse voluntário, todos que são menores que ele devem se dirigir para a esquerda e todos que são maiores para a direta.
# O voluntário está na posição ordenada.

# Vamos repetir o mesmo procedimento para os menores e maiores. A cada passo estamos dobrando o número de pessoas na posição final. A lógica é a seguinte:
# Primeira iteração: a lista original será quebrada através de um valor chamado de pivô.
# Após a quebra, os valores que são menores que o pivô devem ficar à sua esquerda e os maiores à sua direita.
# O pivô é inserido no local adequado, trocando a posição com o valor atual.

# Segunda iteração: agora há duas listas, a da direita e a da esquerda do pivô. Novamente são escolhidos dois novos pivôs e é feito o mesmo processo, de colocar à direita os menores e à esquerda os maiores.
# Ao final os novos pivôs ocupam suas posições corretas.

# Terceira iteração: olhando para as duas novas sublistas (direita e esquerda), repete-se o processo de escolha dos pivôs e separação.
# Na última iteração, a lista estará ordenada, como resultado dos passos anteriores.

def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo-1)
        executar_quicksort(lista, pivo+1, fim)
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
lista_ordenada5 = executar_quicksort(lista, inicio=0, fim=len(lista)-1)
print(lista_ordenada5)
    # [-1, 3, 5, 8, 9, 10, 11]

# Implementamos nosso quicksort em duas funções: executar_quicksort e executar_particao.
# A função executar_quicksort é responsável por criar as sublistas, cada uma das quais, no entanto, deve ser criada com base em um pivô.
# Por isso, caso a posição de início da lista seja menor que o fim (temos mais que 1 elemento), então é chamada a função executar_particao, que de fato faz a comparação e, quando necessário, troca os valores de posição, além de retornar o índice correto para o pivô.

# Fazemos a definição do pivô como o último valor da lista (e mesmo da sublista).
# Criamos a variável que controla a separação da lista da esquerda, ou seja, a lista que guardará os valores menores que o pivô.
# Usamos a estrutura de repetição para ir comparando o pivô com todos os valores da lista à direita.
# A cada vez que um valor menor que o pivo é encontrado, é feita a troca dos valores pelas posições, e a delimitação da lista dos menores (esquerda) é atualizada.
# O pivô é colocado na sua posição (limite da lista esquerda), fazendo a troca com o valor que ali está. Por fim, a função retorna o índice do pivô.


# Outra implementação do algoritmo, na qual usamos list comprehensions para criar uma lista de pivôs (agora o pivô é o primeiro valor da lista), uma lista com os valores menores e uma com os valores maiores.
# Esse processo é chamado recursivamente até que a lista esteja ordenada.

def executar_quicksort_2(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    iguais = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor < pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada6 = executar_quicksort_2(lista)
print(lista_ordenada6)
    # [-1, 3, 5, 8, 9, 10, 11]

# A performance de cada algoritmo vai depender da posição do valor na lista e do seu tamanho. Por exemplo, no algoritmo insertion sort, dado que o lado esquerdo é conhecido (e ordenado), se o valor a ser inserido é grande, o algoritmo terá uma boa performance. Por outro lado, o algoritmo selection sort, uma vez que verifica o mínimo para frente, que não se conhece, sempre está no pior caso.