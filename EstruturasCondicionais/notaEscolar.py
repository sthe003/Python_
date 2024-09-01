#aprovacao, recuperacao ou reprovacao de aluno

nota = int(input("Informe sua nota: "))

if nota >= 60 and nota <=69:
    print("Será necessário a recuperação de nota")
elif nota >=70:
    print("Parabéns! Você foi aprovado(a)")
else:
    print("Você foi reprovado(a)")