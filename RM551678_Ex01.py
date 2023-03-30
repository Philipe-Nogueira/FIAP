"""1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver
um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para
gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema
de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente
obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e
que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a
porcentagem de acordo com cada nível de assinatura:
"""
# tabela de porcentagens e tipos de assinatura
#   "basic":    %30,
#   "silver":   %20,
#   "gold":     %10,
#   "platinum": %5
while True:
    faturamento_anual = float(input("Digite seu faturamento anual: "))
    tipo_assinatura = input("Escolha o tipo de assinatura (basic/silver/gold/platinum): ").lower()
    porcentagem = 0
    bonus = faturamento_anual * porcentagem
    if tipo_assinatura == "basic":
        porcentagem = 0.30
        bonus = faturamento_anual * porcentagem
        print(
            f"O valor a pagar de bônus para o cliente com assinatura {tipo_assinatura} e faturamento anual de R${faturamento_anual:.2f} é de R${bonus:.2f}.")
    elif tipo_assinatura == "silver":
        porcentagem = 0.20
        bonus = faturamento_anual * porcentagem
        print(
            f"O valor a pagar de bônus para o cliente com assinatura {tipo_assinatura} e faturamento anual de R${faturamento_anual:.2f} é de R${bonus:.2f}.")
    elif tipo_assinatura == "gold":
        porcentagem = 0.10
        bonus = faturamento_anual * porcentagem
        print(
            f"O valor a pagar de bônus para o cliente com assinatura {tipo_assinatura} e faturamento anual de R${faturamento_anual:.2f} é de R${bonus:.2f}.")
    elif tipo_assinatura == "platinum":
        porcentagem = 0.05
        bonus = faturamento_anual * porcentagem
        print(
            f"O valor a pagar de bônus para o cliente com assinatura {tipo_assinatura} e faturamento anual de R${faturamento_anual:.2f} é de R${bonus:.2f}.")
    else:
        print("Tipo de assinatura inválido.")
        continue
    break


