valor_inicial = float(input())
taxa_juros = int(input())
periodo = int(input())

valor_final = valor_inicial

# Iterar com base no período em anos para calcular o valorFinal com os juros.
for _ in range(periodo):
    valor_final += valor_final * (taxa_juros / 100)

# Arredondar o valor final para duas casas decimais
valor_final = round(valor_final, 2)

print("Valor final do investimento: R$ {:.2f}".format(valor_final))
