# Lista para armazenar os itens
itens = []

for i in range(3):
    novo_item = input(f"Digite o {i+1}º item: ")
    itens.append(novo_item)


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
