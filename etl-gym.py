# Simulação de dados de entrada (Extract)
dados_brutos = [
    {"nome": "João", "exercicio": "Supino", "peso": 50, "repeticoes": 10},
    {"nome": "Maria", "exercicio": "Agachamento", "peso": 70, "repeticoes": 12},
    {"nome": "Pedro", "exercicio": "Levantamento Terra", "peso": 90, "repeticoes": 8},
    {"nome": "Mariana", "exercicio": "Flexão", "peso": 0, "repeticoes": 20},
    {"nome": "José", "exercicio": "Supino", "peso": 60, "repeticoes": 8}
]

# Transformação dos dados (Transform)
for dado in dados_brutos:
    if dado["exercicio"] == "Supino":
        if dado["peso"] > 50 and dado["repeticoes"] > 8:
            dado["resultado"] = "Bom desempenho"
        else:
            dado["resultado"] = "Desempenho abaixo do esperado"
    else:
        dado["resultado"] = "N/A"

# Simulação de carregamento em um local de destino (Load)
for dado in dados_brutos:
    print(f"Nome: {dado['nome']}, Exercício: {dado['exercicio']}, Resultado: {dado['resultado']}")
