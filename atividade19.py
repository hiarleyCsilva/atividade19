# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = 7
n2 = 7
n3 = 10
n1 = float ( input("digite a nota 1:"))
n2 = float ( input("digite a nota 2:"))
n3 = float ( input("digite a nota 3:"))
media = (n1+n2+n3)/3
print ("sua media é", media)
if media < 5:
    print("Reprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")