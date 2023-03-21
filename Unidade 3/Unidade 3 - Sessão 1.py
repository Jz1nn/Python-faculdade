# CLASSES E MÉTODOS

# Uma classe é uma abstração que descreve entidades do mundo real e, quando instanciadas, dão origem a objetos com características similares. Portanto, a classe é o modelo e o objeto é uma instância.

# ABSTRAÇÃO - CLASSES E OBJETOS

# Objetos são os componentes de um programa OO.
# Um programa que usa a tecnologia OO é basicamente uma coleção de objetos.
# Uma classe é um modelo para um objeto.
# Podemos considerar uma classe uma forma de organizar os dados (de um objeto) e seus comportamentos.

# Vamos pensar na construção de uma casa: antes do "objeto casa" existir, um arquiteto fez a planta, determinando tudo que deveria fazer parte daquele objeto.
# Portanto, a classe é o modelo e o objeto é uma instância. Entende-se por instância a existência física, em memória, do objeto.


# ATRIBUTOS
# Os dados armazenados em um objeto representam o estado do objeto. Na terminologia de programação OO, esses dados são chamados de atributos. Os atributos contêm as informações que diferenciam os vários objetos.

# MÉTODOS
# O comportamento de um objeto representa o que este pode fazer. Nas linguagens procedurais, o comportamento é definido por procedimentos, funções e sub-rotinas. Na terminologia de programação OO, esses comportamentos estão contidos nos métodos, aos quais você envia uma mensagem para invocá-los. 

# ENCAPSULAMENTO
# O ato de combinar os atributos e métodos na mesma entidade é, na linguagem OO, chamado de encapsulamento, termo que também aparece na prática de tornar atributos privados, quando estes são encapsulados em métodos para guardar e acessar seus valores.

# HERANÇA
# Por meio desse mecanismo, é possível fazer o reúso de código, criando soluções mais organizadas. A herança permite que uma classe herde os atributos e métodos de outra classe. As classes funcionário e cliente herdam os atributos da classe pessoa. A classe pessoa pode ser chamada de classe-pai, classe-base, superclasse, ancestral; por sua vez, as classes derivadas são as classes-filhas, subclasses.

# POLIMORFISMO

# Polimorfismo é uma palavra grega que, literalmente, significa muitas formas. Embora o polimorfismo esteja fortemente associado à herança, é frequentemente citado separadamente como uma das vantagens mais poderosas das tecnologias orientadas a objetos. Quando uma mensagem é enviada para um objeto, este deve ter um método definido para responder a essa mensagem. Em uma hierarquia de herança, todas as subclasses herdam as interfaces de sua superclasse. No entanto, como toda subclasse é uma entidade separada, cada uma delas pode exigir uma resposta separada para a mesma mensagem.


class PrimeiraClasse:

    def imprimir_mensagem(self, nome): # criando um metodo
        print(f"Olá {nome}, seja bem vindo")

objeto1 = PrimeiraClasse() # instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('John') # invocando um metodo
    # Olá John, seja bem vindo

# Na linha 33 temos a declaração, e na linha 35 criamos um método para imprimir uma mensagem.
# Todo método em uma classe deve receber como primeiro parâmetro uma variável que indica a referência à classe; por convenção, adota-se o parâmetro self.
# O parâmetro self será usado para acessar os atributos e métodos dentro da própria classe. Além do parâmetro obrigatório para métodos, estes devem receber um parâmetro que será usado na impressão da mensagem. Assim como acontece nas funções, um parâmetro no método é tratado como uma variável local.

# Criamos uma instância da classe na linha 38 (criamos nosso primeiro objeto!). A variável "objeto1" agora é um objeto do tipo PrimeiraClasse, razão pela qual pode acessar seus atributos e métodos.
# Invocamos o método imprimir_mensagem(), passando como parâmetro o nome John.
# Por que passamos somente um parâmetro se o método escrito na entrada 1 espera dois parâmetros? O parâmetro self é a própria instância da classe e é passado de forma implícita pelo objeto. Ou seja, só precisamos passar explicitamente os demais parâmetros de um método.

# Para acessarmos os recursos (atributos e métodos) de um objeto, após instanciá-lo, precisamos usar a seguinte sintaxe: objeto.recurso.

