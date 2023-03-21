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

    def imprimir_mensagem(self, nome): #criando um metodo
        print("Olá {nome}, seja bem vindo")

objeto1 = PrimeiraClasse() # instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('John') # invocando um metodo









