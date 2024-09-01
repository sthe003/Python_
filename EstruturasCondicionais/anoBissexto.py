#ler e identificar se o ano é bissexto ou não

ano = int(input("Informe um ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Não é ano bissexto")