numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero = 0


#Aritimeticos
soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
mod = numero1 % numero2
exp = numero1 ** numero2
print(f"resto da divisao entre {numero1} e o {numero2} = {mod}")
print(f"exponenciação entre os numeros {numero1} e {numero2} = {exp}")

#comparação

maior = numero1 > numero2
menor = numero1 < numero2
igual = numero1 == numero2
diferente = numero1 != numero2

maiorIgual = numero1 >= numero2
menorIgual = numero1 <= numero2

print(f"o numero {numero1} e maior ou igual ao numero {numero2}?: {maiorIgual}")
print(f"O numero {numero1} e diferente do numero {numero2}?: {diferente}")
print("\n")

#atribuição

#numero = numero + 1
numero += 7
numero -= 1
numero *= 1
numero /= 2
print(numero)