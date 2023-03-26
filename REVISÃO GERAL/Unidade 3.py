# UNIDADE 3

### SESSÃO 1
# CLASSES E MÉTODOS

# Uma classe é a abstracao que descreve entidades do mundo real e quando instanciadas dao origem a objetos com caracteristicas similares. Classe = modelo, objeto = instancia.

# ABSTRAÇÃO - CLASSES E OBJETOS

# Objetos sao os componentes de um programa OO. Uma classe é um modelo para um objeto. Classe e uma forma de organizar os dados de um objeto e seus comportamentos.

# Exemplo: uma casa é um objeto(instancia) de uma planta(modelo/classe).

# ATRIBUTOS
# Dados armazenados em um objetos representam o estado do objeto, sao chamados de atributos. Atributos contem as informacoes que diferenciam os varios objetos.

# METODOS
# O comportamento de um objeto representa o que ele pode fazer. O comportamento é definido por procedimentos, funcoes e sub-rotinas. Os comportamentos estao contidos nos metodos, e é enviado uma mensagem para invoca-los.

# ENCAPSULAMENTOS
# Combinar os atributos e metodos na mesma entidade é chamado de encapsulamento. Na pratica de tornar os atributos privados, acontece quando estes sao encapsulados em metodos para guardar e acessar seus valores.

# HERANCA
# Heranca permite o reuso do codigo, criando solucoes mais organizadas. Heranca permite que uma classe herde os atributos e metodos de outra classe. Ex: classes funcionario e cliente herdam os atributos da classe Pessoa, a classe Pessoa é chamada de classe-pai, classe-base, superclasse ou ancestral. As classes derivadas sao classes-filhas ou subclasses.

# POLIMORFISMO
# Significa muitas formas, está fortemente associado à heranca. Quando uma mensagem é enviada para um objeto, ele deve ter um metodo definido para responder a essa mensagem. Na hierarquia de heranca, todas as subclasses herdam as interfaces de sua Superclasse. Porem como toda subclasse é uma entidade separada, cada uma delas pode exigir uma resposta separada para essa mensagem.

class PrimeiraClasse:
    def imprimir_mensagem(self, nome): # criar um metodo
        print(f"Olá {nome}, seja bem vindo")

objeto1 = PrimeiraClasse() # instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('John') # invocando um metodo
    # Olá John, seja bem vindo

# class PrimeiraClasse = Primeiro foi feito a declaracao.
# def imprimir_mensagem(self, nome) = foi criado um metodo para imprimir uma mensagem. Todo metodo em uma classe deve receber como primeiro parametro uma variavel que indica a referencia à classe (parametro self). O parametro "self" sera usado para acessar os atributos e metodos dentro da propria classe. Alem do parametro obrigatorio para os metodos, devem tambem receber um parametro que sera usado na impressao da mensagem. O parametro é tratado como uma variavel local.

# objeto1 = PrimeiraClasse() = instancia da classe (objeto). objeto1 é um objeto do tipo PrimeiraClasse e pode acessar seus atributos e metodos.
# objeto1.imprimir_mensagem('John') = invocado seu metodo passando o parametro 'John'. Foi passado somente 1 parametro, mesmo que a entrada espere 2 porque o parametro SELF é passado de forma implicita pelo objeto (so é necessario passar explicitamente os demais parametros de um metodo).
# Para acessar os recursos (parametros e metodos) de um objeto apos instancia-lo, é necessario usar a sintaxe: objeto.recurso.


# Construcao de uma classe Calculadora, que implementa como metodos quatro operacoes basicas de matematica, alem de obter o resto da divisao:

class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2
    
    def subtrair(self, n1, n2):
        return n1 - n2
    
    def multiplicar(self, n1, n2):
        return n1 * n2
    
    def dividir(self, n1, n2):
        return n1 / n2
    
    def dividir_resto(self, n1, n2):
        return n1 % n2
    
calc = Calculadora()

print('Soma:', calc.somar(4, 3))
print('Subtracao:', calc.subtrair(13, 7))
print('Multiplicacao:', calc.multiplicar(2, 4))
print('Divisao:', calc.dividir(16, 5))
print('Resto da divisao:', calc.dividir_resto(7, 3))
    # Soma: 7
    # Subtração: 6
    # Multiplicação: 8
    # Divisão: 3.2
    # Resto da divisão: 1

# Foi implementado os 5 metodos (todos possuem o parametro self, pois sao metodos da instancia da classe). Cada um deles recebe 2 parametros que sao suas variaveis locais nos metodos.
# calc = Calculadora() # foi instanciado um objeto tipo Calculadora e acessados seus metodos.


# CONSTRUTOR DA CLASSE __INIT__()
# Sera criado e utilizado atributos de instancia (variaveis de instancia). Esse tipo de atributo recebe um valor diferente para cada objeto.
# Um atributo de instancia é uma variavel precedida com o parametro "self", a sintaxe para utilizar é: self.nome_atributo.

