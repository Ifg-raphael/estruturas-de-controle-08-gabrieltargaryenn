# Sua solução aqui

altura = float(input())
sexo = input()

if sexo == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print(f"{peso:.2f}")
