# DIAGRAMA DE CLASSES E HERANÇA

# Um diagrama de classes permite ilustrar o reúso de código através do mecanismo de herança, onde uma classe herda os atributos e métodos de outra classe.

# Um sistema precisa ser desenvolvido para atender três tipos distintos de clientes: pessoas físicas (PF) que compram com assiduidade, pessoas físicas que compram esporadicamente e pessoas jurídicas (PJ).
# Os clientes VIPs terão um número ilimitado de itens para compra, enquanto os clientes PF não-VIPs só poderão comprar até 20 itens e os clientes PJ poderão comprar até 50 itens.
# Para conceder benefícios nas compras, cada tipo de cliente terá um cupom de desconto: clientes VIPs terão um desconto de 20%, clientes PF esporádicos terão um desconto de 5% e clientes PJ terão um desconto de 10%.
# Para encapsular o cupom de desconto, será necessário criar um método.


# RESOLUÇÃO

# Para solucionar esse problema, será necessário implementar quatro classes: uma classe-base e três subclasses, que herdam os recursos da classe-base.
# Todos os atributos que são comuns às classes devem ficar na classe-base, enquanto os atributos específicos devem ser implementados nas classes-filhas.
# A quantidade de itens que cada cliente pode comprar é diferente, razão pela qual o método realizar_compra precisa ser sobrescrito em cada subclasse para atender a essa especificidade.
# Além disso, o cupom de desconto varia de acordo com o tipo de cliente, sendo necessário encapsular esse recurso em um método em cada classe-filha.

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

# Implementamos as quatro classes necessárias.
# Em cada classe-filha, determinados o valor do cupom de desconto logo após invocar o construtor da classe-base.
# Em cada subclasse também sobrescrevemos o método realizar_compras para atender aos requisitos específicos.