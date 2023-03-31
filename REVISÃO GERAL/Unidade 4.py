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
# Um dos recursos da lib Pandas é a leitura de dados estruturados (csv, excel, json, html, sql, etc) e guardar em um DF. Possui uma serie de metodos "read", cuja sintaxe é: pd.read_<formato>(<caminho_arquivo>).

# No codigo a seguir sera feita a leitura de uma tabela em uma pagina web usando o metodo pd.read_html(). O construtor possui os seguintes parametros: pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True).
# Dentre todos, somente o "io" é o que recebe a URL a ser usada. Esse metodo procura por tags <table> na estrutura do codigo HTML e retorna uma lista de DF contendo as tabelas que encontrou.

# Na URL https://www.fdic.gov/bank/individual/failed/banklist.html, está uma tabela com bancos norte americanos que faliram desde 1 de outubro de 2000 (cada linha um banco). Sera usado o metodo read_html() para capturar os dados e carregar em um DF. O metodo captura as tabelas no endereco passado como parametro, cada tabela é armazenada em um DF e o metodo retorna uma lista com todos eles.
# Ao imprimir o tipo de resultado guardado na variavel 'dfs', é obtido uma lista. Ao verificar quantos DF foram criados (len(dfs)), somente uma tabela foi encontrada, pois o tamanho da lista é 1.

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))
    # <class 'list'>
    # 1

# O tamanho da lista resultado do metodo é 1, entao para obter a tabela necessaria, pasta acessar a posicao 0 da lista. No codigo a seguir, é guardado o unico DF da lista em uma nova variavel. É verificado quantas linhas existem e os tipos de cada coluna, com excessao da coluna CERT, todas as demais sao texto.

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)
df_bancos.head()
    # (561, 6)
    # Bank Name           object
    # City                object
    # ST                  object
    # CERT                 int64
    # Acquiring Institution    object
    # Closing Date        object
    # dtype: object
    # 	       Bank Name	                   City	        ST	  CERT	    Acquiring Institution	            Closing Date
    # 0	The First State Bank	            Barboursville	WV	  14361	    MVB Bank, Inc.	                    April 3, 2020
    # 1	Ericson State Bank	                Ericson	        NE	  18265	    Farmers and Merchants Bank	        February 14, 2020
    # 2	City National Bank of New Jersey	Newark	        NJ	  21111	    Industrial Bank	                    November 1, 2019
    # 3	Resolute Bank	                    Maumee	        OH	  58317	    Buckeye State Bank	                October 25, 2019
    # 4	Louisa Community Bank	            Louisa	        KY	  58112	    Kentucky Farmers Bank Corporation	October 25, 2019


# DESAFIO
# Como desenvolvedor em uma empresa de consultoria de software, você foi alocado em uma equipe de marketing analítico em uma marca esportiva, que necessita fazer a coleta das principais notícias do mundo de esporte em um determinado portal https://globoesporte.globo.com/. O cliente deseja um componente capaz de fazer a extração dos dados em forma tabular, com o seguintes campos: manchete, descrição, link, seção, hora da extração, tempo decorrido da publicação até a hora da extração.

# O grande desafio no trabalho de web scraping é descobrir qual o padrão nas tags HTML e atributos CSS usados. Pois somente através deles é que conseguiremos alcançar a informação solicitada. Como o cliente já trabalha com o portal de notícias, foram lhe passadas as seguintes informações técnicas que o ajudarão a fazer a extração.

# Para extração de todas as informações localize todas as div com atributo 'class':'feed-post-body'. De cada item localizado extraia:
# 1. A manchete que ocupa a primeira posição do conteúdo.
# 2. O link que pode ser localizado pela tag "a" e pelo atributo "href".
# 3. A descrição pode estar na terceira posição conteúdo ou dentro de uma div com atributo 'class':'bstn-related'
# 4. A seção está dentro de uma div com atributo 'class':'feed-post-metadata'. Localize o span com atributo 'class': 'feed-post-metadata-section'.
# 5. O tempo decorrido está uma div com atributo 'class':'feed-post-metadata'. Localize o span com atributo 'class': 'feed-post-datetime'.

# Caso tente acessar o texto de uma tag não localizada, um erro é dado, para evitar esses casos, os campos descrição, seção e time_delta devem ser tratados para esses casos, retornando None (nulo).

# RESOLUCAO
# Para fazer o WEB SCRAPING solicitado, serao usadas as libs requests, beautifulsoup4, pandas e datetime. Sendo que as duas primeiras serao usadas para fazer a captura do conteudo da pagina, pandas para entregar os resultados em forma estruturada e datetime para marcar o dia e hora da captura.

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sera acessado o portal e utilizado a propriedade 'text' da lib requests e capturar em formato de string. Apos isso, a strings era transformada em formato HTML para localizar as tags desejadas. Entao sera registrado horario da extracao, e  serao localizadas todas as tags 'div' com o atributo que retornara uma lista com cada noticia.

# Serao impressas quantas noticias foram localizadas e o conteudo da primeira noticia. Contents transforma cada inicio e final da div em um elemento da lista.

