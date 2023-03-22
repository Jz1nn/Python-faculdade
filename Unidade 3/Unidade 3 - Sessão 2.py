# BIBLIOTECAS E MÓDULOS

# Existem duas maneiras de organizar o código: implementar funções, onde cada bloco é responsável por uma funcionalidade específica, e outra é usar a orientação a objetos para criar classes que encapsulam as características e comportamentos de um objeto.
# Ambas as técnicas podem melhorar o código, mas ainda assim, isso resultaria em uma solução agrupada em um arquivo Python (.py).
# Idealmente, para modular uma solução, devemos separar as funções ou classes em vários arquivos .py. De acordo com a documentação oficial do Python, é recomendável separar em um arquivo separado qualquer funcionalidade que possa ser reutilizada, criando assim um módulo.

# Em Python, o termo "módulo" e "biblioteca" são comumente usados. No entanto, eles têm algo em comum: um módulo pode ser considerado como uma biblioteca de códigos.
# Por exemplo, existem vários módulos como o módulo math, que oferece funções matemáticas, e o módulo os, que oferece funções relacionadas ao sistema operacional, como a captura do caminho (getcwd), listagem de diretórios (listdir) e criação de novas pastas (mkdir).
# Esses módulos são considerados bibliotecas de funções específicas, o que possibilita a reutilização de código de uma forma eficiente e elegante.


# Para utilizar um módulo é preciso importá-lo para o arquivo:
# 1. import moduloXXText
#   1.2 import moduloXX as apelido

# 2. from moduloXX import itemA, itemB

# Utilizando as duas primeiras formas de importação (1 e 1.2), todas as funcionalidades de um módulo são carregadas na memória. A diferença entre elas é que, na primeira, usamos o nome do módulo e, na segunda, atribuímos a este um apelido (as = alias).
# Na forma de importação 2, somente funcionalidades específicas de um módulo são carregadas na memória.

# A forma de importação também determina a sintaxe para utilizar a funcionalidade:

import math
math.sqrt(25)
math.log2(1024)
math.cos(45)

print(math.cos(45))
    # 0.5253219888177297

import math as m

m.sqrt(25)
m.log2(1024)
m.cos(45)

print(math.cos(45))
    # 0.5253219888177297


from math import sqrt, log2, cos

m.sqrt(25)
m.log2(1024)
m.cos(45)

print(math.cos(45))
    # 0.5253219888177297

# Na entrada 1, usamos a importação que carrega todas as funções na memória. Linhas 3 a 5 que  precisamos usar a seguinte sintaxe: nomemodulo.nomeitem.

# Na entrada 2, usamos a importação que carrega todas as funções na memória, mas, no caso, demos um apelido para o módulo. Linhas 3 a 5 que, para usá-la, precisamos colocar o apelido do módulo: apelido.nomeitem.

# Na entrada 3, usamos a importação que carrega funções específicas na memória. Linhas 3 a 5 que, para usá-la, basta invocar a função.

# Todos os import devem ficar no começo do arquivo. É uma boa prática declarar primeiro as bibliotecas-padrão (módulos built-in), depois as bibliotecas de terceiros e, por fim, os módulos específicos criados para a aplicação. Cada bloco deve ser separado por uma linha em branco.


# CLASSIFICAÇÃO DOS MÓDULOS (BIBLIOTECAS)

# Podemos classificar os módulos (bibliotecas) em três categorias:

# Módulos built-in: embutidos no interpretador.
# Módulos de terceiros: criados por terceiros e disponibilizados via PyPI.
# Módulos próprios: criados pelo desenvolvedor.


# MÓDULOS BUILT-IN

# Ao instalar o interpretador Python, também é feita a instalação de uma biblioteca de módulos, que pode variar de um sistema operacional para outro.
# Como estão embutidos no interpretador, esses módulos não precisam de nenhuma instalação adicional.

# MÓDULO RANDOM