# Ao instanciar um novo objeto é possivel determinar um estado inicial para variaveis de instancias por meio do METODO CONSTRUTOR da classe. O metodo construtor é chamado de __init__():

class Televisao:
    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)
    # Volume ao ligar a tv =  10
    # Volume atual =  11

# class Televisao: = criado classe Televisao que possui 1 atributo de instancia e 3 metodos, o primeiro é __init__ que significa que ele é invocado quando o objeto é instanciado.
# self.volume = 10 # é instanciado o atributo "volume" com valor 3, ou seja, todo objeto do tipo Televisao sera criado com volume = 10. O atributo recebe o prefixo "self" que o identifica como VARIAVEL DE INSTANCIA. Esse atributo pode ser usado em qualquer metodo da classe, ja que é um atributo do objeto, eliminando a necessidade de passar parametros para os metodos.

# def aumentar_volume(self): / def diminuir_volume(self): # nesses metodos foi alterado o atributo inicial sem precisar passar o parametro (ja que é uma variavel do objeto e nao uma variavel local).


# VARIAVEIS E METODOS PRIVADOS
# Nas linguagens de programacao OO, os atributos e metodos sao acompanhados de modificadores de acesso, que podem ser: public, private e protected.
# Em Python nao existem modificadores de acesso e todos os recursos sao PUBLICOS, porem para simbolizar que um atributo/metodo é privado, é utilizado o sublinhado "_" antes do nome. Ex: _cpf, _calcular_desconto().

# Conceitualmente dado que um atributo é privado, ele so pode ser acessado por membros da propria classe. Entao ao declarar um atributo privado, é necessario que os metodos acessem e recuperem os valores ali guardados. Alem de metodos para este fim, um atributo privado pode ser acessado por "decorators".

class ContaCorrente:
    def __init__(self):
        self._cpf = None
        self._saldo = None

    def depositar(self, valor):
        self._saldo += valor
    
    def consultar_saldo(self):
        return self._saldo
    
# class ContaCorrente: = implementado a classe ContaCorrente que possui 2 atributos privados: _cpf e _saldo.
# Para guardar um valor no atributo cpf, deve-se chamar o metodo "set_cpf" e para recuperar seu valor, é usado "get_cpf".
# Para guardar um valor no atributo saldo, é invocado o metodo "depositar()" e para recuperar seu valor, é usado o metodo "get_saldo".
# Atributos e métodos privados são apenas uma convenção, pois na prática, os recursos podem ser acessados de qualquer forma.


# HERANCA
# Por meio da heranca é possivel fazer a reutilizacao de codigo, permitindo que uma classe-filha herde os recursos da classe-pai. Uma classe aceita multiplas herancas (herda recursos de diversas classes).
# Se for uma heranca multipla, cada SUPERCLASSE deve ser separada por virgula.

class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None

    def bater_ponto(self):
        # codigo
        pass

    def fazer_login(self):
        # codigo
        pass

class Cliente(Pessoa):
    def __init__(self):
        self.codigo = None
        self.dataCadastro = None

    def fazer_compra(self):
        # codigo
        pass

    def pagar_conta(self):
        # codigo
        pass

f1 = Funcionario()
f1.nome = "Funcionario A"
print(f1.nome)

c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)
    # Funcionário A
    # 111.111.111-11
    
# class Pessoa: = criado classe PESSOA com 3 atributos que sao comuns à todas as pessoas do codigo.
# class Funcionario(Pessoa): = criado classe FUNCIONARIO que herda todos os recursos da classe PESSOA (um funcionario é uma pessoa).
# class Cliente(Pessoa): = criado classe CLIENTE, que tambem herda os recursos da classe pessoa (um cliente é uma pessoa).

# f1 = Funcionario() = instanciado um objeto do tipo FUNCIONARIO.
# f1.nome = "Funcionario A" = atribuindo ao atributo "nome" o valor: Funcionario A. O atributo "nome" foi herdado da CLASSE-PAI e foi utilizado normalmente pois a partir desse momento o atributo faz parte da classe-filha.
# O mesmo acontece com o atributo "cpf" utilizado no objeto "c1" que é do tipo CLIENTE.


# METODOS
# Quando a classe é criada em Python, ela herda nao explicitamente todos os recursos de uma classe-base chamada object. A funcao "dir()" retorna uma lista com os recursos de um objeto.
# class Pessoa() = explicitamente a classe PESSOA nao possui nenhuma heranca, porem possui uma serie de recursos.


# METODO CONSTRUTOR NA HERANCA E SOBRESCRITA
# Na heranca, ao adicionar a funcao "__init__()", a classe-filho nao herda o construtor dos pais (o construtor da classe-filho sobrescreve (override) o da classe-pai).

# Para usar o construtor da CLASSE-BASE, é necessario invocar explicitamente dentro do construtor-filho: ClassePai.__init__().

class int42(int):
    def __init__(self, n):
        int.__init__(n)

    def __add__(a, b):
        return 42
    
    def __str__(n):
        return '42'
    
