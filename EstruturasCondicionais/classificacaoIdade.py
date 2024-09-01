#identificar e classificar se o usuario e crianca, adolescente, adulto ou idoso

idade = int(input("Qual sua idade? "))

if idade <=12:
    print("Você é uma criança")
elif idade >=13 and idade <=17:
    print("Você é um adolescente")
elif idade >=18 and idade <=64:
    print("Você é um adulto")
else:
    print("Você é um idoso")