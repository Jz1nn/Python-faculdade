# ENUNCIADO

# Diante da solução feita no Desafio 2 onde foi feito o dedup em uma lista de CPFs, retornar somente parte numérica do CPF e verificar se eles possuem 11 dígitos. Agora a lista de CPFs deve ser organizada de forma crescente para facilitar o cadastro. A lista de CPFs pode crescer exponencialmente, escolher os algoritmos mais adequados é importante nesse caso.

# DEVERÁ SER FEITO:
# Realizar as transformações de limpeza e validação nos CPFs (remover ponto e traço, verificar se tem 11 dígitos e não deixar valores duplicados).
# E também realizar a entrega em ordem crescente.


# RESOLUÇÃO:

# A melhor forma de resolver o problema é usando a busca binária (pois performa melhor que a busca linear), apesar de que os dados precisam estar ordenados.
# Porém os dados podem ser ordenados implementando algoritmos de ordenação.
# Com a informação de que a quantidade de CPFs podem aumentar exponencialmente, portanto a melhor opção dos algoritmos de ordenação é o MERGE-SORT, visto que para a demanda do cliente, no pior caso é o que tem menor complexidade de tempo.

# Parte 1 - Implementar o algoritmo de ordenação merge sort:

def executar_merge_sort(lista, inicio=0, fim=None):
    if not fim:
        fim = len(lista)
        
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
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

# Parte 2 - Implementar o algoritmo de busca binária:

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

# Parte 3 - Implementar a função que faz a verificação do cpf, o dedup e devolve o resultado esperado:

def criar_lista_dedup_ordenada(lista):
    lista = [str(cpf).replace('.','').replace('-','') for cpf in lista]
    lista = [cpf for cpf in lista if len(cpf) == 11]
    lista = executar_merge_sort(lista)
    
    lista_dedup = []
    for cpf in lista:
        if not executar_busca_binaria(lista_dedup, cpf):
            lista_dedup.append(cpf)
    return lista_dedup

# Parte 4 - Criar uma função de teste:

def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
lista_ordenada1 = testar_funcao(lista_cpfs)
    # ['11111111111', '22222222222', '33333333333', '44444444444']

# Foi implementado o algoritmo de ordenação MERGE SORT e BUSCA BINARIA.

# No algoritmo de ordenação, foi feito um tratamento na variável "fim" para que não precise ser passada explicitamente na primeira chamada.

# Na função criar_lista_dedup_ordenada:
# Foi usado uma list comprehension para remover o ponto e o traço dos CPFs.
# Foi criado novamente uma list comprehension, agora para guardar somente os CPFs que possuem 11 dígitos.

# Em posse dos CPFs válidos, chamamos a função de ordenação.
# Agora que temos uma lista ordenada, podemos usar a busca binária para verificar se o valor já está na lista; caso não estiver, então ele é adicionado.

# Por fim foi implementado uma função de teste para checar se não há nenhum erro e se a lógica está correta.