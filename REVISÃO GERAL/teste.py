import requests
import datetime as dt

jogos = requests.get('http://worldcup.sfg.io/matches').json()
print(type(jogos))
    # <class 'list'>

# jogos = requests.get('').json() = os dados foram extraidos com o requests e o conteudo foi convertido para json(), gerando uma lista de dicionarios. Serao extraidas informacoes do primeiro dict da lista (primeiro jogo).
# Porem como solicitado, devem ser extraidas informacoes de cada jogo e gerar um relatorio:

# percorrendo o dicionario da lista (cada jogo) extraindo as informacoes
info_relatorio = []
file = open('relatorio_jogos.txt', "w") # criado arquivo txt na pasta em que esta trabalhando.

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

file.close() # necessario fechar o arquivo
info_relatorio[:5]
    # ['(07/06/2019) - France x Korea Republic = 4 a 0',
    #  '(08/06/2019) - Germany x China PR = 1 a 0',
    #  '(08/06/2019) - Spain x South Africa = 3 a 1',
    #  '(08/06/2019) - Norway x Nigeria = 3 a 0',
    #  '(09/06/2019) - Brazil x Jamaica = 3 a 0']

# for jogo in jogos: = percorrer cada item do dict extraindo as informacoes.
# gols_time1 = jogo['home_team']['goals'] = usadas 2 chaves nas 2 variaveis porque, dentro do dict, existe outro dict.
    # 'home_team': {'country': 'France', 'code': 'FRA', 'goals': 4, 'penalties': 0}.
# Para acessar os gols, é necessario acessar a chave inteira 'goals' (outro dict): ['team']['goals']

# file = open('relatorio_jogos.txt', "w") = funcao built-in para criar um arquivo onde serao ESCRITAS as informacoes (por isso o parametro 'w').
# file.write(linha + '\n') = escrever em cada linha gerada no arquivo, concatenando com uma nova linha '\n' a cada nova informacao.


# MATPLOTLIB
# Biblioteca com funcionalidades de criacao de graficos. Sera criado um grafico simples usando a interface Pyplot baseado nas informacoes salvas sobre os jogos da Copa do Mundo de Futebol Feminino (2019).

# A extracao do relatorio foi armazenada no arquivo 'relatorio_jogos.txt'. Agora os dados que persistiram no arquivo serao lidos, extraindo somente as datas no formato 'dd/mm' e contabilizar quantos jogos ocorreram em cada data. Em seguida sera usado o 'Pyplot' na construcao do grafico de contagem.

# ler arquivo
file = open('relatorio_jogos.txt', 'r')
print('file = ', file, "/n")
info_relatorio = file.readlines()
file.close()
    # file = <_io.TextIOWrapper name='relatorio_jogos.txt' mode='r' encoding='cp1252'>
print("linha 1 =", info_relatorio[0])
    # linha 1 =  (07/06/2019) - France x Korea Republic = 4 a 0

# file = open() = ler o arquivo, passando como parametros o nome do arquivo e a opcao 'r' (abrir em modo leitura (r = read)).
# file.readlines() = acessar o conteudo do arquivo, que cria uma lista, onde cada elemento é uma linha do arquivo.
# file.close() = fechar o arquivo apos a criacao da lista.
# Apos isso foi impresso o primeiro item da lista criada (primeira linha do arquivo que foi feita a leitura). Para cada linha, buscamos somente a parte correspondente ao dia e mes (dd/mm), devendo criar uma nova lista contendo somente essas datas:

# extraindo somente a parte 'dd/mm' da linha
datas = [linha[1:6] for linha in info_relatorio]
print(sorted(datas))
    # ['02/07', '03/07', '06/07', '07/06', '07/07', '08/06', '08/06', '08/06', '09/06', '09/06', '09/06', '10/06', '10/06', '11/06', '11/06', '11/06', '12/06', '12/06', '12/06', '13/06', '13/06', '14/06', '14/06', '14/06', '15/06', '15/06', '16/06', '16/06', '17/06', '17/06', '17/06', '17/06', '18/06', '18/06', '19/06', '19/06', '20/06', '20/06', '20/06', '20/06', '22/06', '22/06', '23/06', '23/06', '24/06', '24/06', '25/06', '25/06', '27/06', '28/06', '29/06', '29/06']

# Tendo uma lista com todas as datas dos jogos, é necessario contar quantas vezes cada data aparece (tendo assim a quantidade de jogos por dia). Sera usado a operacao 'count()' para objetos tipo sequencia: sequencia.count(valor), retornando quantas vezes o valor aparece na sequencia.
# datas.count('08/06'): resultado 3 # fazendo isso em todas as datas, sera necessario usar uma 'list comprehension' para a iteracao. Cada data sera gerada uma tupla com 2 valores: (data, count). Na lista final, tera uma linha para cada data: ('08/06', 3). Para remover as duplicacoes, sera usado o contrutor 'set()'.

datas_count = [(data, datas.count(data)) for data in set(datas)]
print(datas_count)
    # [('17/06', 4), ('22/06', 2), ('24/06', 2), ('08/06', 3), ('07/06', 1), ('18/06', 2), ('03/07', 1), ('07/07', 1), ('27/06', 1), ('28/06', 1), ('25/06', 2), ('09/06', 3), ('20/06', 4), ('13/06', 2), ('12/06', 3), ('19/06', 2), ('11/06', 3), ('14/06', 3), ('16/06', 2), ('10/06', 2), ('29/06', 2), ('02/07', 1), ('23/06', 2), ('15/06', 2), ('06/07', 1)]

# Por conveniencia a lista de tuplas gerada sera transformada em um dicionario com o construtor 'dict()':
datas_count = dict(datas_count)
print(datas_count)
    # {'17/06': 4, '22/06': 2, '24/06': 2, '08/06': 3, '07/06': 1, '18/06': 2, '03/07': 1, '07/07': 1, '27/06': 1, '28/06': 1, '25/06': 2, '09/06': 3, '20/06': 4, '13/06': 2, '12/06': 3, '19/06': 2, '11/06': 3, '14/06': 3, '16/06': 2, '10/06': 2, '29/06': 2, '02/07': 1, '23/06': 2, '15/06': 2, '06/07': 1}

# A transformacao da lista para dict, permite extrair as chaves (que sao datas) e os valores (quantidades). Os dois itens serao usados nos eixos 'x' e 'y' do grafico.

# Com os dados em maos, o grafico sera feito usando a interface Pyoplot da biblioteca 'matplotlib':
import matplotlib.pyplot as plt

eixo_x = datas_count.keys()
eixo_y = datas_count.values()

plt.figure(figsize=(15, 5))
plt.xlabel('Dia do mês')
plt.ylabel('Quantidade de jogos')
plt.xticks(rotation=45)

plt.bar(eixo_x, eixo_y)

plt.show()