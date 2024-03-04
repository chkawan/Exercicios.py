def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 100 and textura == "bumpy" and cor == "yellow":
        return "A fruta é uma banana!"
    elif peso >= 120 and textura == "rough" and cor == "green":
        return "A fruta é uma maçã verde!"
    else:
        return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input("Digite o peso da fruta: "))
textura_fruta = input("Digite a textura da fruta (smooth, bumpy, rough): ")
cor_fruta = input("Digite a cor da fruta (red, yellow, green): ")

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)
