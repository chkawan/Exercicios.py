# Defina a quantidade de passos
quantidade_de_passos = int(input())  # Receber a entrada do usuário

# Verifique se a quantidade de passos é positiva
if quantidade_de_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utilize um loop for para imprimir a mensagem do explorador
    for passo in range(1, quantidade_de_passos + 1):
        print(f"Explorador: {passo} passo" if passo == 1 else f"Explorador: {passo} passos")
