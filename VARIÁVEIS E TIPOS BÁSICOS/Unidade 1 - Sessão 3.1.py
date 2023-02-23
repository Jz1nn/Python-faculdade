# ENUNCIADO

# O cliente que fabrica peças automotivas requisitou uma nova funcionalidade para o sistema: calcular o total de vendas. Como seus negócios estão expandindo, o cliente solicitou que o sistema seja capaz de receber valores em reais, dólar ou euro, e que seja feita a conversão para o valor em reais.

# Criar a função que fará o cálculo do valor.

# A função a ser construída precisa considerar os seguintes itens:

# O valor do produto (obrigatório).
# A quantidade do produto (obrigatório).
# A moeda em que deve ser feito o cálculo (obrigatório, sendo padrão o real).
# A porcentagem do desconto que será concedida na compra (opcional).
# A porcentagem de acréscimo, que depende da forma de pagamento (opcional).

# Uma conta não pode ter desconto e acréscimo ao mesmo tempo.

# Nessa primeira versão, você deve considerar os valores:
# Dólar em R$ 5,00.
# Euro 5,70.

def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde

    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto

    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")

# O nome da função "calcular_valor" executa ações, por isso, é uma boa prática escolher verbos infinitos.
# A função foi desenvolvida de modo a receber cinco parâmetros, sendo três deles obrigatórios e dois opcionais.
# Nessa implementação, para construir os parâmetros opcionais atribuímos o valor "None" às variáveis.
# Nesse caso, como tem um valor padrão, mesmo sendo "None", a função pode ser invocada sem a passagem desses parâmetros.
# Usamos as estruturas condicionais (if), (elif) e (else) para verificar se foram passados valores para desconto ou acréscimo.
# Caso tenha valores, serão diferentes de "None" e, então, os devidos cálculos são realizados.
# Após os cálculos de desconto, é feito o teste para saber qual moeda foi usada na compra e fazer a conversão para real.


# Outra implementação, usando o "**kwargs" para os argumentos opcionais.
# Nesse caso, um dicionário é recebido e precisa ter o valor extraído.

def calcular_valor(valor_prod, qtde, moeda="real", **kwargs):
    v_bruto = valor_prod * qtde

    if 'desconto' in kwargs:
        desconto = kwargs['desconto']
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif 'acrescimo' in kwargs:
        acrescimo = kwargs['acrescimo']
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
            v_liquido = v_bruto

    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")