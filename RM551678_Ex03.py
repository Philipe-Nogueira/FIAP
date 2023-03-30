"""
3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito
grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50
alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve
digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois
as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média
de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar
cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
"""

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