# Random é um módulo built-in usado para criar número aleatórios:

# random.randint(a, b): retorna um valor inteiro aleatório, de modo que esse número esteja entre a, b.
# random.choice(seq): extrai um valor de forma aleatória de uma certa sequência.
# random.sample(population, k): retorna uma lista com k elementos, extraídos da população.

import random

print(random.randint(0, 100))
print(random.choice([1, 10, -1, 100]))
print(random.sample(range(100000), k=12))
    # 80
    # 100
    # [18699, 46029, 49868, 59986, 14361, 27678, 69635, 39589, 74599, 6587, 61176, 14191]


# MÓDULO OS

# OS é um módulo built-in usado para executar comandos no sistema operacional:

# os.getcwd(): retorna uma string com o caminho do diretório de trabalho.
# os.listdir(path='.'): retorna uma lista com todas as entradas de um diretório. Se não for especificado um caminho, então a busca é realizada em outro diretório de trabalho.
# os.cpu_count(): retorna um inteiro com o número de CPUs do sistema.
# os.getlogin(): retorna o nome do usuário logado.
# os.getenv(key): retorna uma string com o conteúdo de uma variável de ambiente especificada na key.
# os.getpid(): retorna o id do processo atual.

import os

os.getcwd()
os.listdir()
os.cpu_count()
os.getlogin()
os.getenv(key='path')
os.getpid()


# MÓDULO RE

# O módulo re (regular expression) fornece funções para busca de padrões em um texto. Uma expressão regular especifica um conjunto de strings que corresponde a ela. As funções neste módulo permitem verificar se uma determinada string corresponde a uma determinada expressão regular. Essa técnica de programação é utilizada em diversas linguagens de programação, pois a construção de re depende do conhecimento de padrões. Vamos explorar as funções:

# re.search(pattern, string, flags=0): varre a string procurando o primeiro local onde o padrão de expressão regular produz uma correspondência e o retorna. Retorna None se nenhuma correspondência é achada.

# re.match(pattern, string, flags=0): procura por um padrão no começo da string. Retorna None se a sequência não corresponder ao padrão.

# re.split(pattern, string, maxsplit=0, flags=0): divide uma string pelas ocorrências do padrão.


# Considerando um cenário onde temos um nome de arquivo com a data: meuArquivo_20-01-2020.py.
# O objetivo é guardar a parte textual do nome em uma variável para a usarmos posteriormente.
# Serão utilizados os três métodos para fazer essa separação:
# O search() faz a procura em toda string, o match() faz a procura somente no começo (razão pela qual, portanto, também encontrará neste caso) e o split() faz a transformação em uma lista.
# Como queremos somente a parte textual, pegamos a posição 0 da lista.

import re

string = 'meuArquivo_20-01-2020.py'
padrao = "[a-zA-Z]*"

texto1 = re.search(padrao, string).group()
texto2 = re.match(padrao, string).group()
texto3 = re.split("_", string)[0]
print(texto1)
print(texto2)
print(texto3)
    # meuArquivo
    # meuArquivo
    # meuArquivo

# Na linha 4, foi construído uma expressão regular para buscar por sequências de letras maiúsculas e minúsculas [a-zA-Z], que pode variar de tamanho 0 até N (*).
# Nas linhas 6 e 7 usamos esse padrão para fazer a procura na string. Ambas as funções conseguiram encontrar; e, então, usamos a função group() da re para capturar o resultado.
# Na linha 8, usamos o padrão "_" como a marcação de onde cortar a string, o que resulta em uma lista com dois valores – como o texto é a primeira parte, capturamos essa posição com o [0].

# MÓDULO DATETIME

# Trabalhar com datas é um desafio nas mais diversas linguagens de programação. Em Python há um módulo built-in capaz de lidar com datas e horas.
# O módulo datetime fornece classes para manipular datas e horas. Uma vez que esse módulo possui classes, então a sintaxe para acessar os métodos deve ser algo similar a: modulo.classe.metodo().
# Dada a diversa quantidade de possibilidades de se trabalhar com esse módulo, vamos ver um pouco das classes datetime e timedelta.

