# APLICAÇÃO DE BANCO DE DADOS

# As opções de armazenamento de dados utilizadas pelos softwares, podem ser em arquivos CSV, JSON, XML ou em um sistema de banco de dados. O sistema de banco de dados pode ser dividido em duas categorias: banco de dados relacional e banco de dados NoSQL.
# A abordagem relacional é baseada na teoria dos conjuntos e persiste os dados em tabelas, enquanto o NoSQL é projetado para lidar com a velocidade e a escala de aplicações em grande escala e em outros formatos não estruturados. O NoSQL geralmente não segue os princípios do sistema de gerenciamento de banco de dados relacional e é projetado especificamente para lidar com a grande quantidade de dados que trafegam na rede e são processados.


# LINGUAGEM DE CONSULTA ESTRUTURADA - SQL

# A linguagem SQL, é usada para se comunicar com bancos de dados relacionais. A sigla significa structured query language, ou linguagem de consulta estruturada, e foi padronizada pelo ANSI em 1986. Embora cada fornecedor tenha sua própria interpretação do SQL, existe uma linguagem base padrão que é comum a todos. Algumas empresas de software para banco de dados adicionaram extensões e modificações à linguagem padrão.


# As instruções da linguagem SQL são divididas em três grupos: DDL, DML, DCL

# DDL é um acrônimo para Data Definition Language (linguagem de definição de dados). Fazem parte deste grupo as instruções destinadas a criar, deletar e modificar banco de dados e tabelas. Neste módulo vão aparecer comandos como CREATE, o ALTER e o DROP.

# DML é um acrônimo para Data Manipulation Language (linguagem de manipulação de dados). Fazem parte deste grupo as instruções destinadas a recuperar, atualizar, adicionar ou excluir dados em um banco de dados. Neste módulo vão aparecer comandos como INSERT, UPDATE e DELETE.

# DCL é um acrônimo para Data Control Language (linguagem de controle de dados). Fazem parte deste grupo as instruções destinadas a manter a segurança adequada para o banco de dados. Neste módulo vão aparecer comandos como GRANT e REVOKE.


# BANCO DE DADOS RELACIONAL:

# CONEXÃO COM BANCO DE DADOS RELACIONAL

# A necessidade de estabelecer uma conexão entre uma aplicação em uma linguagem de programação e um sistema gerenciador de banco de dados relacional (RDBMS) para poder enviar comandos SQL e efetuar ações no banco de dados. Para isso, podem ser utilizadas tecnologias como ODBC e JDBC para permitir a comunicação entre a linguagem de programação e o banco de dados.

# A vantagem de utilizar as tecnologias ODBC e JDBC na comunicação entre uma aplicação e um sistema gerenciador de banco de dados relacional (RDBMS) esta no fato de que uma aplicacao pode acesar diferentes RDBMS sem precisar recompilar o codigo. A transparência entre diferentes RDBMS é possível devido ao uso de um driver, que é responsável por traduzir as chamadas ODBC e JDBC para a linguagem do RDBMS. O JDBC é uma API padrão em Java que abstrai a conexão com um RDBMS, enquanto o ODBC é uma API padronizada para conexão com os diversos RDBMS. Cada fornecedor de RDBMS constrói e distribui um driver JDBC gratuito, e para usar a API ODBC, é necessário configurar uma entrada nas propriedades do sistema.


# CONEXÃO DE BANCO DADOS SQL EM PYTHON

# A utilização de bibliotecas em Python para se comunicar com RDBMS: cada biblioteca é específica para o driver de um determinado fornecedor, permitindo a conexão e execução de comandos SQL no banco. Para padronizar os módulos de conexão e envio de comandos, existe o PEP 249, que estabelece regras que os fornecedores devem seguir na construção dos módulos. Isso permite que, caso seja necessário alterar o banco de dados, apenas os parâmetros precisam ser modificados, sem necessidade de alterar o código.


# BANCO DE DADOS SQLITE

# O SQLite é uma tecnologia de banco de dados que pode ser incorporada em dispositivos móveis e aplicativos, não requer um processo de servidor separado e armazena dados em um único arquivo de disco. É possível usar o módulo built-in sqlite3 do interpretador Python para trabalhar com o SQLite.

# CRIANDO UM BANCO DE DADOS

# Para utilizar o módulo sqlite3 em Python, é necessário importá-lo e usar o método connect() para se conectar a um banco de dados. Como o SQLite não utiliza um processo de servidor separado, o arquivo do banco de dados é criado na pasta do projeto assim que a conexão é estabelecida. Caso queira criar o arquivo em outra pasta, basta especificar o caminho junto com o nome do arquivo. C:/Users/Documents/meu_projeto/meus_bancos/bancoDB.db.

import sqlite3

conn = sqlite3.connect('aulaBD.bd')
print(type(conn))
    # <class 'sqlite3.Connection'>

# Ao executar o código da entrada 1, o arquivo é criado, e a variável "conn" agora é um objeto da classe Connection pertencente ao módulo sqlite3.


# CRIANDO UMA TABELA

