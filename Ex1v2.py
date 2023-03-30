
def calcular_bonus(tipo_assinatura, faturamento_anual):
    tabela_porcentagens = {
        'basic': 0.30,
        'silver': 0.20,
        'gold': 0.10,
        'platinum': 0.05
    }
    porcentagem = tabela_porcentagens[tipo_assinatura]
    bonus = faturamento_anual * porcentagem
    print(
        f"O valor do bônus para o cliente com assinatura {tipo_assinatura} e faturamento anual de R${faturamento_anual:.2f} é de R${bonus:.2f}.")
while True:
    faturamento_anual = float(input("Digite seu faturamento anual: "))
    tipo_assinatura = input("Escolha o tipo de assinatura (basic/silver/gold/platinum): ").lower()
    tabela_porcentagens = {
            'basic': 0.30,
            'silver': 0.20,
            'gold': 0.10,
            'platinum': 0.05
        }
    if tipo_assinatura not in tabela_porcentagens:
        print("Tipo de assinatura inválido. Tente novamente.")
        continue
    elif tipo_assinatura == "basic":
        calcular_bonus("basic", faturamento_anual)
    elif tipo_assinatura == "silver":
        calcular_bonus("silver", faturamento_anual)
    elif tipo_assinatura == "gold":
        calcular_bonus("gold", faturamento_anual)
    elif tipo_assinatura == "platinum":
        calcular_bonus("platinum", faturamento_anual)
    else:
        print("Tipo de Assinatura inválida! Tente novamente. ")
    break