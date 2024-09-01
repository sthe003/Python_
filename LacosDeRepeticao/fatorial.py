#retornar o fatorial do numero informado pelo user

numero = int(input("Digite um número: "))

resultado = 1
conta = 1

while conta <= numero:
    resultado = resultado * conta
    conta = conta + 1
    print(resultado)



#feito com o laco for:
number = int(input("Digite um número: "))
result = 1
count = 1
for n in range(1,number+1):
    result = result * n

print(result)


