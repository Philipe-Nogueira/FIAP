def print_votos(dia, votos):
    print(f"{dia} teve {votos} votos.")

eleitores = int(input("Digite o numero total de eleitores: "))

if eleitores <= 0:
    print("Número inválido de eleitores.")
else:
    votos_por_dia = [0, 0, 0, 0, 0] # segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira
    votantes = 0
    while votantes < eleitores:
        voto = int(input("Digite 1 para votar na Segunda-Feira, 2 para o Terça-Feira, 3 para o Quarta-Feira, "
                         "4 para Quinta-Feira e 5 para Sexta-Feira: "))
        if 1 <= voto <= 5:
            votos_por_dia[voto-1] += 1
            votantes += 1
        else:
            print("Número inválido, digite um numero entre 1 e 5")

    dias_da_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
    for i, dia in enumerate(dias_da_semana):
        print_votos(dia, votos_por_dia[i])

    dia_com_mais_votos = dias_da_semana[votos_por_dia.index(max(votos_por_dia))]
    print(f"A Live foi agendada para {dia_com_mais_votos}")