# Vamos construir uma classe Calculadora, que implementa como métodos as quatro operações básicas matemáticas, além da operação de obter o resto da divisão.

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
print('Subtração:', calc.subtrair(13, 7))
print('Multiplicação:', calc.multiplicar(2, 4))
print('Divisão:', calc.dividir(16, 5))
print('Resto da divisão:', calc.dividir_resto(7, 3))
    # Soma: 7
    # Subtração: 6
    # Multiplicação: 8
    # Divisão: 3.2
    # Resto da divisão: 1

# Implementamos os cinco métodos, todos possuem o parâmetro self, pois são métodos da instância da classe. Cada um deles ainda recebe dois parâmetros que são duas variáveis locais nos métodos. Instanciamos um objeto do tipo Calculadora e acessamos seus métodos.


# CONSTRUTOR DA CLASSE __INIT__()

# Até o momento criamos classes com métodos, os quais utilizam variáveis locais.
# E os atributos das classes?
# Nesta seção, será criado e utilizado atributos de instância, também chamadas de variáveis de instâncias.
# Esse tipo de atributo é capaz de receber um valor diferente para cada objeto. Um atributo de instância é uma variável precedida com o parâmetro self, ou seja, a sintaxe para criar e utilizar é self.nome_atributo.

# Ao instanciar um novo objeto, é possível determinar um estado inicial para variáveis de instâncias por meio do método construtor da classe. O método construtor é chamado de __init__().

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

# Criamos a classe Televisao, que possui um atributo de instância e três métodos, o primeiro dos quais é (__init__), aquele que é invocado quando o objeto é instanciado.
# Nesse método construtor, instanciamos o atributo volume com o valor 10, ou seja, todo objeto do tipo Televisao será criado com volume = 10.
# O atributo recebe o prefixo self, que o identifica como variável de instância. Esse tipo de atributo pode ser usado em qualquer método da classe, uma vez que é um atributo do objeto, eliminando a necessidade de passar parâmetros para os métodos.
# Nos métodos aumentar_volume e diminuir_volume alteramos esse atributo sem precisar passá-lo como parâmetro, já que é uma variável do objeto, e não uma variável local.


# VARIÁVEIS E MÉTODOS PRIVADOS

# Em linguagens de programação OO, como Java e C#, as classes, os atributos e os métodos são acompanhados de modificadores de acesso, que podem ser: public, private e protected.
# Em Python, não existem modificadores de acesso e todos os recursos são públicos.
# Para simbolizar que um atributo ou método é privado, por convenção, usa-se um sublinhado "_" antes do nome; por exemplo, _cpf, _calcular_desconto().

# Conceitualmente, dado que um atributo é privado, ele só pode ser acessado por membros da própria classe.
# Portanto, ao declarar um atributo privado, precisamos de métodos que acessem e recuperam os valores ali guardados.
# Em Python, além de métodos para este fim, um atributo privado pode ser acessado por decorators.

class ContaCorrente:
    def __init__(self):
        self._saldo = None
    
    def depositar(self, valor):
        self._saldo += valor
    
    def consultar_saldo(self):
        return self._saldo
    
# Implementamos a classe ContaCorrente, que possui dois atributos privados: _cpf e _saldo.
# Para guardar um valor no atributo cpf, deve-se chamar o método set_cpf, e, para recuperar seu valor, usa-se get_cpf.
# Para guardar um valor no atributo saldo, é preciso invocar o método depositar(), e para recuperar seu valor, deve-se usar o método get_saldo.
# Atributos e métodos privados são apenas uma convenção, pois na prática, os recursos podem ser acessados de qualquer forma.


# HERANÇA EM PYTHON

# Um dos pilares da OO é a reutilização de código por meio da herança, que permite que uma classe-filha herde os recursos da classe-pai.
# Uma classe aceita múltiplas heranças, ou seja, herda recursos de diversas classes.
# A sintaxe para criar a herança é feita com parênteses após o nome da classe: class NomeClasseFilha(NomeClassePai).
# Se for uma herança múltipla, cada superclasse deve ser separada por vírgula.

# Será feito a implementação do diagrama de classes.

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
f1.nome = "Funcionário A"
print(f1.nome)

c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)
    # Funcionário A
    # 111.111.111-11

# Criamos a classe PESSOA com três atributos que são comuns a todas pessoas da nossa solução.
# Criamos a classe FUNCIONARIO, que herda todos os recursos da classe PESSOA, razão pela qual dizemos que "um funcionário é uma pessoa".
# Criamos a classe CLIENTE, que também herda os recursos da classe pessoa, logo, "um cliente é uma pessoa".

