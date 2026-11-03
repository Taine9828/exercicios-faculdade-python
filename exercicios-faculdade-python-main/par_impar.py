##Crie um programa em Python que solicite um número inteiro ao usuário e informe se ele é par ou ímpar.

numero = int(input("Digite um numero inteiro:"))
if numero % 2 == 0:
    print (f"numero par {numero}")
else:
    print (f"numero impar {numero}")