# Agora que temos uma conexão com um banco de dados, vamos utilizar uma instrução DDL da linguagem SQL para criar a tabela fornecedor. O comando SQL que cria a tabela fornecedor está no código a seguir e foi guardado em uma variável chamada ddl_create.

# Observação: se tentar criar uma tabela que já existe, um erro é retornado. Caso execute todas as células novamente, certifique-se de apagar a tabela no banco, para evitar o erro.

ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAr(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
"""

# O comando DDL implementado faz parte do conjunto de instruções SQL, razão pela qual deve seguir a sintaxe que essa linguagem determina.

# N padrão na instrução, começa com o comando CREATE TABLE, seguido do nome da tabela a ser criada e, entre parênteses, o nome do campo, o tipo e a especificação de quando não são aceitos valores nulos.
# O primeiro campo possui uma instrução adicional, que é o autoincremento, ou seja, para cada novo registro inserido, o valor desse campo aumentará um.

# Tendo a conexao e a DDL, basta utilizar um mecanismo para que esse comando seja executado no banco. Esse mecanismo, segundo o PEP 249, deve estar implementado em um método chamado execute() de um objeto cursor.
# Os cursores desempenham o papel de pontes entre os conjuntos fornecidos como respostas das consultas e as linguagens de programação que não suportam conjuntos. Portanto, sempre que precisarmos executar um comando SQL no banco usando a linguagem Python, usaremos um cursor para construir essa ponte.

cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))

print("Tabela criada!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
    # <class 'sqlite3.Cursor'>
    # Tabela criada!
    # Descrição do cursor:  None
    # Linhas afetadas:  -1

# A partir da conexão, criamos um objeto cursor.
# Invocamos o método execute() desse objeto para, enfim, criar a tabela pelo comando armazenado na variável ddl_create. Como o cursor é uma classe, ele possui métodos e atributos.
# Foram acessados os atributos description e rowcount. O primeiro diz respeito a informações sobre a execução; e o segundo a quantas linhas foram afetadas.
# No módulo sqlite3, o atributo description fornece os nomes das colunas da última consulta. Como se trata de uma instrução DDL, a description retornou None e a quantidade de linhas afetadas foi -1. Todo cursor e toda conexão, após executarem suas tarefas, devem ser fechados pelo método close().

# Segundo o PEP 249 (2020), todos os módulos devem implementar 7 campos para o resultado do atributo description: name, type_code, display_size, internal_size, precision, scale e null_ok.

# Além de criar uma tabela, também podemos excluí-la. A sintaxe para apagar uma tabela (e todos seus dados) é "DROP TABLE table_name".


# CRUD - CREATE, READ, UPDATE, DELETE

# CRUD é um acrônimo para as quatro operações de DML que podemos fazer em uma tabela no banco de dados. Podemos inserir informações (create), ler (read), atualizar (update) e apagar (delete).
# Os passos necessários para efetuar uma das operações do CRUD são sempre os mesmos:
# 1. estabelecer a conexão com um banco;
# 2. criar um cursor e executar o comando;
# 3. gravar a operação;
# 4. fechar o cursor e a conexão.

# CREATE

import sqlite3

conn = sqlite3.connect('aulaBD.bd')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
""")

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
""")

conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
    # Dados inseridos!
    # Descrição do cursor:  None
    # Linhas afetadas:  1

# Fizemos a conexão e criamos um cursor. 
# Através do cursor, inserimos 3 registros na tabela fornecedor. A sintaxe para a inserção exige que se passe os campos a serem inseridos e os valores.
# Não foi passado o campo id_fornecedor, pois este foi criado como autoincremento.
# Após a execução das três inserções, foi usado o método commit() para gravar as alterações na tabela. A quantidade de linhas afetadas foi 1, pois mostra o resultado da última execução do cursor, que foi a inserção de 1 registro.

# Uma maneira mais prática de inserir vários registros é passar uma lista de tuplas, na qual cada uma destas contém os dados a serem inseridos em uma linha. Nesse caso, teremos que usar o método executemany() do cursor.

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)""", dados)

conn.commit()

print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
    # Dados inseridos!
    # Descrição do cursor:  None
    # Linhas afetadas:  3

# Foi criado uma lista de tuplas chamada dados. Invocamos o método executemany() para inserir a lista.
# Os valores foram substituídos por interrogações, além da instrução SQL, o método exige a passagem dos dados. Agora foram afetadas 3 linhas no banco, pois esse foi o resultado do método do cursor.


# READ

# Agora que temos dados na tabela fornecedor, podemos recuperar os dados.
# Também precisamos estabelecer uma conexão e criar um objeto cursor para executar a instrução de seleção.
# Ao executar a seleção, podemos usar o método fetchall() para capturar todas as linhas, através de uma lista de tuplas.

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()

print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