# Instanciamos um objeto do tipo funcionário, atribuindo à variável nome o valor "Funcionário A".
# O atributo nome foi herdado da classe-pai.
# O utilizamos normalmente, pois, na verdade, a partir de então esse atributo faz parte da classe mais especializada.
# O mesmo acontece para o atributo cpf, usado no objeto c1 que é do tipo cliente.


# MÉTODOS

# Quando uma classe é criada em Python, ela herda, mesmo que não declarado explicitamente, todos os recursos de uma classe-base chamada object.
# A função dir(), retorna uma lista com os recursos de um objeto.
# Como é possível observar, a classe Pessoa, que explicitamente não tem nenhuma herança, possui uma série de recursos nos quais os nomes estão com underline (sublinhado).

dir(Pessoa())
    # ['__class__',
    #  '__delattr__',
    #  '__dict__',
    #  '__dir__',
    #  '__doc__',
    #  '__eq__',
    #  '__format__',
    #  '__ge__',
    #  '__getattribute__',
    #  '__gt__',
    #  '__hash__',
    #  '__init__',
    #  '__init_subclass__',
    #  '__le__',
    #  '__lt__',
    #  '__module__',
    #  '__ne__',
    #  '__new__',
    #  '__reduce__',
    #  '__reduce_ex__',
    #  '__repr__',
    #  '__setattr__',
    #  '__sizeof__',
    #  '__str__',
    #  '__subclasshook__',
    #  '__weakref__',
    #  'cpf',
    #  'endereco',
    #  'nome']


# MÉTODO CONSTRUTOR NA HERANÇA E SOBRESCRITA

# Na herança, quando adicionamos a função __init__(), a classe-filho não herdará o construtor dos pais.
# Ou seja, o construtor da classe-filho sobrescreve (override) o da classe-pai.

# Para utilizar o construtor da classe-base, é necessário invocá-lo explicitamente, dentro do construtor-filho, da seguinte forma:
# ClassePai.__init__().

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

# Temos a classe-filho int42, que tem como superclasse a classe int.
# Definimos o construtor da nossa classe, mas fazemos com que nosso construtor seja sobrescrito pelo construtor da classe-base, o qual espera receber um valor.
# O método construtor é um método mágico, assim como o __add__ e o __str__. O primeiro retorna a soma de dois valores, mas na nossa classe int42, ele foi sobrescrito para sempre retornar o mesmo valor.
# O segundo método, __str__, retorna uma representação de string do objeto, e, na nossa classe, sobrescrevemos para sempre imprimir 42 como a string de representação do objeto, que será exibida sempre que a função print() for invocada para o objeto.

# Podemos conferir o efeito de substituir os métodos mágicos. Nossa classe int42 recebe como parâmetro um valor, uma vez que estamos usando o construtor da classe-base int.
# O método __add__, ao invés de somar os valores, simplesmente retorna o valor 42, pois o construímos assim.
# Podemos ver o efeito do método __str__, que também foi sobrescrito para sempre imprimir 42.

# Usamos a classe original int para você poder perceber a diferença no comportamento quando sobrescrevemos os métodos mágicos.

# Ao sobrescrever os métodos mágicos, utilizamos outra importante técnica da OO, o polimorfismo.
# Essa técnica, pode ser utilizada em qualquer método, não somente nos mágicos.
# Construir métodos com diferentes comportamentos pode ser feito sobrescrevendo (override) ou sobrecarregando (overload) métodos.
# No primeiro caso, a classe-filho sobrescreve um método da classe-base, por exemplo, o construtor, ou qualquer outro método.
# No segundo caso, da sobrecarga, um método é escrito com diferentes assinaturas para suportar diferentes comportamentos.

# Em Python, graças à sua natureza de interpretação e tipagem dinâmica, a operação de sobrecarga não é suportada de forma direta, o que significa que não conseguimos escrever métodos com os mesmos nomes, mas diferentes parâmetros.
# Para contornar essa característica, podemos escrever o método com parâmetros default.
# Assim, a depender dos que forem passados, mediante estruturas condicionais, o método pode ter diferentes comportamentos ou fazer o overload com a utilização do decorator functools.singledispatch.


# HERANÇA MÚLTIPLA