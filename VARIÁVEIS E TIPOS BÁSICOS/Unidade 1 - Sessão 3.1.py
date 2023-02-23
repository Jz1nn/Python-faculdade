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