a = int42(7)
b = int42(13)
print(a + b)
print(a)
print(b)
    # 42
    # 42
    # 42

c = int(7)
d = int(13)
print(c + d)
print(c)
print(d)
    # 20
    # 7
    # 13

# class int42(int): = classe-filho INT42 que tem como SUPERCLASSE a classe "int".
# int.__init__(n) = definido o construtor da classe, fazendo com que o construtor FILHO seja sobrescrito pelo construtor da classe-base (que espera receber um valor).

# O metodo construtor é um metodo 'magico', assim como "__add__" e "__str__".
# __add__ = retorna a soma de 2 valores, mas na classe INT42, ele foi sobrescrito para sempre retornar o mesmo valor.
# __str__ = retorna uma representacao de string do objeto, mas na classe INT42, foi sobrescrito para sempre imprimir 42 como a string de representacao do objeto (sera exibida sempre que a funcao "print()" for invocada para esse objeto).

# A classe INT42 recebe como parametro 1 valor, ja que esta sendo usado o construtor da classe-base "int".
# O metodo "__add__" ao inves de somar os valores, simplesmente retorna o valor 42 (pois foi construido assim).
# O metodo "__str__" tambem foi sobrescrito para sempre imprimir 42.

# Ao sobrescrever metodos magicos é utilizado uma importante tecnica da OO, o polimorfismo. Essa tecnica pode ser usada em qualquer metodo (nao somente nos magicos). A construcao de metodos com diferentes comportamentos podem ser feitos sobrescrevendo ou sobrecarregando os metodos.
# Sobrescrever (override) = a classe-filho sobrescreve um metodo da classe-base (o construtor ou qualquer outro metodo).
# Sobrecarregar (overload) = um metodo é escrito com diferentes assinaturas para suportar diferentes comportamentos.

# Em Python a operacao de SOBRECARGA nao é suportada diretamente (nao conseguimos escrever metodos com os mesmos nomes, mas diferentes parametos).
# Para realizar a SOBRECARGA, é possivel escrever o metodo com parametros 'default'. A depender do que forem passados, mediante a estruturas condicionais, o metodo pode ter diferentes comportamentos ou fazer OVERLOAD com a utilizacao do decorator "functools.singledispatch".


# HERANCA MULTIPLA
# Python permite que uma classe-filha herde recursos de mais de uma SUPERCLASSE, basta declarar cada classe a ser herdada separada por virgula:

class Ethernet():
    def __init__(self, name, mac_address):
        self.name = name
        self.mac_address = mac_address

class PCI():
    def __init__(self, bus, vendor):
        self.bus = bus
        self.vendor = vendor

class USB():
    def __init__(self, device):
        self.device = device

class Wireless(Ethernet):
    def __init__(self, name, mac_address):
        Ethernet.__init__(self, name, mac_address)

class PCIEthernet(PCI, Ethernet):
    def __init__(self, bus, vendor, name, mac_address):
        PCI.__init__(self, bus, vendor)
        Ethernet.__init__(self, name, mac_address)

class USBWireless(USB, Wireless):
    def __init__(self, device, name, mac_address):
        USB.__init__(self, device)
        Wireless.__init__(self, name, mac_address)

eth0 = PCIEthernet('pci :0:0:1', 'realtek', 'eth0', '00:11:22:33:44')
wlan0 = USBWireless('usb0', 'wlan0', '00:33:44:55:66')

print('PCIEthernet é uma PCI?', isinstance(eth0, PCI))
print('PCIEthernet é uma Ethernet?', isinstance(eth0, Ethernet))
print('PCIEthernet é uma USB?', isinstance(eth0, USB))

print('\nUSBWireless é uma USB?', isinstance(wlan0, USB))
print('USBWireless é uma Wireless?', isinstance(wlan0, Wireless))
print('USBWireless é uma Ethernet?', isinstance(wlan0, Ethernet))
print('USBWireless é uma PCI?', isinstance(wlan0, PCI))
    # PCIEthernet é uma PCI? True
    # PCIEthernet é uma Ethernet? True
    # PCIEthernet é uma USB? False

    # USBWireless é uma USB? True
    # USBWireless é uma Wireless? True
    # USBWireless é uma Ethernet? True
    # USBWireless é uma PCI? False

# class PCIEthernet(PCI, Ethernet): = herda recursos das classes PCI e ETHERNET (PCIEthernet é uma PCI e tambem uma Ethernet).
# class USBWireless(USB, Wireless): = herda de USB e Wireless (Wireless herda de Ethernet), entao USBWireless é uma USB, uma Wireless e uma Ethernet.
# isinstance(objeto, classe) = checa se um objeto é uma instancia de uma determinada classe.

class ContaCorrente:
    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._saldo = 0

    def _checar_saldo(self, valor):
        return self._saldo >= valor
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False
        
    def obter_saldo(self):
        return self._saldo
    
