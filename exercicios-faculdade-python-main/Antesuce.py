#Escreva um programa que receba a digitação de um número inteiro e mostre qual é o seu número antecessor e o seu sucessor.

numero = int(input ("Digite um numero: "))
antecessor = numero - 1
sucessor = numero + 1
print (f"O antecessor do numero {numero} é {antecessor}", end="")
print (f" e o sucessor é o {sucessor}")