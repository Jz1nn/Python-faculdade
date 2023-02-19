# CONDICIONAIS

# Estrutura condicional simples

a = 5
b = 10

if a < b:
    print("a é menor que b")
    r = a + b
    print(r)


#estrutura condicional composta

a = 10
b = 5

if a < b:
    print("a é menor que b")
    r = a + b
    print(r)
else:
    print("a é maior que b")
    r= a - b
    print(r)

# Para construir uma estrutura encadeada, devemos usar o comando "elif", que é uma abreviação de else if.

codigo_compra = 5111

if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

# ESTRUTURAS LÓGICAS EM PYTHON: AND, OR, NOT

# Operador booleano AND: O resultado será True quando os dois argumentos forem verdadeiros.
# Operador booleano OR: O resultado será True quando pelo menos um dos argumentos for verdadeiro.
# Operador booleano NOT A: Irá inverter o valor do argumento. Portanto, se o argumento for verdadeiro, a operação o transformará em falso e vice-versa.

# EXEMPLO: Um aluno só pode ser aprovado caso ele tenha menos de 5 faltas e média final superior a 7.

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

# Primeiro é feito a função input() e depois será convertida para inteira com a função int()

# Operações booleanas prioridade: 
# not 
# and
# or

A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)

# ESTRUTURAS DE REPETIÇÃO EM PYTHON: WHILE E FOR

# WHILE
# Sempre que o número de repetições não seja conhecido. 
# Por exemplo, quando queremos solicitar e testar se o número digitado pelo usuário é par ou ímpar.

numero = 1
while numero != 0:
    numero = int(input("Digite um número: ")) #Converter "string" para "int" o input().
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

# FOR
# "c" percorre a string assumindo seu conteúdo.

nome = "John"
for c in nome:
    print(c)

# Função enumerate() para retornar à posição de cada item dentro da sequência.
# Para que possamos capturar tanto a posição quanto o valor, vamos precisar usar duas variáveis de controle.
# A variável "i" é usada para capturar a posição e a variável "c" cada caractere da palavra.

nome = "John"
for i, c in enumerate(nome):
    print(f"posição = {i}, valor = {c}")

# CONTROLE DE REPETIÇÃO COM RANGE, BREAK E CONTINUE

# O comando FOR em Python requer uma sequência para que ocorra a iteração.
# Para criar uma sequência numérica de iteração em Python, podemos usar a função range().

for x in range(5):
    print(x)

# "X" é a variável de controle, a cada iteração do laço seu valor é alterado.
# "Range()" foi utilizada para criar um "iterable" numérico (objeto iterável) para que as repetições acontecesse.

# A função range() pode ser usada de três formas distintas:
# 1: passando um único argumento que representa a quantidade de vezes que o laço deve repetir;
# 2: passando dois argumentos, um que representa o início das repetições e outro o limite superior (NÃO INCLUÍDO) do valor da variável de controle;
# 3: Passando três argumentos, início das repetições; limite superior (NÃO INCLUÍDO) da variável de controle; um que representa o incremento (ex:"2" = 2,4,6,8);

# Método 1:

for i in range(10):
    print(i)

# Método 2:

for i in range(0, 5):
    print(i)

# Método 3:

for i in range(0, 20, 2):
    print(i)

# BREAK e CONTINUE

# BREAK para a execução de uma estrutura de repetição.
# CONTINUE pula algumas execuções, dependendo de uma condição.

disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

# Quando chegou a primeira letra "A", a estrutura de repetição foi interrompida.

disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)

# Foram impressas todas as letras, exceto vogais "a". Toda vez que elas eram encontradas, determina que pule, mas que a repetição prossiga para o próximo valor.

# EXEMPLIFICANDO
# Criar uma solução que procura pelas vogais "a", "e" em um texto.
# Toda vez que essas vogais são encontradas, devemos informar que encontramos e qual posição do texto ela está.

texto = """A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado"""

for i, c in enumerate(texto):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print(f"vogal '{c}' encontrada na posição {i}")
    else:
        continue

# "i" variável que percorre o texto e lê a posição, "c" variável que assume cada caractere.