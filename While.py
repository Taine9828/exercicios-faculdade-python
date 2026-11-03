# Escreva um programa que receba números e some eles até que o número digitado for -1.
# Ao final mostre a soma de todos os números digitados.

soma = 0
numero = 0

print ("Digite numeros para somar. -1 para encerrar")
numero = int(input())

while numero != -1:
    soma = soma + numero
numero = int(input ("Digite outro numero"))
print (f"A soma de todos os numeros é: {soma}")