import datetime as dt

# Operações com data e hora
hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)
uma_semana_atras = hoje - dt.timedelta(weeks=1)

agora = dt.time.now()
duas_horas_atras = agora - dt.timedelta(hours=2)

# Formatação
hoje_formatado = dt.datetime.strftime(hoje, "%d-%m-%Y")
ontem_formatado = dt.datetime.strftime(ontem, "d de %B de %Y")

# Conversão de string para data
data_string = '11/06/20119 15:30'
data_dt = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M")

# Foi usado algumas funcionalidades disponíveis no módulo datetime. Fizemos a importação com a utilização do apelido de dt, prática essa que é comum para nomes grandes.

# Foi usado o método today() da classe datetime para capturar a data e a hora do sistema.

# Foi usado a classe timedelta para subtrair 1 dia de uma data específica.

# Foi usado a classe timedelta para subtrair 1 semana de uma data específica.

# Foi usado o método now() da classe datetime para captura a data e hora do sistema.

# Foi usado a classe timedelta para subtrair 2 horas de uma data específica.

# Foi usado o método strftime() da classe datetime para formatar a aparência de uma data específica.

# Foi usado o método strptime() da classe datetime, para converter uma string em um objeto do tipo datetime. Essa transformação é interessante, pois habilita as operações que vimos.


# MÓDULOS DE TERCEIROS

# PyPI é a abreviação para Python Package Index, que é um repositório para programas Python. Programadores autônomos e empresas podem, com isso, criar uma solução em Python e disponibilizar em forma de biblioteca no repositório PyPI, o que permite que todos usufruam e contribuam para o crescimento da linguagem. 

# BIBLIOTECA REQUESTS

# A biblioteca requests habilita funcionalidades do protocolo HTTP, como o get e o post. Dentre seus métodos, o get() é o responsável por capturar informação da internet. Essa biblioteca foi construída com o intuito de substituir o módulo urllib2, que demanda muito trabalho para obter os resultados. O método get() permite que você informe a URL de que deseja obter informação. Sua sintaxe é: requests.get('https://XXXXXXX'). Para outros parâmetros dessa função, como autenticação, cabeçalhos, etc., consulte a documentação.


# Observe o código a seguir:
# Importamos a biblioteca requests e, na linha 3, usamos o método get() para capturar um conteúdo de uma API do github e guardar na variável info. Ao fazer uma requisição podemos olhar algumas informações da extração pela propriedade headers.

import requests

info = requests.get('https://api.github.com/events')
info.headers
print(info)
    # {'Server': 'GitHub.com', 'Date': 'Wed, 22 Mar 2023 19:56:42 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': 'W/"fbecde7ef9455b4dfaf0cec50f9770a969bd71605dadd25e35862d524d806a9b"', 'Last-Modified': 'Wed, 22 Mar 2023 19:51:41 GMT', 'X-Poll-Interval': '60', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Link': '<https://api.github.com/events?page=2>; rel="next", <https://api.github.com/events?page=10>; rel="last"', 'x-github-api-version-selected': '2022-11-28', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '58', 'X-RateLimit-Reset': '1679518549', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '2', 'Accept-Ranges': 'bytes', 'Transfer-Encoding': 'chunked', 'X-GitHub-Request-Id': 'EE6D:49E7:2512E:2871C:641B5D7A'}

print(info.headers['date']) # Data de extração
print(info.headers['server']) # Servidor de origem
print(info.headers['status']) # Status HTTP da extração, 200 é ok
print(info.encoding) # Encoding do texto
print(info.headers['last-modified']) # Data da última modificação da informação
    # Thu, 04 Jun 2020 22:09:33 GMT
    # GitHub.com
    # 200 OK
    # utf-8
    # Thu, 04 Jun 2020 22:04:33 GMT