texto_string = requests.get('https://globoesporte.globo.com/').text
hora_extracao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
print('Quantidade de manchetes = ', len(lista_noticias))
lista_noticias[0].contents
    # Quantidade de manchetes =  10
    # [<div class="feed-post-header"></div>,<div class="_label_event"><div class="feed-post-body-title gui-color-primary gui-color-hover"><div class="_ee"><a class="feed-post-link gui-color-primary gui-color-hover" href="https://globoesporte.globo.com/futebol/futebol-internacional/futebol-italiano/jogo/17-06-2020/napoli-juventusita.ghtml">VICE SENHORA</a></div></div></div>,<div class="_label_event"><div class="feed-post-body-resumo">Napoli vence Juventus nos pênaltis e leva Copa da Itália</div></div>,<div class="feed-media-wrapper"><div class="_label_event"><a class="feed-post-figure-link gui-image-hover" href="https://globoesporte.globo.com/futebol/futebol-internacional/futebol-italiano/jogo/17-06-2020/napoli-juventusita.ghtml"><div class="bstn-fd-item-cover"><picture class="bstn-fd-cover-picture"><img alt="Foto: (Alberto Lingria/Reuters)" class="bstn-fd-picture-image" src="https://s2.glbimg.com/BeTGAixT5O_Cvs4hQA88PdHiCsY=/0x0:5406x3041/540x304/smart/https://i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/G/4/GZIncSSPmVRWLaYiNGIg/2020-06-17t212444z-1091152315-rc29bh9icqss-rtrmadp-3-soccer-italy-nap-juv-report.jpg" srcset="https://s2.glbimg.com/BeTGAixT5O_Cvs4hQA88PdHiCsY=/0x0:5406x3041/540x304/smart/https://i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/G/4/GZIncSSPmVRWLaYiNGIg/2020-06-17t212444z-1091152315-rc29bh9icqss-rtrmadp-3-soccer-italy-nap-juv-report.jpg 1x,https://s2.glbimg.com/A6dTbIFD8sDl_t7eMHvA-2ONF0Y=/0x0:5406x3041/810x456/smart/https://i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/G/4/GZIncSSPmVRWLaYiNGIg/2020-06-17t212444z-1091152315-rc29bh9icqss-rtrmadp-3-soccer-italy-nap-juv-report.jpg 1.5x,https://s2.glbimg.com/n_XVqiX_3nn_wSar4FYy5I-cPUw=/0x0:5406x3041/1080x608/smart/https://i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/G/4/GZIncSSPmVRWLaYiNGIg/2020-06-17t212444z-1091152315-rc29bh9icqss-rtrmadp-3-soccer-italy-nap-juv-report.jpg 2x" title="Foto: (Alberto Lingria/Reuters)"/></picture></div></a></div></div>,<div class="feed-post-metadata"><span class="feed-post-datetime">Há 3 horas</span><span class="feed-post-metadata-section"> futebol italiano </span></div>]    

# Procurando pelas tags corretas dentro da estrutura, serao encontradas todas as informacoes solicitadas. Pela saida anterior, nota-se que a manchete ocupa a posicao 2 da lista de conteudos, entao para guardar a manchete sera feito o seguinte:

lista_noticias[0].contents[1].text.replace('"', '')
    # 'VICE SENHORA'

# O link da noticia se encontra na posicao 1 da lista de conteudos, entao para guardar o link sera usado o metodo find('a'):

lista_noticias[0].find('a')['href']
    # 'https://globoesporte.globo.com/futebol/futebol-internacional/futebol-italiano/jogo/17-06-2020/napoli-juventusita.ghtml'

# A descricao pode estar na posicao 3 ou em outra tag, entao sera testado em ambas, e caso nao esteja retornara None (nulo):

descricao = lista_noticias[0].contents[2].text
if not descricao:
    descricao = lista_noticias.find('div', attrs={'class': 'bstn=related'})
    descricao = descricao.text if descricao else None # somente acessara a propriedade text caso tenha encontrado ("find") 
descricao
    # 'Napoli vence Juventus nos pênaltis e leva Copa da Itália'

# Para extrair a sessao e o tempo decorrido, sera acessado o primeiro atributo 'feed-post-metadata' e guardado em uma variavel, entao em seguida dentro desse novo subconjunto, sera localizado os atributos 'feed-post-datetime' e 'feed-post-metadata-section'. É possivel que nao exista essa informacao, entao é preciso garantir que so sera acessada a propriedade 'text' caso seja encontrado ('find').

metadados = lista_noticias[0].find('div', attrs={'class': 'feed-post-metadata'})

time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

time_delta = time_delta.text if time_delta else None
secao = secao.text if secao else None

print('time_delta: ', time_delta)
print('secao: ', secao)
    # time_delta =  Há 3 horas
    # seção =   futebol italiano

# Na noticia 0, foram extraidas as informacoes solicitadas, mas é necessario extrair todas as outras informacoes. Cada extracao deve ser feita dentro de uma estrutura de repeticao. Para criar um DF com os dados, sera criada uma lista vazia e a cada iteracao appendar uma tupla com as informacoes extraidas. Com essa lista é possivel criar um DF, passando os dados e nomes das colunas.

dados = []

