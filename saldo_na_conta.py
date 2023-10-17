saldo_atual = float(input("Digite o saldo atual: "))
valor_deposito = float(input("Digite o valor do depósito: "))
valor_retirada = float(input("Digite o valor da retirada: "))

# Calcula o saldo atualizado
saldo_atual = saldo_atual + valor_deposito - valor_retirada

# Imprime o saldo atualizado formatado
print(f"Saldo atualizado: {saldo_atual:.1f}")