# A propriedade headers retorna um dicionário de informações. Extraímos algumas informações dessa propriedade.
# Acessamos a data de extração; na linha 2, o servidor que foi acessado; na linha 3, o status da extração; na linha 4, a decodificação texto; e na linha 5, a data da última modificação da informação no servidor.
# Essas informações podem ser usadas em um relatório!

# Para acessar o conteúdo que foi extraído, podemos usar a propriedade text, que converte todo o conteúdo para uma string, ou então o método json(), que faz a conversão para uma lista de dicionários.

texto_str = info.text
print(type(texto_str))
texto_str[:100] # exibe somente os 100 primeiros caracteres
    # <class 'str'>
    # '[{"id":"12535753096","type":"PushEvent","actor":{"id":5858581,"login":"grahamegrieve","display_login'

texto_json = info.json()
print(type(texto_json))
texto_json[0]
    # <class 'list'>

# Temos o conteúdo como uma string e, o conteúdo como uma lista de dicionários. Nesse caso, bastaria usar a linguagem Python para fazer os devidos tratamentos e extrair as informações!


# Vamos utilizar a biblioteca requests para extrair informações da Copa do Mundo de Futebol Feminino, que aconteceu no ano de 2019.
# As informações estão disponíveis no endereço http://worldcup.sfg.io/matches, no formato chave:valor.
# Após extrair as informações, vamos gerar um relatório que contém informações de cada jogo no seguinte formato: (dia/mes/ano) - time 1 x time 2 = gols time 1 a gols time 2.

# primeiro passo extrair as informações com o request utilizando o método json().
import requests
import datetime as dt

jogos = requests.get('http://worldcup.sfg.io/matches').json()
print(type(jogos))
    # <class 'list'>

# Foi realizada a extração com o requests e já convertemos o conteúdo para json(). Como resultado, temos uma lista de dicionários.
# Estamos extraindo as informações do primeiro dicionário da lista, ou seja, as informações do primeiro jogo.
# Nossa missão é criar uma lógica que extraia as informações de cada jogo, conforme solicitado, e gere um relatório. Então vamos a lógica para extrair.

# segundo passo: percorrer cada dicionário da lista (ou seja, cada jogo) extraindo as informações
info_relatorio = []
file = open('relatorio_jogos.txt', "w") # cria um arquivo txt na pasta em que está trabalhando.

for jogo in jogos:
    data = jogo['datetime'] # extrai a data
    data = dt.datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ") # converte de string para data
    data = data.strftime("%d/%m/%Y") # formata
    
    nome_time1 = jogo['home_team_country']
    nome_time2 = jogo['away_team_country']

    gols_time1 = jogo['home_team']['goals']
    gols_time2 = jogo['away_team']['goals']
    
    linha = f"({data}) - {nome_time1} x {nome_time2} = {gols_time1} a {gols_time2}"
    file.write(linha + '\n') # escreve a linha no arquivo txt
    info_relatorio.append(linha)

file.close() # é preciso fechar o arquivo
info_relatorio[:5]
    # ['(07/06/2019) - France x Korea Republic = 4 a 0',
    #  '(08/06/2019) - Germany x China PR = 1 a 0',
    #  '(08/06/2019) - Spain x South Africa = 3 a 1',
    #  '(08/06/2019) - Norway x Nigeria = 3 a 0',
    #  '(09/06/2019) - Brazil x Jamaica = 3 a 0']

# Usamos uma estrutura de repetição para percorrer cada item do dicionário, extraindo as informações. Chamamos a atenção para as linhas 13 e 14, nas quais usamos duas chaves.
# Isso foi feito porque, dentro do dicionário, existe outro dicionário.
# 'home_team': {'country': 'France', 'code': 'FRA', 'goals': 4, 'penalties': 0}.
# Dentro da chave home_team existe um outro dicionário. Portanto, para acessar os gols, precisamos também acessar a chave interna goals, ficando então jogo['home_team']['goals'].

