# Sua solução aqui

# Le a entrada do usuario como uma unica string, por exemplo: "1.60 M"
entrada = input()

# divide a string em duas partes usando espaço como separador:
# a primeira parte sera a altura (como string), e a segunda o sexo
altura, sexo = entrada.split() #split divide a string em partes

# converte a altura de string para numero com casas decimais (float)
altura = float(altura)

# verifica o sexo e aplica a formula correspondente
if sexo == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

# o :.2f imprime com 2 casas decimais
print(f"{peso:.2f}")
