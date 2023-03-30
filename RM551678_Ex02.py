"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor
para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de
votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira
e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
"""

"""
a sala tem 30 alunos (eleitores)
"""
#Definir
eleitores = int(input("Digite o numero total de eleitores:"))
segunda_feira = 0
terca_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0
votantes = 0

while (votantes < eleitores):
    voto = int(input("Digite 1 para votar na Segunda-Feira, 2 para o Terça-Feira, 3 para o Quarta-Feira, "
                     "4 para Quinta-Feira e 5 para Sexta-Feira: "))

    if (voto == 1):
        segunda_feira += 1
    elif (voto == 2):
        terca_feira += 1
    elif (voto == 3):
        quarta_feira += 1
    elif (voto == 4):
        quinta_feira += 1
    elif (voto == 5):
        sexta_feira += 1
    else:
        print("Número inválido, digite um numero entre 1 e 5")
        votantes -= 1
    votantes += 1

if(segunda_feira>terca_feira and segunda_feira>quarta_feira and segunda_feira>quinta_feira and segunda_feira>sexta_feira):
    print("A Live foi agendada para Segunda-Feira")
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")
elif(terca_feira>quarta_feira and terca_feira>quinta_feira and terca_feira>sexta_feira):
    print("A Live foi agendada para Terça-Feira")
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")

elif (quarta_feira>quinta_feira and quarta_feira>sexta_feira):
    print("A Live foi agendada para Quarta-Feira")
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")

elif (quinta_feira>sexta_feira):
    print("A Live foi agendada para Quinta-Feira")
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")

else:
    print("A Live foi agendada para Sexta-Feira")
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")
