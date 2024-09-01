#contar numeros até 100

numero = int(input("Digite um número até 99: "))

if numero > 100:
    print("Por favor, digite um número até 100.")
else:
    for i in range(numero, 101):
        print(i)

#anotacoes: o "i" irá armazenar o numero informado, o range tem como funcionalidade criar sequencias numerais