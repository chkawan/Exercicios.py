def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return "Sua senha é muito curta. Recomenda-se no mínimo 8 caracteres."

    # Verificando se a senha contém letras maiúsculas, minúsculas, números e caracteres especiais
    for caractere in senha:
        if caractere.islower():
            tem_letra_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?":
            tem_caractere_especial = True

    # Verificando se a senha atende a todos os critérios
    if tem_letra_minuscula and tem_numero and tem_caractere_especial:
        return "Sua senha atende aos requisitos de segurança. Parabéns!"
    else:
        return "Sua senha não atende aos requisitos de segurança."

# Obtendo a senha do usuário
senha = input("Digite sua senha: ").strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
