# Recebendo a capacidade atual e o aumento percentual
capacidade_atual, aumento_percentual = map(int, input().split())

# Calculando a nova capacidade
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Convertendo a nova capacidade para inteiro
nova_capacidade_inteira = int(nova_capacidade)

# Imprimindo a nova capacidade
print("Nova capacidade:", nova_capacidade_inteira)
