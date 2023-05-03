
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