# class ContaCorrente: = criado classe ContaCorrente. Especificado que a classe deve ser construida recebendo como parametro um 'nome' (se nao for passado, o objeto nao é instanciado).
# def __init__(self, nome): = dentro do construtor foram criados atributos e seus valores iniciais. A variavel "_saldo" recebe um sublinhado como prefixo para indicar que é uma variavel privada e deve ser acessada somente por membros da classe. O valor deste atributo deve ser alterado pelos metodos depositar e sacar. Porem o atributo é usado tambem para checar o saldo e tambem no metodo de consulta ao saldo.

# def _checar_saldo(self, valor): = esse metodo é privado (por esse motivo recebe o underline). O metodo é usado como um dos passos para a realizacao do saque, a realizacao do saque so pode acontecer se houver saldo suficiente.
# self._checar_saldo(valor): = é invocado antes de realizar o saque. "self" indica que o metodo pertence à classe.

class ContaPF(ContaCorrente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
    
    def solicitar_emprestimo(self, valor):
        return self.obter_saldo() >= 500
    
# class ContaPF(ContaCorrente): = criado classe ContaPF, que herda todas as funcionalidades da classe-pai (ContaCorrente), inclusive seu construtor.
# O objeto deve ser instanciado passando o NOME e o CPF como parametros (o nome faz parte do CONSTRUTOR-BASE).
# Alem dos recursos herdados, foi criado o ATRIBUTO 'cpf' e o METODO 'realizar_emprestimo()', que consulta o saldo para aprovar ou nao o emprestimo.

class ContaPJ(ContaCorrente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def sacar_emprestimo(self, valor):
        return valor <= 5000
    
# class ContaPJ(ContaCorrente): = criado classe ContaPJ, que herda todas as funcionalidades da classe-pai (ContaCorrente), inclusive seu construtor.
# O objeto deve ser instanciado passando o NOME e o CNPJ como parametros (o nome faz parte do CONSTRUTOR-BASE).
# Alem dos recursos herdados, foi criado o ATRIBUTO cnpj e o METODO 'sacar_emprestimo()', que verifica se o valor solicitado é inferior a 5000.
# Para esse valor, nao foi usado o parametro 'self', pois se trata de uma variavel LOCAL e nao um atributo de classe ou instancia.

conta_pf1 = ContaPF("John", '111.111.111-11')
conta_pf1.depositar(1000)
print('Saldo atual é', conta_pf1.obter_saldo())
print('Recebera emprestimo = ', conta_pf1.solicitar_emprestimo(2000))

conta_pf1.sacar(800)
print('Saldo atual é', conta_pf1.obter_saldo())
print('Recebera emprestimo = ', conta_pf1.solicitar_emprestimo(2000))
    # Saldo atual é 1000
    # Receberá empréstimo =  True
    # Saldo atual é 200
    # Receberá emprestimo =  False

# conta_pf1 = ContaPF("John", '111.111.111-11') = criado objeto do tipo 'ContaPF' para testar as funcionalidades. Instanciado com os valores necessarios, feito deposito e consultado o saldo, depois foi solicitado o emprestimo.
# Como ha saldo suficiente, o emprestimo é aprovado. Na segunda parte do teste, foi realizado um saque, solicitado impressao do restante e solicitado novamente um emprestimo, esse por vez nao foi aprovado, pois nao ha saldo suficiente.

conta_pj1 = ContaPJ("Empresa A", "11.111.111/111-11")
print('Saldo atual é', conta_pj1.obter_saldo())
print('Recebera emprestimo = ', conta_pj1.sacar_emprestimo(3000))
    # Saldo atual é 0
    # Receberá empréstimo =  True

# conta_pj1 = ContaPJ("Empresa A", "11.111.111/111-11") = criado objeto do tipo 'ContaPJ' para testar as funcionalidades. Instanciado com os valores necessarios, feito deposito e consultado o saldo, depois foi solicitado o emprestimo.
# Mesmo nao havendo saldo para o cliente, uma vez que a regra do empréstimo nao depende desse atributo, o saque é permitido.


# DESAFIO:

# O diagrama de classes ilustra o reuso do codigo atraves do mecanismo de heranca (cada classe herda os atributos e metodos de outra classe).

# Um sistema precisa ser desenvolvido para atender três tipos distintos de clientes: pessoas físicas (PF) que compram com assiduidade, pessoas físicas que compram esporadicamente e pessoas jurídicas (PJ).
# Os clientes VIPs terão um numero ilimitado de itens para compra, enquanto os clientes PF nao-VIPs só poderão comprar até 20 itens e os clientes PJ poderão comprar até 50 itens.
# Para conceder benefícios nas compras, cada tipo de cliente terá um cupom de desconto: clientes VIPs terão um desconto de 20%, clientes PF esporádicos terão um desconto de 5% e clientes PJ terão um desconto de 10%.
# Para encapsular o cupom de desconto, será necessário criar um método.

class Cliente:
    def __init__(self):
        self.nome = None
        self.email = None
        self.telefone = None
        self._cupom_desconto = 0

    def get_cupom_desconto(self):
        return self._cupom_desconto
    
    def realizar_compras(self, lista_itens):
        pass

class ClienteVipPF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.2

    def realizar_compras(self, lista_itens):
        return f"Quantidade total de itens comprados = {len(lista_itens)}"
    
class ClientePF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.05

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 20:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."
    
class ClientePJ(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.1

    def realizar_compras(self, lista_itens):
        if len(lista_itens) <= 50:
            return f"Quantidade total de itens comprados = {len(lista_itens)}"
        else:
            return "Quantidade de itens superior ao limite permitido."
        
cli1 = ClienteVipPF()
cli1.nome = "Maria"
print(cli1.get_cupom_desconto())
print(cli1.realizar_compras(['item1', 'item2', 'item3']))
    # 0.2
    # Quantidade total de itens comprados = 3

# Foram implementadas quatro classes: uma classe-base e três subclasses, que herdam os recursos da classe-base. Todos os atributos que são comuns às classes devem ficaram na classe-base, enquanto os atributos específicos foram implementados nas classes-filhas.
# A quantidade de itens que cada cliente pode comprar é diferente, portanto o método 'realizar_compra()' foi sobrescrito em cada SUBCLASSE.
# Em cada classe-filha, determinados o valor do cupom de desconto logo após invocar o construtor da classe-base. sendo necessário encapsular esse recurso em um método em cada classe-filha.


### SESSÃO 2
# BIBLIOTECAS E Modulos

# Existem duas maneiras de organizar o codigo: implementando funcoes (cada bloco é responsavel por uma funcionalidade) e usando a OO para criar CLASSES que encapsulam as caracteristicas e comportamentos de um objeto.
# Idealmente para modular uma solucao, é necessario separar as funcoes ou classes em varios arquivos '.py'. De acordo com a documentacao oficial do Python, é recomendado separar em um arquivo a parte qualquer funcionalidade que possa ser utilizada (criando um modulo).

# Existem varios modulos: modulo 'math' que contem funcoes matematicas e o modulo 'os' que possui funcoes relacionadas ao sistema operacional, como captura do caminho (getcwd), listagem de diretorios (listdir) e criacao de novas pastas (mkdir). Esses modulos sao bibliotecas de funcoes especificas, que possibilitam reutilizar o codigo de forma eficiente e elegante.

# Para usar o modulo, é necessario importar para o arquivo:
# import moduloXXText
# import moduloXX as apelido
# from moduloXX import itemA, itemB

# Nos primeiros exemplos de importacao, todas as funcionalidades sao carregadas na memoria. Na primeira é usado no codigo o nome do modulo e na segunda o modulo foi atribuido a um apelido (as = alias). No ultimo exemplo do importacao, somente funcionalidades especificas do modulo sao carregadas na memoria.

# Todos os 'import' devem ficar no inicio do codigo, primeiro é declarado as bibliotecas-padrao (modulos built-in), depois as bibliotecas de terceiros, por fim os modulos especificos criados para a aplicacao. Cada bloco deve ser separado por uma linha em branco.


# CLASSIFICACAO DOS MODULOS (BIBLIOTECAS)
# Sao classificadas em 3 categorias:
# Modulos built-in: embutidos no interpretador.
# Modulos de terceiros: criados por terceiros e disponibilizados via PyPI.
# Modulos proprios: criados pelo desenvolvedor.

# MODULOS BUILT-IN
# Esses modulos sao embutidos no interpretador, entao nao é necessario sua instalacao.

# MODULO RANDOM
# É usado para criar numeros aleatorios:
# random.randint(a, b): retorna um valor inteiro aleatorio, de modo que esse numero esteja entre a, b.
# random.choice(seq): extrai um valor de forma aleatoria de uma certa sequência.
# random.sample(population, k): retorna uma lista com k elementos, extraidos da populacao.

import random

print(random.randint(0, 100))
print(random.choice([1, 10, -1, 100]))
print(random.sample(range(100000), k=12))
    # 80
    # 100
    # [18699, 46029, 49868, 59986, 14361, 27678, 69635, 39589, 74599, 6587, 61176, 14191]

# MODULO OS
# É usado para executar comandos no sistema operacional:
# os.getcwd(): retorna uma string com o caminho do diretorio de trabalho.
# os.listdir(path='.'): retorna uma lista com todas as entradas de um diretorio. Se nao for especificado um caminho, entao a busca é realizada em outro diretorio de trabalho.
# os.cpu_count(): retorna um inteiro com o numero de CPUs do sistema.
# os.getlogin(): retorna o nome do usuario logado.
# os.getenv(key): retorna uma string com o conteudo de uma variavel de ambiente especificada na key.
# os.getpid(): retorna o id do processo atual.

import os

os.getcwd()
os.listdir()
os.cpu_count()
os.getlogin()
os.getenv(key='path')
os.getpid()

# MODULO RE
# Regular expression fornece funcoes para busca de padroes em um texto. Permite verificar se uma determinada string corresponde a uma determinada expressao regular.

# re.search(pattern, string, flags=0) = varre a string procurando o primeiro local onde o padrão de expressão regular produz uma correspondência e o retorna. Retorna None se nenhuma correspondência é achada.
# re.match(pattern, string, flags=0) = procura por um padrão no começo da string. Retorna None se a sequência nao corresponder ao padrão.
# re.split(pattern, string, maxsplit=0, flags=0) = divide uma string pelas ocorrências do padrão.

# Tendo um arquivo com nomeado com a data: meuArquivo_20-01-2020.py:
# O objetivo é guardar a parte textual do nome em uma variavel para ser utilizada posteriormente. Serao usados os 3 metodos para fazer essa separacao:
# search() = faz a procura em toda a string. match() = faz a procura somento no comeco. split() = faz a transformacao em uma lista.
# Como queremos somente a parte textual, pegamos a posicao 0 da lista.

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

# padrao = "[a-zA-Z]*" = expressao regular para buscar sequencias de letras maiusculas e minusculas (pode variar de tamanho 0 ate N(*)).
# Nas variaveis 'texto1' e 'texto2' a expressao regular citada anteriormente foi usada para fazer a procura na string. Ambas encontraram, portando foi usado a funcao 'group()' da 're' para guardar o resultado.
# texto3 = re.split("_", string)[0] = usado "_" como marcacao para cortar a string, que retorna uma lista com 2 valores (sendo o texto a primeira parte), entao foi capturado a posicao [0].


# MODULO DATETIME
# Capaz de lidar com datas e horas, o modulo fornece classes para manipula-las. Como o modulo possui CLASSES, a sintaxe para acessar os metodos é a seguinte: modulo.classe.metodo().

# Classes DATETIME e TIMEDELTA do modulo DATETIME:

import datetime as dt

# Operacoes com data e hora
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

# import datetime as dt = feita importacao do modulo e atribuido um apelido 'dt'
# dt.datetime.today() = metodo today() da classe datetime que captura data e hora do sistema.
# dt.timedelta(days=1) = classe timedelta() para subtrair 1 dia de uma data especifica.
# dt.timedelta(weeks=1) = classe timedelta() para subtrair 1 semana de uma data especifica.
# dt.time.now() = metodo now() da classe datetime para capturar a data e hora do sistema.
# dt.timedelta(hours=2) = classe timedelta() para subtrair 2 horas de uma data especifica.
# dt.datetime.strftime(hoje, "%d-%m-%Y") = metodo strftime() da classe datetime para formatar a aparencia de uma data especifica.
# dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M") = metodo strptime() da classe datetime para converter uma string em um objeto do tipo datetime.


# MODULOS DE TERCEIROS
# Programadores autonomos e empresas podem usar o PyPI(Python Package Index) para criar e disponibilizar solucoes em Python em forma de bibliotecas no repositorio, permitindo que outros usuarios usem e contribuam para o crescimento da linguagem.


# BIBLIOTECA REQUESTS
# Habilita funcionalidades do protocolo 'HTTP' como get e post.
# get() = é responsavel por capturar informacoes da internet. Permite que o usuario informe a URL que deseja obter informacao. A sintaxe é: requests.get('https://xxxxxxxxxx').

# Exemplo de uso da biblioteca 'requests' e o metodo 'get()' para capturar o conteudo de uma API do github e guardar em uma variavel 'info':

import requests

info = requests.get('https://api.github.com/events')
info.headers
print(info)

print(info.headers['date']) # data da extracao
print(info.headers['server']) # servidor de origem
print(info.headers['status']) # status http da extracao, 200 é ok
print(info.encoding) # encoding do texto
print(info.headers['las-modified']) # data da ultima modificacao da informacao
    # Thu, 04 Jun 2020 22:09:33 GMT
    # GitHub.com
    # 200 OK
    # utf-8
    # Thu, 04 Jun 2020 22:04:33 GMT

# info.headers[] = retorna um dict de informacoes. Foram extraidas algumas informacoes dessa propriedade.
# Foi acessado a data da extracao, servidor acessado, status da extracao, codificacao do texto e a data da ultima modificacao da informacao do servidor.
# Tais informacoes podem ser usadas em um relatorio.

# É possivel usar uma propriedade 'text' para acessar o conteudo extraido, convertendo todo o conteudo para uma string ou metodo 'json()' que faz conversao para uma lista de 'dict'.
texto_str = info.text
print(type(texto_str))
texto_str[:100] # somente os 100 primeiros caracteres
    # <class 'str'>
    # '[{"id":"12535753096","type":"PushEvent","actor":{"id":5858581,"login":"grahamegrieve","display_login'

texto_json = info.json()
print(type(texto_json))
texto_json[0]
    # <class 'list'>

# O conteudo é uma 'string' e uma lista de dicionarios. É possivel usar o Python para fazer os tratamentos e extrair as informacoes.


# Utilizando a biblioteca 'requests' para extrair informacoes da Copa do Mundo de Futebol Feminino (2019):
# As informações estão disponíveis no endereço http://worldcup.sfg.io/matches, no formato chave:valor. Apos extrair as informacoes, sera gerado um relatorio contendo informacoes de cada jogo no formato: '(dia/mes/ano)' - 'time 1' x 'time 2' = gols 'time 1' a gols 'time 2'.

# extraindo informacoes com o 'request' e o metodo 'json()':
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

# Apos a importacao da biblioteca, foram usadas as informacoes do dicionario para definir os dados nos eixos x e y: 'datas_count.keys()' e 'datas_count.values()'.
# plt.figure(figsize=(15, 5)) = tamanho do grafico. Logo apos configurados os 'rotulos' dos eixos x e y.
# plt.xticks(rotation=45) = rotacao para as datas visualizadas no eixo x.
# plt.bar(eixo_x, eixo_y) = criacao do grafico, opcao de barra (bar) e passando informacoes a serem plotadas.
# plt.show() = exibir o grafico.


# MODULOS PROPRIOS
# Os codigos podem ser organizados em varios arquivos '.py' (modulos), cada modulo pode importar outros modulos, tanto os pertencentes ao mesmo projeto, como os built-in ou de terceiros.
# Criando um modulo 'utils.py', esse modulo possui uma funcao que cria uma conexao 'ssh' com determinado servidor. No modulo é preciso usar a lib 'paramiko' para construir a conexao.
# A funcao 'create_ssh_client()' retorna um client (a conexao em si). Em outro modulo chamado principal, é feita a importacao do modulo 'utils'.
# Dentro do modulo princupal sera utilizado a funcionalidade de conexao para copiar um arquivo localizado em um servidor para outro local. Ambos os arquivos .py precisam estar no mesmo nivel de pasta.

# Se for preciso usar o MODULO utils em vários projetos, é interessante transformá-lo em uma biblioteca e disponibilizá-la via PyPI.


# DESAFIO

# A biblioteca 'requests' habilita funcionalidades do protocolo HTTP (get e post). Dentre seus metodos, get() é responsavel por capturar informacoes da internet.

# Em um projeto de consultoria de software, o cliente solicitou a automação da extração de dados do CNAE, que é a classificação oficialmente adotada pelo Sistema Estatístico Nacional na produção de estatísticas por tipo de atividade econômica. Os dados estão disponíveis em um URL fornecido e o desenvolvedor foi responsável por gerar um relatório com as seguintes informações:

# Quantas atividades distintas estão registradas?
# Quantos grupos de atividades existem?
# Quantas atividades estão cadastradas em cada grupo?
# Qual grupo ou quais grupos possuem o maior numero de atividades vinculadas?


# RESOLUCAO
# Sera utilizada a biblioteca requests para extrair os dados e gerar o relatorio, em seguida manipular as listas e dicionarios para responder às perguntas.

# extracao
import requests

dados = requests.get('https://servicodados.ibge.gov.br/api/v2/cnae/classes').json() # resulta em uma lista de dict

dados[0] # exibir o primeiro registro de dados (primeiro dict da lista)
    # {'id': '01113',
    #  'descricao': 'CULTIVO DE CEREAIS',
    #  'grupo': {'id': '011',
    #   'descricao': 'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #   'divisao': {'id': '01',
    #    'descricao': 'AGRICULTURA, PECUÁRIA E SERVIÇOS RELACIONADOS',
    #    'secao': {'id': 'A',
    #     'descricao': 'AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AGRICULTURA'}}},
    #  'observacoes': ['Esta classe compreende - o cultivo de alpiste, arroz, aveia, centeio, cevada, milho, milheto, painço, sorgo, trigo, trigo preto, triticale e outros cereais nao especificados anteriormente',
    #   'Esta classe compreende ainda - o beneficiamento de cereais em estabelecimento agrícola, quando atividade complementar ao cultivo\r\n- a produção de sementes de cereais, quando atividade complementar ao cultivo',
    #   'Esta classe nao compreende - a produção de sementes certificadas dos cereais desta classe, inclusive modificadas geneticamente (01.41-5)\r\n- os serviços de preparação de terreno, cultivo e colheita realizados sob contrato (01.61-0)\r\n- o beneficiamento de cereais em estabelecimento agrícola realizado sob contrato (01.63-6)\r\n- o processamento ou beneficiamento de cereais em estabelecimento nao-agrícola (grupo 10.4) e (grupo 10.6)\r\n- a produção de biocombustível (19.32-2)']}

# Com os dados guardados em uma lista de dict, é possivel usar a funcao 'len()' para saber quantos elementos a lista possui. O resultado sera a quantidade de dict que representa as quantidades distintas de atividades.

# quantidades distintas de atividades
qtde_atividades_distintas = len(dados)

# Para saber quantos grupos de atividades existem, é necessario criar uma lista que percorre cada registro e extrai a informacao do grupo. No grupo, a informacao esta na chave interna 'descricao' da chave externa 'grupo', portanto para acessar, sera usado a sintaxe: ['chave_externa']['chave_interna'].
# Entao sera criada uma lista vazia, e dentro de uma extrutura de repeticao, sera extraida a informacao e guardada na lista.

# criar uma lista dos grupos de atividades, extraindo a descricao de cada registro
grupos = []
for registro in dados:
    grupos.append(registro['grupo']['descricao'])

grupos[:10]
    # ['PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'PRODUÇÃO DE LAVOURAS TEMPORÁRIAS',
    #  'HORTICULTURA E FLORICULTURA',
    #  'HORTICULTURA E FLORICULTURA',
    #  'EXTRAÇÃO DE MINERAIS METÁLICOS nao-FERROSOS']

# Com a lista contendo todos os grupos, é possivel usar o construtor 'set()' para criar um conjunto de dados sem as repeticoes e sem alterar a lista com todos. Com o resultado do set() é feita a contagem com a funcao 'len()' obtendo a quantidade de grupos distintos.

# extraindo a quantidade de grupos de atividades
qtde_grupos_distintos = len(set(grupos))

# Usando 'listcomp' sera criada uma lista de tuplas para contar quantas atividades estao cadastradas em cada grupo. Cada tupla vai conter o grupo e a contagem de quantas vezes esse grupo aparece na lista: (grupo, grupos.count(grupo)). Sendo feito para cada grupo distinto (for grupo in set(grupos)).

# com o resultado (lista de tuplas), é criado uma lina lista com o grupo e a quantidade de atividades pertencentes a ele
grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
grupos_count[:5]
    # [('TECELAGEM, EXCETO MALHA', 3),
    #  ('COMÉRCIO ATACADISTA DE PRODUTOS DE CONSUMO nao-ALIMENTAR', 8),
    #  ('ATIVIDADES DE ORGANIZAÇÕES ASSOCIATIVAS PATRONAIS, EMPRESARIAIS E PROFISSIONAIS',
    #   2),
    #  ('SEGURIDADE SOCIAL OBRIGATÓRIA', 1),
    #  ('FABRICAÇÃO DE ELETRODOMÉSTICOS', 2)]

# Para saber qual grupo/grupos possui maior numero de atividades vinculadas, a lista de tuplas sera transformada em um dict.

# por conveniencia a lista sera transformada em um dicionario
grupos_count = dict(grupos_count)

# Agora é possivel crirar uma lista que contem todos os grupos que possuem a contagem com mesmo valor da quantidade maxima encontrada. Com o dicionario, é possivel acessar a chave e o valor.

# com o dict, sera descoberto qual/quais grupos possuem mais atividades
valor_maximo = max(grupos_count.values())
grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]
print(len(grupos_mais_atividades))
grupos_mais_atividades
    # ['REPRESENTANTES COMERCIAIS E AGENTES DO COMÉRCIO, EXCETO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS']

# Criando uma CLASSE e um METODO, é possivel extrair quando necessario, basta instanciar a classe e invocar o metodo:

import requests

from datetime import datetime

class ETL:
    def __init__(self):
        self.url = None

    def extract_cnae_data(self, url):
        self.url = url
        data_extracao = datetime.today().strftime("%Y/%m/%d - %H:%M:%S")
        # faz extracao
        dados = requests.get(self.url).json()

        # extrai os grupos dos registros
        grupos = []
        for registro in dados:
            grupos.append(registro['grupo']['descricao'])

        # criar uma lista de tuplas (grupo, quantidade_atividades)
        grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
        grupos_count = dict(grupos_count) # transformar em um dicionario

        valor_maximo = max(grupos_count) # capturar valor maximo de atividades
        # gerar uma lista com grupos que possuem quantidade maxima de atividades
        grupos_mais_atividades = [chave for(chave, valor) in grupos_count.items() if valor == valor_maximo]

        # informacoes
        qtde_atividades_distintas = len(dados)
        qtde_grupos_distintos = len(set(grupos))

        print(f"Dados extraidos em: {data_extracao}")
        print(f"Quantidade de atividades distintas = {qtde_atividades_distintas}")
        print(f"Quantidade de grupos distintos = {qtde_grupos_distintos}")
        print(f"Grupos com maior numero de atividades = {grupos_mais_atividades}, atividades = {valor_maximo}")

        return None
    
# Usar a classe ETL:
ETL().extract_cnae_data('https://servicodados.ibge.gov.br/api/v2/cnae/classes')


### SESSÃO 3
# APLICAÇÃO DE BANCO DE DADOS

# As opções de armazenamento de dados utilizadas pelos softwares, podem ser em arquivos CSV, JSON, XML ou em um sistema de banco de dados. O sistema de banco de dados pode ser dividido em duas categorias: banco de dados relacional e banco de dados NoSQL.
# A abordagem relacional é baseada na teoria dos conjuntos e persiste os dados em tabelas, enquanto o NoSQL é projetado para lidar com a velocidade e a escala de aplicações em grande escala e em outros formatos nao estruturados. O NoSQL geralmente nao segue os princípios do sistema de gerenciamento de banco de dados relacional e é projetado especificamente para lidar com a grande quantidade de dados que trafegam na rede e são processados.






































































