for noticia in lista_noticias:
    manchete = noticia.contents[1].text.replace('"', '')
    link = noticia.find('a')['href']

    descricao = noticia.contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class': 'bstn=related'})
        descricao = descricao.text if descricao else None

    metadados = noticia.find('div', attrs={'class': 'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None

    dados.append((manchete, link, descricao, time_delta, secao))

df = pd.DataFrame(dados, columns=['manchete', 'descricao', 'link', 'secao', 'hora_extracao', 'time_delta'])
df.head()

# Agora a solucao sera transformada em uma classe (toda vez que for preciso fazer a extracao, basta instanciar um objeto e executar o metodo de extracao):

from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

class ExtracaoPortal:
    def __init__(self):
        self.portal = None

    def extrair(self, portal):
        self.portal = portal
        texto_string = requests.get('https://globoesporte.globo.com/').text
        hora_extracao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        bsp_texto = BeautifulSoup(texto_string, 'html.parser')
        lista_noticias = bsp_texto.find_all('div', attrs={'class': 'feed-post-body'})

        dados = []

        for noticia in lista_noticias:
            manchete = noticia.contents[1].text.replace('"', '')
            link = noticia.find('a').get('href')

            descricao = noticia.contents[2].text
            if not descricao:
                descricao = noticia.find('div', attrs={'class': 'bstn=related'})
                descricao = descricao.text if descricao else None

            metadados = noticia.find('div', attrs={'class': 'feed-post-metadata'})
            time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
            secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

            time_delta = time_delta.text if time_delta else None
            secao = secao.text if secao else None

            dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

        df = pd.DataFrame(dados, columns=['manchete', 'descricao', 'link', 'secao', 'hora_extracao', 'time_delta'])
        return df
    
df = ExtracaoPortal().extrair('https://globoesporte.globo.com/')
df.head()


### SESSÃO 2
# MANIPULAÇÃO DE DADOS EM PANDAS

# MÉTODOS PARA MANIPULAÇÃO DE DADOS
# A lib pandas possui tambem metodos para transformacao dos dados e extracao de informacao.


# METODOS PARA LEITURA E ESCRITA DA LIB PANDAS
# A lib foi desenvolvida para trabalhar com dados estruturados (dispostos em linhas e colunas). Os dados podem estrar gravados em arquivos, paginas web, APIs, outros softwares, object stores (sistemas de armazenamento em cloud) ou em bancos de dados. A lib possui metodos capazes de fazer a leitura dos dados e carrega-los em um DF.

# Os metodos que fazem a leitura dos dados estruturados possuem o prefixo pd.read_XXX, onde pd é o apelido da lib pandas e XXX é o formato do arquivo. A lib possui metodos capazes de escrever o DF em um arquivo, um banco de dados ou copiar para a area de transferencia do sistema.


# A seguir serao descritos os metodos de leitura read_json, read_csv e a funcao read_sql (que contempla a funcao read_sql_query).
# (JSON) JavaScript Object Notation - Notacao de Objetos JavaScript, é uma formatacao leve de troca de dados e independente de linguagem de programacao. Os dados desse formato sao encontrados como uma colecao de pares chave/valor ou uma lista ordenada de valores. Uma chave pode conter outra estrutura interna (criando um arquivo com multiniveis).

# (CSV) Comma-separated valores - valores separados por virgula, é um formato de arquivo em que os dados sao separados por um delimitador, originalmente o delimitador é uma virgula, mas um arquivo CSV pode ser criado com qualquer delimitador (ex: ponto e virgula, pipe |, dentre outros). 


# LEITURA DE JSON E CSV COM PANDAS
# A leitura de um arquivo JSON é feita com o metodo: pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=True, convert_axes=True, convert_dates=True, keep_default_dates=True, numpy=False, precise_float=False, date_unit=None, encoding=None, lines=False, chunksize=None, compression='infer'). O unico parametro obrigatorio para carregar os dados é o 'path_or_buf', onde deve ser passado um caminho para o arquivo ou um "arquivo como objeto", que é um arquivo lido com a funcao open().

# A seguir sera usado o metodo 'read_json' para ler dados de uma API. Passando o caminho para o metodo, nesse caso a fonte de dados encontram-se a taxa selic de cada dia.
pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json').head()
    # 	data	    valor
    # 0	04/06/1986	0.065041
    # 1	05/06/1986	0.067397
    # 2	06/06/1986	0.066740
    # 3	09/06/1986	0.068247
    # 4	10/06/1986	0.067041    

# Para fazer o carregamento dos dados, é necessario incluir o caminho (diretorio), portanto o parametro 'filepath_or_buffer' é obrigatorio. Outro parametro importante para a leitura do arquivo é o 'sep' ou 'delimiter' (ambos fazem a mesma coisa). Sep por padrao possui o valor ',', entao caso nao seja especificado nenhum valor, o metodo fara a leitura dos dados considerando que estao separados por virgula. O parametro 'header' tem como valor padrao 'infer', que significa que o metodo realiza a inferencia para os nomes das colunas a partir da primeira linha de dados do arquivo.

# A seguir sera feita a leitura de uma fonte CSV, onde os campos sao separados por virgula (entao nao é preciso especificar um delimitador diferente).
pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv').head()
    # 	Rank	City	State	Population	Change
    # 0	 1	New York	NY	    8405837	     +0.73%
    # 1	 2	Los Angeles	CA	    3884307	     +0.03%
    # 2	 3	Chicago	    IL	    2718782	     -0.30%
    # 3	 4	Houston	    TX	    2195914	     +0.59%


# MANIPULACAO DE DADOS COM PANDAS
# Alem dos metodos para carregar e salvar os dados, a lib pandas possui metodos para transformar os dados e a extracao de informacao para areas de negocios.

# O trabalho com dados consiste em capturar os dados em suas origens, fazer as transformacoes dos dados para padroniza-los e aplicar tecnicas estatisticas classicas (ou algoritmos de machine/deep learning).
# Nesse trabalho é comum fazer a divisao em duas etapas:
# 1. capturar e fazer a transformacao/padronizacao dos dados.
# 2. extracao de informacoes.


# ETAPA DE CAPTURA E TRANSFORMACAO/PADRONIZACAO DOS DADOS
# A extracao de dados pode ser feita por meio do metodo read_json() e guardada em um DF pandas. Ao carregar dados em um DF, é possivel visualizar quantas linhas/colunas e os tipos de dados em cada coluna com o metodo info().

# No exemplo a seguir, o metodo retorna que o DF possui 8552 registros (entradas) e 2 colunas, os indices sao numericos e variam de 0 a 8551 (n-1). Outras informacoes relevantes que esse metodo retorna é sobre a quantidade de celulas sem valor (non-null) e o tipo dos dados nas colunas. Como ambas colunas possuem os mesmos valores nao nulos (8552), nao existem valores faltantes. O tipo dos dados é object, que significa que os dados sao do tipo string ou existe uma mistura de tipos, onde valor é um float.

df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
print(df_selic.info())
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 8552 entries, 0 to 8551
    # Data columns (total 2 columns):
    # data     8552 non-null object
    # valor    8552 non-null float64
    # dtypes: float64(1), object(1)
    # memory usage: 133.6+ KB
    # None


# REMOVENDO LINHAS DUPLICADAS
# Um dos primeiros tratamentos que devemos fazer para carregar em uma base de dados é a remocao dos dados duplicados. Ex: queremos manter o registro da compra atual ou queremos manter a primeira compra. Um DF da lib pandas possui o metodo meu_df.drop_duplicates() que permite fazer essa remocao de dados duplicados.

# No codigo a seguir, é usado o metodo para remover as linhas duplicadas e solicitando que mantenha o ultimo registo (keep='last'). Atraves do parametro inplace=True, a transformacao é feita e salva no mesmo DF (sobrescrevendo o objeto na memoria). Caso inplace nao seja passado, a transformacao é aplicada mas nao é salva (o DF continua da mesma forma anterior a transformacao). O metodo 'subset' permite que a remocao dos dados duplicados sejam feitas com base em uma ou mais colunas.

df_selic.drop_duplicates(keep='last', inplace=True)


# CRIACAO DE NOVAS COLUNAS
# Outra transformacao é a criacao de novas colunas, a sintaxe é similar a criacao de uma nova chave em um dict: meu_df['nova_coluna'] = dado. Sera criada uma coluna que adiciona a data de extracao das informacoes.

# No modulo datetime, esta sendo usada a classe date e o metodo today(), onde é guardada a data em uma nova coluna (a lib pandas entende que esse valor deve ser colocado em todas as linhas). Apos isso sera criada uma nova coluna com o nome do responsavel pela extracao (basta atribuir a string a uma nova coluna).
# Ha um problema com o tipo de dados das datas, apesar de cada valor ser do tipo date, vendo pelo metodo info() o tipo de dados é object. Para corrigir isso, sera usado o metodo astype() para converter o tipo de dados da coluna para datetime.

from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = 'Autora'

print(df_selic.info())
df_selic.head()
    # <class 'pandas.core.frame.DataFrame'>
    # Int64Index: 8552 entries, 0 to 8551
    # Data columns (total 4 columns):
    # data             8552 non-null object
    # valor            8552 non-null float64
    # data_extracao    8552 non-null object
    # responsavel      8552 non-null object
    # dtypes: float64(1), object(3)
    # memory usage: 333.5+ KB
    # None
    # 	data	     valor	   data_extracao	 responsavel
    # 0	04/06/1986	0.065041	2020-07-19	     Autora
    # 1	05/06/1986	0.067397	2020-07-19	     Autora
    # 2	06/06/1986	0.066740	2020-07-19	     Autora
    # 3	09/06/1986	0.068247	2020-07-19	     Autora
    # 4	10/06/1986	0.067041	2020-07-19	     Autora


# METODO TO_DATETIME() E ASTYPE()
# O tipo data tras vantagens como: ordenar da data mais recente para a mais antiga e verificar a variacao da taxa selic em um determinado periodo. Serao usados os metodos pandas.to_datetime() e minha_series.astype() para fazer a conversao e transformacao das colunas data e data_extracao. No codico a seguir, é realizada a transformacao e guardada dentro da propria coluna (sobrescrevendo os valores). A notacao pd.to_datetime() é um metodo da lib, nao do DF.

# Primeiramente, o metodo recebe a coluna com os valores a serem alterados (df_selic['data']) e apos isso o segundo parametro, indicando que no formato atual (antes da conversao) o dia está em primeiro (dayfirst=True). Em seguida como a coluna data_extracao foi criada com o metodo today(), o formato ja esta correto para a conversao. Nessa conversao é usado o metodo astype(), transformando os dados de uma coluna (que é uma Series) em um determinado tipo (nesse caso o tipo datetime é passado).

# Com o astype() é possivel padronizar valores das colunas, ex: transformar todos em float, int ou outro tipo. A seguir, usando o metodo info(), ambas as colunas sao transformadas no tipo datetime. O formato resultante ano-mes-dia é um padrao do datetime64[ns] que segue o padrao internacional, no qual o ano vem primeiro, seguido pelo mes e por ultimo o dia. É possivel usar o strftime() para transformar o traco em barra (/), porem o resultado seriam strings, e nao datas.

df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

print(df_selic.info())
df_selic.head()
    # <class 'pandas.core.frame.DataFrame'>
    # Int64Index: 8552 entries, 0 to 8551
    # Data columns (total 4 columns):
    # data             8552 non-null datetime64[ns]
    # valor            8552 non-null float64
    # data_extracao    8552 non-null datetime64[ns]
    # responsavel      8552 non-null object
    # dtypes: datetime64[ns](2), float64(1), object(1)
    # memory usage: 333.5+ KB
    # None
    # 	data	     valor	   data_extracao	 responsavel
    # 0	1986-06-04	0.065041	2020-07-19	     Autora
    # 1	1986-06-05	0.067397	2020-07-19	     Autora
    # 2	1986-06-06	0.066740	2020-07-19	     Autora
    # 3	1986-06-09	0.068247	2020-07-19	     Autora
    # 4	1986-06-10	0.067041	2020-07-19	     Autora


# SERIES.STR
# Muitas vezes é necessario padronizar os valores em colunas, ex: queremos ter certeza que a coluna "responsavel" possui todas as palavras em letras maiusculas. Ao selecionar uma coluna no DF, sabemos que o resultado é uma Series e que esse objeto tem um recurso "str" que permite aplicar as funcoes de string para todos os valores da Series.

# No codigo a seguir, é selecionada a coluna 'responsavel', usado recurso str e aplicado o metodo upper(). Dessa forma, a lib pandas entende que queremos converter todos os valores dessa coluna para letras maiusculas. Ao atribuir o resultado à propria coluna, o valor antigo é substituido.

df_selic['responsavel'] = df_selic['responsavel'].str.upper()
df_selic.head()
    # 	data	     valor	   data_extracao	 responsavel
    # 0	1986-06-04	0.065041	2020-07-19	     AUTORA
    # 1	1986-06-05	0.067397	2020-07-19	     AUTORA
    # 2	1986-06-06	0.066740	2020-07-19	     AUTORA
    # 3	1986-06-09	0.068247	2020-07-19	     AUTORA
    # 4	1986-06-10	0.067041	2020-07-19	     AUTORA


# METODO SORT_VALUES()
# No codigo a seguir, sera usado o metodo sort_values() que permite ordenar o DF de acordo os valores de uma coluna. Esse metodo é do DF, por isso a notacao é meu_df.metodo(). Serao usados 3 parametros do metodo sort_values, o primeiro informando qual coluna deve ser usada para ordenar, o segundo, para que seja feita em ordem decrescente e o terceiro (inplace=True) para que a modificacao seja feita no proprio objeto (sobrescrevendo o DF).

df_selic.sort_values(by='data', ascending=False, inplace=True)
df_selic.head()
    # 	    data	     valor	   data_extracao	 responsavel
    # 8551	2020-07-17	2.250000	2020-07-19	     AUTORA
    # 8550	2020-07-16	2.250000	2020-07-19	     AUTORA
    # 8549	2020-07-15	2.250000	2020-07-19	     AUTORA
    # 8548	2020-07-14	2.250000	2020-07-19	     AUTORA
    # 8547	2020-07-13	2.250000	2020-07-19	     AUTORA


# METODO RESET_INDEX() E SET_INDEX()
# Ao fazer a ordenacao dos dados com o metodo anterior, os indices dos cinco primeiros registros é 8551, 8550...85XX. Nenhuma transformacao afetou o indice (anteriormente nao foram especificados rotulos para as linhas, entao ele usa um intervalo numerico). Porem o intervalo numerico é diferente das posicoes de um vetor, pois é um nome e vai acompanhar a linha independente da transformacao.
# As unicas formas de alterar o indice sao com os metodos reset_index() e set_index(). O primeiro redefine o indice usando o padrao e o segundo define novos indices. No codigo a seguir, é usado o metodo reset_index() para redefinir os indices padores (sequencia numerica). O primeiro parametro (drop=True), significa que nao queremos usar o indice que sera substituido em uma nova coluna, e o inplace informa para gravar as alteracoes no proprio objeto.

df_selic.reset_index(drop=True, inplace=True)
df_selic.head()
    # 	data	     valor	   data_extracao	 responsavel
    # 0	2020-07-17	2.250000	2020-07-19	     AUTORA
    # 1	2020-07-16	2.250000	2020-07-19	     AUTORA
    # 2	2020-07-15	2.250000	2020-07-19	     AUTORA
    # 3	2020-07-14	2.250000	2020-07-19	     AUTORA
    # 4	2020-07-13	2.250000	2020-07-19	     AUTORA

# Durante a transformacao dos dados, pode ser necessario definir novos valores para os indices (ao inves de usar o range numerico). Essa transformacao pode ser feita usando o metodo 'meu_df.set_index()'. Esse metodo permite especificar os novos valores usando um coluna ja existente, ou passando uma lista de tamanho igual a quantidade de linhas.

# Nos exemplos a seguir, no primeiro codigo sera criada uma lista que usa os indices do DF, adicionando um prefixo para cada valor. Apos isso sao impressos os cinco primeiros itens da nova lista. No segundo codigo, sera definido o novo indice com base na lista criada. O parametro keys() recebe como parametro uma lista de listas, e o segundo parametro especifica que a modificacao deve ser salva no objeto. Entao sera impresso os cinco primeiros itens do DF.

lista_novo_indice = [f'selice_{indice}' for indice in df_selic.index]
print(lista_novo_indice[:5])
    # ['selice_0', 'selice_1', 'selice_2', 'selice_3', 'selice_4']

df_selic.set_index(keys=[lista_novo_indice], inplace=True)
df_selic.head()
    # 	        data	     valor	   data_extracao	 responsavel
    # selic_0	2020-07-17	2.250000	2020-07-19	     AUTORA
    # selic_1	2020-07-16	2.250000	2020-07-19	     AUTORA
    # selic_2	2020-07-15	2.250000	2020-07-19	     AUTORA
    # selic_3	2020-07-14	2.250000	2020-07-19	     AUTORA
    # selic_4	2020-07-13	2.250000	2020-07-19	     AUTORA

# Especificando um indice com valor conceitual, é possivel usar as funcoes idxmax() e idxmin() para descobrir qual o indice de maior e menor valor de uma Series.

print(df_selic['valor'].idxmax())
print(df_selic['valor'].idxmin())
    # selic_8551
    # selic_0


# EXTRACAO DE INFORMACOES
# FILTROS COM LOC

# Um dos recursos mais usados por equipes de analise de dados é a aplicacao de filtros. Por exemplo: em uma determinada pesquisa, querem saber qual a media de idade de todas as pessoas de uma sala de aula, bem como a media de idades somente das mulheres e somente dos homens. Essa distincao por genero é um filtro. Com esse filtro é possivel comparar a idade de todos, com a idade de cada grupo e entender se mulheres ou homens estao a baixo ou acima da media geral.

# Os DF da lib pandas possuem uma propriedade chamada 'loc'. Ela permite acessar um conjunto de linhas (filtrar linhas), por meio do indice ou por um vetor booleano (True ou False).
# A seguir sera testado o filtro pelo indice, localizando (loc) o registro de indice 'selic_0' (como resultado obtemos uma Series). No codigo seguinte, serao filtrados 3 registros, para isso foi necessario passar uma lista contendo os indices (como resultado, obtemos um novo DF). Entao foi feito um fatiamento (slice) procurando um intervalo de indices [:'selic_5'].

df_selic.loc['selic_0']
    # data	            2020-07-17
    # valor	            2.250000
    # data_extracao	    2020-07-19
    # responsavel	    AUTORA
    # Name: selic_0, dtype: object

df_selic.loc[['selic_0', 'selic_4', 'selic_2000']]
    # 	         data	       valor	    data_extracao	 responsavel
    # selic_0	 2020-07-17	   2.250000	    2020-07-19	     AUTORA
    # selic_4	 2020-07-13	   2.250000	    2020-07-19	     AUTORA
    # selic_2000 2020-03-19	   4.250000	    2020-07-19	     AUTORA

df_selic.loc[:'selic_5']
    # 	         data	       valor	    data_extracao	 responsavel
    # selic_0	 2020-07-17	   2.250000	    2020-07-19	     AUTORA
    # selic_1	 2020-07-16	   2.250000	    2020-07-19	     AUTORA
    # selic_2	 2020-07-15	   2.250000	    2020-07-19	     AUTORA
    # selic_3	 2020-07-14	   2.250000	    2020-07-19	     AUTORA
    # selic_4	 2020-07-13	   2.250000	    2020-07-19	     AUTORA
    # selic_5	 2020-07-10	   2.250000	    2020-07-19	     AUTORA

# LOC aceita um segundo argumento, que é a coluna (ou colunas) que serao exibidas para os indices escolhidos. No codigo a seguir, sera selecionada uma unica coluna e no proximo codigo uma lista de colunas.

# O mesmo resultado poderia ser alcançado passando a coluna, ou a lista de colunas conforme as sintaxes:
# df_selic.loc[['selic_0', 'selic_4', 'selic_200']]['valor'].
# df_selic.loc[['selic_0', 'selic_4', 'selic_200']][['valor', 'data_extracao']].

df_selic.loc[['selic_0', 'selic_4', 'selic_2000'], 'valor']
    # selic_0       2.250000
    # selic_4       2.250000
    # selic_2000    4.250000
    # Name: valor, dtype: float64

df_selic.loc[['selic_0', 'selic_4', 'selic_2000'], ['valor', 'data_extracao']]
    # 	         valor	    data_extracao
    # selic_0	 2.250000	    2020-07-19
    # selic_4	 2.250000	    2020-07-19
    # selic_2000 4.250000	    2020-07-19

# Existe tambem a propriedade 'iloc'. Ela filtra as linhas considerando a posicao que ocupam no objeto. No codigo a seguir, sera usado o iloc para filtrar os 5 primeiros registros, usando a mesma notacao do fatiamento de listas. Essa prorpiedade nao possui opcao de selecionar colunas.

df_selic.iloc[:5]
    # 	         data	       valor	    data_extracao	 responsavel
    # selic_0	 2020-07-17	   2.250000	    2020-07-19	     AUTORA
    # selic_1	 2020-07-16	   2.250000	    2020-07-19	     AUTORA
    # selic_2	 2020-07-15	   2.250000	    2020-07-19	     AUTORA
    # selic_3	 2020-07-14	   2.250000	    2020-07-19	     AUTORA
    # selic_4	 2020-07-13	   2.250000	    2020-07-19	     AUTORA


# FILTROS COM TESTES BOOLEANOS
# É possivel usar operadores relacionais e logicos para fazer testes condicionais com os valores das colunas de um DF. Criando internamente um teste condicional, a lib testa todas as linhas do DF ou da Series, retornando uma Series booleana, ou seja, composta por valores True ou False.

# No codigo a seguir, sera usado um operador relacional para testar se os valores da coluna 'valor' sao menores que < 0.01. O resultado sera armazenado em uma variavel chamada 'teste', o tipo de dado da variavel (teste) é uma Series. Na linha teste[:5] sera impressa os 5 primeiros resultados do teste logico.

teste = df_selic['valor'] < 0.01

print(type(teste))
teste[:5]
    # <class 'pandas.core.series.Series'>
    # selic_0     False
    # selic_1     False
    # selic_2     False
    # selic_3     False
    # selic_4     False
    # Name: valor, dtype: bool

# No codigo a seguir, é realizado mais um teste logico para ver se a data da taxa é do ano de 2020. Sera usado o metodo 'to_datetime()' para converter a string para a data e fazer a comparacao.

teste2 = df_selic['data'] >= pd.to_datetime('2020-01-01')

print(type(teste2))
teste2[:5]
    # <class 'pandas.core.series.Series'>
    # selic_0     True
    # selic_1     True
    # selic_2     True
    # selic_3     True
    # selic_4     True
    # Name: data, dtype: bool

# O teste condicional pode ser feito usando operadores logicos. Para a operacao logica AND em pandas, é usado o caractere '&', e para a operacao logica OR em pandas, é usado o caractere '|'. Cada teste deve estar entre parenteses. No codigo a seguir, serao feitos testes usando a operacao logica AND e OR.

teste3 = (df_selic['valor'] < 0.01) & (df_selic['data'] >= pd.to_datetime('2020-01-01'))
teste4 = (df_selic['valor'] < 0.01) | (df_selic['data'] >= pd.to_datetime('2020-01-01'))

print('Resultado do AND:\n')
print(teste3[:3])

print('\nResultado do OR:\n')
print(teste4[:3])
    # Resultado do AND:
    # selic_0     True
    # selic_1     True
    # selic_2     True
    # Name: valor, dtype: bool

    # Resultado do OR:
    # selic_0     True
    # selic_1     True
    # selic_2     True
    # Name: valor, dtype: bool

# Com a criacao das condicoes, basta aplicar no DF para criar o filtro. A construcao é feita passando a condicao para a propriedade loc. No codigo a seguir, primeiro sera criada a condicao do filtro (Series booleana), e depois sera passado como parametro para filtrar os registros. O filtro retornou 4 registros.

filtro1 = df_selic['valor'] < 0.01
df_selic.loc[filtro1]
    #     	        data	      valor	   data_extracao	responsavel
    # selic_0	    2020-07-17	0.008442	2020-07-19	     AUTORA
    # selic_1	    2020-07-16	0.008442	2020-07-19	     AUTORA
    # .......       .......     .......    .......          .......
    # selic_21	    2020-06-18	0.008442	2020-07-19	     AUTORA
    # selic_7606	1990-03-16	0.000000	2020-07-19	     AUTORA
    # selic_7607	1990-03-15	0.000000	2020-07-19	     AUTORA
    # selic_7608	1990-03-14	0.000000	2020-07-19	     AUTORA

# Primeiro foi criada a condicao, depois guardado na variavel e depois aplicado. Porem, poderia ter passado a condicao direta: df_selic.loc[df_selic['valor'] < 0.01].

# No codigo a seguir, primeiro sera criada uma condicao para exibir o registro das datas apenas do mes de janeiro de 2020. Primeiro criando 2 variaveis para armazenar as datas, depois criando o filtro e entao aplicando no DF, e guardando o resultado (DF) em um novo DF.
# O filtro poderia ser escrito como: df_selic.loc[(df_selic['data'] >= pd.to_datetime('2020-01-01')) & (df_selic['data'] <= pd.to_datetime('2020-01-31'))], mas seria muito grande e dificil de ler.

data1 = pd.to_datetime('2020-01-01')
data2 = pd.to_datetime('2020-01-31')

filtro_janeiro_2020 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

df_janeiro_2020 = df_selic.loc[filtro_janeiro_2020]
df_janeiro_2020.head()
    # 	         data	    valor	    data_extracao	responsavel
    # selic_114	2020-01-31	0.017089	2020-07-19	    AUTORA
    # selic_115	2020-01-30	0.017089	2020-07-19	    AUTORA
    # selic_116	2020-01-29	0.017089	2020-07-19	    AUTORA
    # selic_117	2020-01-28	0.017089	2020-07-19	    AUTORA
    # selic_118	2020-01-27	0.017089	2020-07-19	    AUTORA

# Agora sera criado mais um filtro e um novo DF. No codigo a seguir, o novo DF contem as informacoes do mes de janeiro do ano de 2019.

data1 = pd.to_datetime('2019-01-01')
data2 = pd.to_datetime('2019-01-31')

filtro_janeiro2019 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)

df_janeiro2019 = df_selic.loc[filtro_janeiro2019]
df_janeiro2019.head()
    #     	       data	    valor	data_extracao	responsavel
    # selic_367	2019-01-31	0.02462	2020-07-19	    AUTORA
    # selic_368	2019-01-30	0.02462	2020-07-19	    AUTORA
    # selic_369	2019-01-29	0.02462	2020-07-19	    AUTORA
    # selic_370	2019-01-28	0.02462	2020-07-19	    AUTORA
    # selic_371	2019-01-25	0.02462	2020-07-19	    AUTORA

# Agora com 3 DFs, um completo e dois com filtros, serao usado metodos de estratistica descritiva para extrair informacoes sobre o valor da taxa selic em cada DF. O objetivo é saber qual o valor maximo e minimo registrado em cada caso e qual sua media.

# Selecionando uma coluna, obtemos uma Series, entao sera usado o metodo solicitado:

print('Minimo geral = ', df_selic['valor'].min())
print('Minimo janeiro de 2019 = ', df_janeiro2019['valor'].min())
print('Minimo janeiro de 2020 = ', df_janeiro_2020['valor'].min())

print('Maximo geral = ', df_selic['valor'].max())
print('Maximo janeiro de 2019 = ', df_janeiro2019['valor'].max())
print('Maximo janeiro de 2020 = ', df_janeiro_2020['valor'].max())

print('Media geral = ', df_selic['valor'].mean())
print('Media janeiro de 2019 = ', df_janeiro2019['valor'].mean())
print('Media janeiro de 2020 = ', df_janeiro_2020['valor'].mean())
    # Minimo geral =  0.0
    # Minimo janeiro de 2019 =  0.02462
    # Minimo janeiro de 2020 =  0.017089
    # Maximo geral =  0.0585
    # Maximo janeiro de 2019 =  0.02462
    # Maximo janeiro de 2020 =  0.017089
    # Media geral =  0.019999999999999997
    # Media janeiro de 2019 =  0.02462
    # Media janeiro de 2020 =  0.017089

# Os filtros permitem começar a tirar respostas para áreas de negócios. No ano de 2019 tanto a mínima quanto a máxima foram superiores que no ano de 2020. A máxima geral é bem superior a máxima desses meses, assim como a média geral, que é bem superior, ou seja, nesses meses a taxa média foi inferior a média geral, sendo que em janeiro de 2020 foi ainda pior.


# Essas transformacoes podem ser gravadas fisicamente em um arquivo (ex: .csv). No codigo a seguir, sera salvo um arquivo 'dados_selic.csv' na pasta de trabalho, com os parametros padroes: separado por virgula, com cabecalho, com os indices, dentre outros.

df_selic.to_csv('dados_selic.csv')

# Poderíamos extrair diversas outras informações dos dados. Todo esse trabalho faz parte do cotidiano nos engenheiros, cientistas e analistas de dados. Os engenheiros de dados mais focados na preparação e disponibilização dos dados, os cientistas focados em responder questões de negócio, inclusive utilizando modelos de machine learning e deep learning e os analistas, também respondendo a perguntas de negócios e apresentando resultados. 


# BANCOS DE DADOS COM PANDAS
# Pandas possui 2 metodos que permitem executar instrucoes SQL em banco de dados:

# 1. pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
# 2. pandas.read_sql_query(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)

# O unico parametro obrigatorio em ambos os metodos é a instrucao SQL e uma conexao com o banco de dados (con). A conexao deve ser feita usando outra lib, a sqlalchemy. Seguindo a srecomendacoes da PEP 249 todas as lib precisam fornecer um metodo "conect" onde recebe a string de conexao. Sendo que a sintaxe da string de conexao depende da lib e do banco de dados.

# No codigo a seguir, serao feitos 2 exemplos, um usando a conexao com um banco postgresql e outro com um banco mysql. A unica diferenca entre eles é a importacao da lib especifica e a string de conexao. Assim, ao estabelecer conexao com o banco de dados e armazenar a instancia em uma variavel, basta passa-la como parametro para o metodo da lib pandas.

import psycopg2

host = 'XXXXX'
port = 'XXXXX'
database = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'

conn_str = fr'dbname={database} user={username} password={password} host={host} port={port}'
conn = psycopg2.connect(conn_str)

query = 'SELECT * FROM XXX.YYYY'
df = pd.read_sql(query, conn)

import mysql.connector

host = 'XXXXX'
port = 'XXXXX'
database = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'

conn_str = fr'host={host} port={port} database={database} user={username} password={password}'
conn = mysql.connector.connect(host='localhost', user='root', password='', database='db')

query = 'SELECT * FROM XXX.YYYY'
df = pd.read_sql(query, conn)