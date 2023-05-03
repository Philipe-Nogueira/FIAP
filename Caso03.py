
notas_impares = []
notas_pares = []

for i in range(1, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    while True:
        nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("ERRO: A nota deve estar entre 0 e 10.")
    notas_impares.append(nota)

for i in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    while True:
        nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("ERRO: A nota deve estar entre 0 e 10.")
    notas_pares.append(nota)

media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

if media_impares > media_pares:
    print("A metade dos alunos ímpares teve a maior média. E a média é: ", media_impares)
else:
    print("A metade dos alunos pares teve a maior média. E a média é: ", media_pares)

