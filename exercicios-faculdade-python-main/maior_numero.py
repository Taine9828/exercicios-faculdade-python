##programa em Python que solicite dois números ao usuário e informe qual deles é maior ou se os dois são iguais.

numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite outro numero:"))

if numero1 > numero2:
    print (f"Numero {numero1} é maior que {numero2}")
elif numero2 > numero1:
    print (f"Numero {numero2} é maior que {numero1}")
else:
    print (f"Numeros iguais")        