# Usamos a função built-in open() para criar um arquivo chamado relatorio_jogos.txt, no qual escreveremos informações – por isso o parâmetro "w".
# Escrevemos cada linha gerada no arquivo, concatenando com uma nova linha "\n" a cada informação gerada. Como passamos somente o nome do arquivo, ele será gerado na pasta onde estiver trabalhando.


# MATPLOTLIB

# Matplotlib é uma biblioteca com funcionalidades para criar gráficos.
# Vamos utilizar a interface Pyplot para criar um gráfico simples baseado nas informações que salvamos sobre os jogos da Copa do Mundo de Futebol Feminino de 2019.

# Fizemos a extração e criamos um relatório, salvando-o como relatorio_jogos.txt. Agora vamos ler os dados que foram persistidos no arquivo, extrair somente as datas no formado dd/mm e contabilizar quantos jogos aconteceram em cada data. Em seguida, vamos usar o Pyplot para construir esse gráfico de contagem.

# ler o arquivo salvo
file = open('relatorio_jogos.txt', 'r')
print('file = '. file, "/n")
info_relatorio = file.readlines()
file.close()
    # file = <_io.TextIOWrapper name='relatorio_jogos.txt' mode='r' encoding='cp1252'>
print("linha 1 =", info_relatorio[0])
    # linha 1 =  (07/06/2019) - France x Korea Republic = 4 a 0

# Para ler um arquivo, usamos a função built-in open(), passando como parâmetros o nome do arquivo e a opção 'r', que significa que queremos abrir o arquivo em modo leitura (r = read).
# A função open() retorna um objeto do tipo "_io.TextIOWrapper", conforme podemos observar pelo print.
# Para acessar o conteúdo do arquivo, precisamos usar a função readlines(), que cria uma lista, na qual cada elemento é uma linha do arquivo.
# Após a criação da lista, podemos fechar o arquivo. Imprimimos o primeiro item da lista criada, que corresponde à primeira linha do arquivo de que fizemos a leitura.
# Para cada linha, queremos somente a parte que corresponde ao dia e mês: dd/mm, razão pela qual vamos criar uma nova lista que contém somente essas datas.

# Extrair somente a parte 'dd/mm' da linha
datas = [linha[1:6] for linha in info_relatorio]
print(sorted(datas))
    # ['02/07', '03/07', '06/07', '07/06', '07/07', '08/06', '08/06', '08/06', '09/06', '09/06', '09/06', '10/06', '10/06', '11/06', '11/06', '11/06', '12/06', '12/06', '12/06', '13/06', '13/06', '14/06', '14/06', '14/06', '15/06', '15/06', '16/06', '16/06', '17/06', '17/06', '17/06', '17/06', '18/06', '18/06', '19/06', '19/06', '20/06', '20/06', '20/06', '20/06', '22/06', '22/06', '23/06', '23/06', '24/06', '24/06', '25/06', '25/06', '27/06', '28/06', '29/06', '29/06']

# Agora temos uma lista com todas as datas dos jogos e precisamos contar quantas vezes cada uma aparece.
# Assim vamos ter a quantidade de jogos por dia.
# Para fazer esse trabalho, vamos utilizar a operação count() disponível para os objetos do tipo sequência: sequencia.count(valor), que retorna quantas vezes o valor aparece na sequência.
# Então, se fizermos datas.count('08/06'), temos que obter o valor 3. Uma vez que ´precisamos fazer isso para todas as datas, vamos, então, usar uma list comprehension para fazer essa iteração. Para cada data, vamos gerar uma tupla com dois valores: (data, count). Em nossa lista final, queremos ter uma linha para cada data, exemplo: ('08/06', 3). Então, para remover as duplicações, vamos utilizar o construtor set().

