#pedir ao usuario tres numeros e identificar o maior entre eles

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite mais um número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é: ", numero1)
elif numero2 > numero1 and numero2> numero3:
    print("O número maior é: ", numero2)
else:
    print("O número maior é: ", numero3)


#anotacao: o codigo acima possui a logica certa, utilizando if, elif e else como objetivo para estudo.
#contudo, seria executado da mesma forma com a funcao MAX.

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo: "))
number3 = int(input("Digite o terceiro: "))

maior_numero = max(number1, number2, number3)

print("O maior número é:", maior_numero)
