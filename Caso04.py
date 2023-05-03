minutos_atuais = int(input("Digite quantos minutos a máquina está marcando: "))

fatorial = 1
i = 1

while i <= minutos_atuais:
    fatorial *= i
    i += 1

senha = "LIBERDADE" + str(fatorial)

print("A senha necessária para desbloqueio é:", senha)