datas_count = [(data, datas.count(data)) for data in set(datas)]
print(datas_count)
    # [('17/06', 4), ('22/06', 2), ('24/06', 2), ('08/06', 3), ('07/06', 1), ('18/06', 2), ('03/07', 1), ('07/07', 1), ('27/06', 1), ('28/06', 1), ('25/06', 2), ('09/06', 3), ('20/06', 4), ('13/06', 2), ('12/06', 3), ('19/06', 2), ('11/06', 3), ('14/06', 3), ('16/06', 2), ('10/06', 2), ('29/06', 2), ('02/07', 1), ('23/06', 2), ('15/06', 2), ('06/07', 1)]

# Com o passo anterior, temos uma lista de tuplas com a data e quantidade de jogos! Por uma questão de conveniência, vamos transformar essa lista em um dicionário usando o construtor dict().

datas_count = dict(datas_count)
print(datas_count)
    # {'17/06': 4, '22/06': 2, '24/06': 2, '08/06': 3, '07/06': 1, '18/06': 2, '03/07': 1, '07/07': 1, '27/06': 1, '28/06': 1, '25/06': 2, '09/06': 3, '20/06': 4, '13/06': 2, '12/06': 3, '19/06': 2, '11/06': 3, '14/06': 3, '16/06': 2, '10/06': 2, '29/06': 2, '02/07': 1, '23/06': 2, '15/06': 2, '06/07': 1}

# Essa transformação da lista para dicionário nos permite extrair as chaves (que são as datas) e os valores (que são as quantidades). Esses dois itens serão usados nos eixos x e y do gráfico.

# Agora que já preparamos os dados, vamos utilizar a interface Pyplot da biblioteca matplotlib para criar nosso gráfico.
# Para que possamos ver um gráfico dentro de um notebook, temos que habilitar a opção %matplotlib inline e importar a biblioteca.
# Fazemos isso nas linhas 1 e 2. Nas linhas 4 e 5, usamos as informações do nosso dicionário para definir os dados que serão usados nos eixos x e y.
# Na linha 7, configuramos o tamanho do nosso gráfico.
# Nas linhas 8 e 9 definimos os rótulos dos eixos.
# Na linha 10, configuramos uma rotação para as datas que vão aparecer no eixo x.
# A linha 12 é onde de fato criamos o gráfico, escolhendo a opção de barras (bar) e passando as informações a serem plotadas.
# Na linha 14, usamos a função show para exibir nosso gráfico.

# %matplotlib inline
# import matplotlib.pyplot as plt

eixo_x = datas_count.keys()
eixo_y = datas_count.values()

# plt.figure(figsize=(15, 5))
# plt.xlabel('Dia do mês')
# plt.ylabel('Quantidade de jogos')
# plt.xticks(rotation=45)

# plt.bar(eixo_x, eixo_y)

# plt.show()

# MÓDULOS PRÓPRIOS

# Os códigos podem ser organizados em diversos arquivos com extensão .py, ou seja, em módulos.
# Cada módulo pode importar outros módulos, tanto os pertencentes ao mesmo projeto, como os built-in ou de terceiros.
# Criamos um módulo (arquivo Python) chamado utils.py. Esse módulo possui uma função que cria uma conexão ssh com um determinado servidor.
# Podemos entender um cliente SSH como um túnel de comunicação. No módulo precisamos usar a biblioteca paramiko para construir essa conexão.
# A função create_ssh_client retorna um client, ou seja, a conexão em si. Em um outro módulo, chamado principal, importamos a função do módulo utils.
# É dentro do módulo principal que vamos utilizar a funcionalidade de conexão para copiar um arquivo que está em um servidor para outro local.
# É importante ressaltar que, da forma pela qual fizemos a importação, ambos os arquivos .py precisam estar no mesmo nível de pasta.

# Se precisarmos usar o módulo utils em vários projetos, é interessante transformá-lo em uma biblioteca e disponibilizá-la via PyPI.