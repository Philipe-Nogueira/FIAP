
#Definir

def imprimir_votos():
    print("Segunda-Feira teve ", segunda_feira, "votos.")
    print("Terça-Feira teve ", terca_feira, "votos.")
    print("Quarta-Feira teve ", quarta_feira, "votos.")
    print("Quinta-Feira teve ", quinta_feira, "votos.")
    print("Sexta-Feira teve ", sexta_feira, "votos.")

while True:
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
        votos = [segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira]
        max_votos = max(votos)
        num_max_votos = votos.count(max_votos)

    if num_max_votos == 1:
        if max_votos == segunda_feira:
            print("A Live foi agendada para Segunda-Feira")
            imprimir_votos()
        elif max_votos == terca_feira:
            print("A Live foi agendada para Terça-Feira")
            imprimir_votos()
        elif max_votos == quarta_feira:
            print("A Live foi agendada para Quarta-Feira")
            imprimir_votos()
        elif max_votos == quinta_feira:
            print("A Live foi agendada para Quinta-Feira")
            imprimir_votos()
        elif max_votos == sexta_feira:
            print("A Live foi agendada para Sexta-Feira")
            imprimir_votos()
        break
    else:
        print("Houve um empate. Vamos reiniciar a votação.")
        imprimir_votos()



