# ENUNCIADO

# DEDUP = deduplicação de dados, consiste em eliminar registros duplicados dos dados.

# Implementar uma solução que receba uma lista de CPFs, aplique a transformação "dedup" e retorne apenas a parte numérica dos CPFs. Verificar se os CPFs possuem 11 dígitos e eliminar aqueles que não possuem. Para realizar a deduplicação, você precisa escolher entre um algoritmo de busca linear ou binária. Também é necessário remover os caracteres ponto (.) e traço (-) que frequentemente aparecem nos CPFs antes de verificar se eles possuem 11 dígitos.

# RESOLUÇÃO:

# Será utilizado um algoritmo de busca linear, ja que não podemos garantir que os CPFs virão ordenados (exigência da busca binária). CPFs possuem números, traço e pontos, serão tratados como "string" para poder usar a função "replace()" para trocar um caractere por outro. Será usado a função "len()" para verificar se o CPF possui 11 dígitos.

# Implementar o algoritmo de busca linear:
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Criar a função que faz o dedup e os tratamentos do cpf:
def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf)

    return lista_dedup

# Criar função de teste:
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)
    # ['11111111111', '22222222222', '33333333333']

# Implementado solução em 3 etapas. As etapas 1 e 2 são parte da solução, a etapa 3 é uma boa prática de programação, ja que toda solução, é viável ter uma ou mais funções de teste.

# Na primeira parte, implementamos a função de busca linear, a qual vai receber uma lista e um valor a ser procurado. Nesse algoritmo, toda a lista é percorrida até encontrar (ou não) o valor.
# Na segunda parte da solução, implementamos a função que faz ajustar o CPF, que valida seu tamanho e que faz o dedup.

# Criamos uma estrutura de dados, do tipo lista, vazia. Essa lista armazenará os valores únicos dos CPFs.
# Criamos a estrutura de repetição, que percorrerá cada CPF da lista original.
# Fazemos o cast (conversão forçada) do CPF para o tipo string. Quando percorremos uma lista, cada elemento pode ter um tipo diferente.

# Usado um encadeamento da função replace para substituir o traço por "nada". Quando usamos replace("-", ""), o primeiro elemento é o que queremos substituir e o segundo é o que queremos colocar no lugar. Não há nada dentro das aspas, ou seja, o traço será apenas removido. O mesmo acontece para o ponto.
# Checamos se o tamanho do CPF é 11. Se não for, nada acontece, e o loop passa para a próxima iteração. Se for, então passamos para a proxima linha.

# Invocamos a função de busca, passando como parâmetro a lista_dedup (que é a lista final que queremos) e o CPF. Essa função vai procurar, na lista_dedup, o valor. Caso o encontre, retornará True; caso não o encontre, retornará False. Queremos justamente os casos falsos, pois isso quer dizer que o CPF ainda não está na lista correta, razão pela qual usamos if not. Caso não esteja, então passamos a proxima linha.

# Adicionamos à lista_dedup o CPF, já validado, transformado e com a garantia de que não está duplicado.
# Na terceira parte da solução, apenas fazemos um teste. Dada uma sequência fictícia de CPFs, veja que o resultado é exatamente o que queremos: CPFs somente numéricos sem duplicações. Veja como o algoritmo foi capaz de lidar com CPFs que contêm traços e pontos da mesma forma que o fez com os somente numéricos.