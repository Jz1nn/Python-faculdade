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
    
# class ContaCorrente: = instanciado classe ContaCorrente. Especificado que a classe deve ser construida recebendo como parametro um 'nome' (se nao for passado, o objeto nao é instanciado).
# def __init__(self, nome): = dentro do construtor foram criados atributos e seus valores iniciais. A variavel "_saldo" recebe um sublinhado como prefixo para indicar que é uma variavel privada e deve ser acessada somente por membros da classe. O valor deste atributo deve ser alterado pelos metodos depositar e sacar. Porem o atributo é usado tambem para checar o saldo e tambem no metodo de consulta ao saldo.

# def _checar_saldo(self, valor): = esse metodo é privado (por esse motivo recebe o underline). O metodo é usado como um dos passos para a realizacao do saque, porque a realizacao do saque so pode acontecer se houver saldo suficiente.
# self._checar_saldo(valor): = é invocado antes de realizar o saque.