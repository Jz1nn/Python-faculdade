# UNIDADE 4

### SESSÃO 1
# BIBLIOTECA PANDAS

# ESTRUTURA DE DADOS
# Pandas é um pacote Python que fornece estruturas de dados projetadas para facilitar o trabalho com dados estruturados (tabelas) e de series temporais.

# Para utilizar a lib Pandas, é necessario fazer a instalacao (pip install pandas). Como uma ferramenta de alto nivel, pandas possui duas estrutudas de dados que sao as principais para a analise/manipulacao de dados: Series e DataFrame.

# Series é como um vetor de dados (unidimensional), capaz de armazenar diferentes tipos de dados. Um DataFrame é um conjunto de Series (ou um conteiner para series). Ambas estruturas possuem a indexacao das linhas, cada linha possui um rotulo (nome) que o identifica (pode ser uma string, inteiro, decimal ou uma data).

# Uma Series possui somente 'uma coluna' de informacao e seus rotulos (indices). Um DataFrame pode ter uma ou mais colunas alem dos indices (tambem ha um rotulo de identificacao para cada coluna). É possivel comparar um DataFrame com uma planilha eletronica (Excel).


# A seguir serao criados Series e DataFrames a partir de estruturas de dados do Python (listas, dicionarios, tuplas, etc). Apos a criacao, sera feita a extracao de informacoes da estrutura e selecionar colunas especificas.

# A lib é importada com o apelido: as pd. Para usar as funcionalidades a sintaxe é: pd.funcao().
import pandas as pd


# Series
# Para construir um objeto do tipo Series, é necessario usa o metodo 'Series()' do pandas, com o construtor: pandas.Series(date=None, index=None, dtype=None, name=None, copy=False, fastpath=False). Todos os parametros possuem valores default (permitindo instancia um objeto de diferentes formas).

# Dentre todos os parametros, somente um é obrigatorio para criar uma Series com dados, o parametro data=XXXX (se for uma Series sem dados, nenhum parametro é obrigatorio). Esse parametro pode receber: inteiro, string, float, uma lista de valores ou um dict.

pd.Series(data=5) # cria uma Series com valor 5
    # 0    5
    # dtype: int64

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(data=lista_nomes) # cria uma Series com os nomes da lista
    # 0    Howard
    # 1       Ian
    # 2     Peter
    # 3     Jonah
    # 4    Kellie
    # dtype: object

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie'
}

pd.series(data=dados) # cria uma Series com os dados do dict
    # nome1    Howard
    # nome2       Ian
    # nome3     Peter
    # nome4     Jonah
    # nome5    Kellie
    # dtype: object

# pd.Series(data=5) = Series com um unico valor, onde 0 é o indice e 5 é o valor. Quando nao é explicito o indice, é construido um range de 0 ate n-1.
# dtype: int64 = tipo de data onde temos somente um valor inteiro no objeto.

# pd.Series(data=lista_nomes) = Series criado a partir de uma lista de nomes, agora os indices variam de 0 - 4 e o dtype é object. Esse tipo de dado é usado para representar texto ou valores numericos/nao-numericos combinados.

# pd.series(data=dados) = Series criado a partir de um dict, onde os indices sao os nomes das chaves e os valores sao os valores das chaves.


# Outra forma de construir Series é passando os dados e rotulos que desejamos usar. A seguir sera usada uma lista de cpfs para rolular os valores da Series.
cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

pd.Series(lista_nomes, index=cpfs)
    # 111.111.111-11    Howard
    # 222.222.222-22       Ian
    # 333.333.333-33     Peter
    # 444.444.444-44     Jonah
    # 555.555.555-55    Kellie
    # dtype: object

# Rotular Series serve para facilitar a localizacao/manipulacao dos dados. Ex: saber o nome da pessoa com cpf 111.111.111-11, para saber a localizacao dessa informacao usando o atributo 'loc', com a sintaxe: series_dados.loc[rotulo], onde o rotulo é o indice a ser localizado.

# Criando uma Series com uma lista de nomes e guardados em uma variavel 'series_dados'. Usando o atributo 'loc', é localizado a informacao com o indice '111.111.111-11'.
series_dados = pd.Series(lista_nomes, index=cpfs)

series_dados.loc['111.111.111-11']
    # 'Howard'


