#receber um numero do user e retornar a tabuada

numero = int(input("Digite um número: "))

for count in range(10):
    print("%d x %d = %d" % (numero, count+1, numero*(count+1)))

#anotacoes: o count tem como intuito guardar o numero e o range dar sequencia