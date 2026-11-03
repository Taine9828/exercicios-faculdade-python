## programa em Python que solicite a nota de um aluno e informe se ele foi aprovado, ficou em recuperação ou foi reprovado.
## Nota maior ou igual a 7: aprovado 
## Nota maior ou igual a 5 e menor que 7: recuperação
## Nota menor que 5: reprovado

nota = float(input("Digite a nota do aluno:"))
if nota >= 7:
    print (f"Nota {nota} Aluno aprovado!")
elif nota >= 5:
    print (f"Nota {nota} Aluno em recuperação!")
else:
    print (f"Nota {nota} Aluno reprovado!")