# EXTRAIR INFORMACOES DE UMA SERIES
# Sera criado uma Series contendo numeros e um valor nulo (None). As informacoes extraidas, sao em relacao a "forma" dos dados, podendo ser usadas independente do tipo de dado armazenado na Series. Porem nas funcoes matematicas/estatisticas seguintes, faz mais sentido serem usadas para tipos numericos.
# A diferenca entre o atributo 'shape' e o metodo 'count()' é que o primeiro verifica quantas linhas a Series possui (indices) e o segundo quantos dados NAO NULOS existem.

series_dados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantas linhas = ', series_dados.shape) # retorna uma tupla com o numero de linhas
print('Tipo de dados', series_dados.dtypes) # retorna o tipo de dados, se for misto sera object 
print('Os valores sao unicos?', series_dados.is_unique) # verifica se os valores sao unicos (sem duplicacoes)
print('Existem valores nulos?', series_dados.hasnans) # verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) # conta quantos valores existem (exclui nulos)

print('Qual o menor valor?', series_dados.min()) # extrai o menor valor da Series (os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # extrai o maior valor da Series (os dados precisam ser do mesmo tipo)
print('Qual a media aritmetica?', series_dados.mean()) # extrai a media aritmetica de uma Series numerica
print('Qual o desvio padrao?', series_dados.std()) # extrai o desvio padrao de uma Series numerica
print('Qual a mediana?', series_dados.median()) # extrai a mediana de uma Series numerica

print('\nResumo:\n', series_dados.describe()) # exibe um resumo sobre os dados na Series
    # Quantidade de linhas =  (5)
    # Tipo de dados float64
    # Os valores são únicos? True
    # Existem valores nulos? True
    # Quantos valores existem? 4
    # Qual o menor valor? -1.0
    # Qual o maior valor? 23.4
    # Qual a média aritmética? 11.899999999999999
    # Qual o desvio padrão? 10.184301645179211
    # Qual a mediana? 12.6

    # Resumo:
    #  count     4.000000
    # mean     11.900000
    # std      10.184302
    # min      -1.000000
    # 25%       7.400000
    # 50%      12.600000
    # 75%      17.100000
    # max      23.400000
    # dtype: float64


# DATAFRAME
# Para construir um objeto desse tipo, é necessario usar o metodo 'DataFrame()'. O metodo possui o seguinte construtor: pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False). Todos os parametros possuem valores default (permitindo instanciar um objeto de diferentes formas).

# Dentre todos os parametros esperados, so 1 é obrigatorio para criar um DataFame com dados: data=XXXX. Esse parametro recebe um objeto iteravel como uma lista, tupla, dict ou um DataFrame.


# CONSTRUTOR DATAFRAME COM LISTA
# Serao criadas 4 listas com mesmo tamanho (5 valores) que serao usadas como fonte de dados para criar os primeiros DataFrames. Entao sera invocado o metodo 'DataFrame()' e passado como parametro a lista de nomes e um rotulo (indice) para a coluna.

# Como resultado, teremos os dados da coluna e os indices (como nao sera especificado o indice, sera criado um range de 0 ate n-1). Apos isso sera criado o mesmo DataFrame, agora passando a lista de cpfs como indice. Sera usado a funcao 'zip()' para criar as tuplas (cada uma com um valor de cada lista), e cada uma transformada em uma lista de tuplas. Fazendo essa construcao para criar um DataFrame, onde cada lista passe a ser uma coluna.

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

pd.DataFrame(lista_nomes, columns=['nome'])

pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas

pd.DataFrame(dados, columns=['nome', 'cpf', 'idade', 'email'])
    #     nome	cpfs	         idade	           email
    # 0	Howard	111.111.111-11	  32	      risus.varius@dictumPhasellusin.ca
    # 1	Ian	    222.222.222-22	  22	      Nunc@vulputate.ca
    # 2	Peter	333.333.333-33	  25	      fames.ac.turpis@cursusa.org
    # 3	Jonah	444.444.444-44	  29	      non@felisullamcorper.org
    # 4	Kellie	555.555.555-55	  38	      eget.dictum.placerat@necluctus.co.uk


# CONSTRUTOR DATAFRAME COM DICIONARIO
# Usando um dict para criar um DataFrame, cada chave sera uma coluna e pode ser atribuida uma lista de valores. OBS: cada chave deve estar associada a uma lista do mesmo tamanho. Sera criado o dict de dados, onde cada chave possui uma lista do mesmo tamanho. Sera criado o DataFrame passando o dict como fonte de dados (o construtor ja consegue identificar o nome das colunas).

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

