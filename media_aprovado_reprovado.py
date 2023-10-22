# Exercício Python 19: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print("saiba sua média")
nota1 = float(input("insira sua primeira nota:"))
nota2 = float(input("insira sua segunda nota:"))
media = (nota1+nota2)/2
if media >= 7.0 :
    print(f"aprovado sua média é:{media}")
elif media < 6.9 and media > 5.0 :
    print(f"recuperação sua média é:{media}")
else :
    print(f"reprovado sua média é:{media}")    