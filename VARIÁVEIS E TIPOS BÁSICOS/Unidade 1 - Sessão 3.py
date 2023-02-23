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


auksjgdb