pd.DataFrame(dados)
    #   nomes	     cpfs	                   emails	            idades
    # 0	Howard	111.111.111-11	risus.varius@dictumPhasellusin.ca	 32
    # 1	Ian	    222.222.222-22	        Nunc@vulputate.ca	         22
    # 2	Peter	333.333.333-33	fames.ac.turpis@cursusa.org	         25
    # 3	Jonah	444.444.444-44	non@felisullamcorper.org	         29
    # 4	Kellie	555.555.555-55	eget.dictum.placerat@necluctus.co.uk 38


# EXTRAIR INFORMACOES DO DATAFRAME
# Embora Series e DataFrames possuam recursos em comum, eles possuem suas proprias particularidades. No DataFrame temos o metodo 'info()' que mostra quantas linhas e colunas existem, exibe tambem o tipo de cada coluna e quantos valores NAO NULOS existem. Esse metodo tambem retorna uma informacao sobre a quantidade de memoria RAM que a estrutura ocupa.

df_dados = pd.DataFrame(dados)

print('\nInformacoes do DataFrame:\n')
print(df_dados.info()) # apresenta informacoes sobre a estrutura do DF

df_dados.head() # Exibe os 5 primeiros registros do DataFrame
    # Informações do DataFrame:

    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 5 entries, 0 to 4
    # Data columns (total 4 columns):
    # nomes     5 non-null object
    # cpfs      5 non-null object
    # emails    5 non-null object
    # idades    5 non-null int64
    # dtypes: int64(1), object(3)
    # memory usage: 240.0+ bytes
    # None


# SELEÇÃO DE COLUNAS EM UM DATAFRAME
# Podemos realizar operações em colunas especificas de um DF ou criar um novo objeto contendo somente as colunas que serao usadas para analise. As sintaxes para selecionar uma coluna:

# nome_df.nome_coluna
# nome_df[nome_coluna]

# A primeira nao aceita colunas com espacos entre as palavras. A segunda aceita, se precisar selecionar mais de uma coluna, é necessário passar uma lista: nome_df[['col1', 'col2', 'col3']] (se preferir a lista pode ser criada fora da secao e passada como parametro).

# Selecionando uma coluna é obtido uma Series, então podemos aplicar seus atributos e métodos,  Ex: para obter a media aritmetica de uma determinada coluna. Nos codigos a seguir, sera feita a seleção de uma única coluna (idades), a impressão do tipo do objeto agora é Series. A partir desse objeto, sera impresso a media de idade.

# No outro codigo, sera criado uma lista com as colunas que queremos selecionar e sera passado essa lista para selecao (df_dados[colunas]), obteremos um novo DF, agora com 2 colunas.

# Com selecoes de certas colunas podemos extrair informacoes especificas e compara-las com outras colunas ou outros dados.

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))

print('Media de idades = ', df_uma_coluna.mean())

df_uma_coluna
    # <class 'pandas.core.series.Series'>
    # Média de idades =  29.2
    # 0    32
    # 1    22
    # 2    25
    # 3    29
    # 4    38
    # Name: idades, dtype: int64

colunas = ['nomes', 'cpfs']
df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))
df_duas_colunas
    # <class 'pandas.core.frame.DataFrame'>
    #   nomes	     cpfs
    # 0	Howard	111.111.111-11
    # 1	Ian	    222.222.222-22
    # 2	Peter	333.333.333-33
    # 3	Jonah	444.444.444-44
    # 4	Kellie	555.555.555-55


# WEB SCRAPING - RASPAGEM WEB
# Acessando a pagina de noticias do jornal New York Times (https://nyti.ms/3aHRu2D), sera criado um DF contendo o dia da noticia, o comentario que foi feito, a explicacao dada e o link da noticia.

# Sera usado a lib 'requests' para raspagem, com o metodo requests.get() e convertendo tudo para uma string (usando propriedade text). Entao sera impresso os 100 primeiros caracteres do texto.

import requests

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])
    # <!DOCTYPE html>
    # <!--[if (gt IE 9)|!(IE)]> <!--><html lang="en" class="no-js page-interactive section

# Como temos um conteudo em HTML, precisamos usar a lib BeautifulSoup para converter a string em uma estrutura HTML e filtrar as tags. No codigo a seguir, sera importada a lib e atraves da classe BeautifulSoup, sera instanciado um objeto passando o texto em string e o parametro 'html.parser'.

# Com o objeto do tipo BS, podemos usar o metodo 'find_all()' para buscar todas ocorrencias de determinada tag. Sera buscado todas as tags 'span' que contenham um atributo 'class':'short-desc'. O resultado dessa busca é um conjunto iteravel, como uma lista. Entao sera exibida a noticia no indice 5 desse iteravel, apos isso sera exibido o "conteudo" desse mesmo elemento.

