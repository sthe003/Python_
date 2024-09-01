#identificar se o numero é positivo, zero ou negativo

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é igual a zero")