resultado[:2]
    # Descrição do cursor:  (('id_fornecedor', None, None, None, None, None, None), ('nome_fornecedor', None, None, None, None, None, None), ('cnpj', None, None, None, None, None, None), ('cidade', None, None, None, None, None, None), ('estado', None, None, None, None, None, None), ('cep', None, None, None, None, None, None), ('data_cadastro', None, None, None, None, None, None))
    # Linhas afetadas:  -1
    # [(1,
    #   'Empresa A',
    #   '11.111.111/1111-11',
    #   'São Paulo',
    #   'SP',
    #   '11111-111',
    #   '2020-01-01'),
    #  (2,
    #   'Empresa B',
    #   '22.222.222/2222-22',
    #   'Rio de Janeiro',
    #   'RJ',
    #   '22222-222',
    #   '2020-01-01')]

for linha in resultado:
    print(linha)
    # (1, 'Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
    # (2, 'Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
    # (3, 'Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
    # (4, 'Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01')
    # (5, 'Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01')
    # (6, 'Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')

# Usamos a instrução SQL "select * from fornecedor" para selecionar todos (*) os dados da tabela fornecedor. O comando é executado pelo cursor e, através do método fetchall(), guardamos o resultado na variável "resultado".
# O resultado do método é uma lista de tuplas. Imprimimos uma fatia da lista. O resultado do atributo description, retornou tuplas, informando o nome da coluna afetada.
# Os outros 6 campos da tupla retornaram None graças à implementação do módulo sqlite3.

# Usamos uma estrutura de decisão para iterar na lista e imprimir cada valor. Cada linha é uma tupla com as informações que inserimos.


# Podemos selecionar somente os registros que satisfaçam uma determinada condição usando a cláusula "where", que funciona como uma estrutura condicional. No código a seguir, será selecionado somente o registro cujo id_fornecedor é igual a 5:

cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor = 5")
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conn.close()
[(5, 'Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01')]


# UPDATE

# Ao inserir um registro no banco, pode ser necessário alterar o valor de uma coluna, o que pode ser feito por meio da instrução SQL UPDATE.

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()
    # (1, 'Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
    # (2, 'Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
    # (3, 'Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
    # (4, 'Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01')
    # (5, 'Empresa E', '55.555.555/5555-55', 'Campinas', 'SP', '55555-555', '2020-01-01')
    # (6, 'Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')

# Alteramos o campo cidade do registro com id_fornecedor 5. No comando update é necessário usar a cláusula where para identificar o registro a ser alterado, caso não use, todos são alterados.
# Como estamos fazendo uma alteração no banco, precisamos gravar, razão pela qual usamos o commit(). Para checar a atualização fizemos uma leitura mostrando todos os registros.


# DELETE

# Ao inserir um registro no banco, pode ser necessário removê-lo no futuro, o que pode ser feito por meio da instrução SQL DELETE.

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()
    # (1, 'Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
    # (3, 'Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
    # (4, 'Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01')
    # (5, 'Empresa E', '55.555.555/5555-55', 'Campinas', 'SP', '55555-555', '2020-01-01')
    # (6, 'Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')

# Apagamos o registro com id_fornecedor 2. No comando delete, é necessário usar a cláusula where para identificar o registro apagado.
# Como estamos fazendo uma alteração no banco, precisamos gravar, razão pela qual usamos o commit(). Para checar a atualização, fizemos uma leitura que mostra todos os registros.

# Com a operação delete, concluímos nosso CRUD em um banco de dados SQLite usando a linguagem Python. O mais interessante e importante é que todas as etapas e todos os comandos que usamos podem ser aplicados em qualquer banco de dados relacional, uma vez que os módulos devem seguir as mesmas regras.

# INFORMAÇÕES DO BANCO DE DADOS E DAS TABELAS

# Além das operações de CRUD, é importante sabermos extrair informações estruturais do banco de dados e das tabelas.
# Por exemplo, considerado um banco de dados, quais tabelas existem ali? Quais são os campos de uma tabela? Qual é a estrutura da tabela, ou seja, qual DDL foi usada para gerá-la?
# Os comandos necessários para extrair essas informações podem mudar entre os bancos, mas vamos ver como extraí-las do SQLite. No código a seguir, temos uma instrução SQL capaz de retornar as tabelas no banco SQLite e outra capaz de extrair as DDLs usadas para gerar as tabelas.

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

# Lista as tabelas do banco de dados
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
print('Tabelas:')
for tabela in cursor.fetchall():
    print(tabela)

# Captura a DDL usada para criar a tabela
tabela = 'fornecedor'
cursor.execute(f"""SELECT sql FROM sqlite_master WHERE type='table' AND name='{tabela}'""")
print(f'\nDDL da tabela {tabela}:')
for schema in cursor.fetchall():
    print("%s" % (schema))    
    # cursor.close()
    # conn.close()
    # Tabelas:
    # ('fornecedor',)
    # ('sqlite_sequence',)
    # DDL da tabela fornecedor:
    # CREATE TABLE fornecedor (
    #     id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     nome_fornecedor TEXT NOT NULL,
    #     cnpj VARCHAR(18) NOT NULL,
    #     cidade TEXT, 
    #     estado VARCHAR(2) NOT NULL,
    #     cep VARCHAR(9) NOT NULL,
    #     data_cadastro DATE NOT NULL
    # )