# OBS: para saber qual tag buscar, é preciso examinar o codigo fonte da pagina que deseja raspar.

from bs4 import BeautifulSoup

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})

print(type(bsp_texto))
print(type(lista_noticias))
print(lista_noticias[5])

lista_noticias[5].contents
    # <class 'bs4.BeautifulSoup'>
    # <class 'bs4.element.ResultSet'>
    # <span class="short-desc"><strong>Jan. 25 </strong>“You had millions of people that now aren't insured anymore.” <span class="short-truth"><a href="https://www.nytimes.com 2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html" target="_blank">(The real number is less than 1 million, according to the Urban Institute.)</a></span></span>[<strong>Jan. 25 </strong>,"“You had millions of people that now aren't insured anymore.” ",<span class="short-truth"><a href="https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html" target="_blank">(The real number is less than 1 million, according to the Urban Institute.)</a></span>]

# Agora sera criada uma estrutura de repeticao para percorrer cada noticia do objeto iteravel, extraindo as informacoes necessarias.

# 1. Criado uma lista vazia

# 2. O código noticia.contents[0] retorna:
    # <strong>Jan. 25 </strong>
# Ao acessar a propriedade text, eliminamos as tags então temos:
    # Jan. 25.
# Usamos a função strip() para eliminar espaço em branco na string e concatenamos com o ano.

# 3. O código contents[1] retorna:
    # "“You had millions of people that now aren't insured anymore.”"
# Usamos o strip() para eliminar espaços em branco e a função replace para substituir os caracteres especiais por nada.

# 4. O código noticia.contents[2] retorna:
    # <a href="https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html" target="_blank" >(The real number is less than 1 million, according to the Urban Institute.)</a></span>
# Ao acessar a propriedade text, eliminamos as tags então temos
    # (The real number is less than 1 million, according to the Urban Institute.)
# O qual ajustamos para eliminar espaços e os parênteses.

# 5. O código noticia.find('a')['href'] retorna:
    # https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html

# Apeendamos a lista de dados uma tupla com as quatro informações extraidas.

dados = []

for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017' # dessa informacao <string>Jan. 25 </strong> vai extrair Jan. 25, 2017
    comentario = noticia.contents[1].strip().replace('"', '') # dessa informacao <string>"“You had millions of people...
    explicacao = noticia.contents[2].text.strip().replace('(', '').replace(')', '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

dados[1]
    # ('Jan. 21, 2017','A reporter for Time magazine — and I have been on their cover 14 or 15 times. I think we have the all-time record in the history of Time magazine.','Trump was on the cover 11 times and Nixon appeared 55 times.','http://nation.time.com/2013/11/06/10-things-you-didnt-know-about-time/')

# Agora com a lista de tuplas com os dados, sera criado um DF com esses dados. No codigo a seguir, sera usado o construtor DF passando os dados e o nome das colunas. Usando o atributo 'shape' é possivel saber que foram extraidas 180 noticias e cada coluna possui o tipo object.

df_noticias = pd.DataFrame(dados, columns=['data', 'comentario', 'explicacao', 'url'])

print(df_noticias.shape)
print(df_noticias.dtypes)
df_noticias.head()
    # (180, 4)
    # data          object
    # comentario    object
    # explicacao    object
    # url           object
    # dtype: object
    #          data                                          comentario                                          explicacao                                                url
    # 0  Jan. 25, 2017  “You had millions of people that now aren't ins...  The real number is less than 1 million, accordi...  https://www.nytimes.com/2017/03/13/us/politics/...
    # 1  Jan. 21, 2017  A reporter for Time magazine — and I have been ...  Trump was on the cover 11 times and Nixon appea...  http://nation.time.com/2013/11/06/10-things-you...
    # 2  Jan. 20, 2017  Take a look at the Pew reports (which show voti...  Among states with relevant data, Pew found that...  http://www.factcheck.org/2017/01/trumps-claim-o...
    # 3  Jan. 20, 2017  We've taken in tens of thousands of people. We ...  The United States admitted 110,574 refugees in ...  http://www.factcheck.org/2017/01/trumps-claim-t...
    # 4  Jan. 20, 2017  As of this morning, it's 109 people. We caught ...  The statement was made at Trump's first press c...  http://www.factcheck.org/2017/01/trumps-claim-t...


# LEITURA DE DADOS ESTRUTURADOS COM A LIB PANDAS