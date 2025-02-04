#  2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.

#  Utilizando a forma comum, para os calculos.
print("==== Digite três numeros inteiros ====")

print("Digite o primeiro numero: ")
numero = int(input())

print("Digite o segundo numero: ")
numero2 = int(input())

print("Digite o terceiro numero: ")
numero3 = int(input())

print(numero + numero2 + numero3) 


print("=============================================")
 #  Utilizando a função sum()

print("==== Digite três números inteiros ====")

# Ler os números e converter para inteiro
print("Digite o primeiro numero: ")
numero11 = int(input())

print("Digite o segundo numero: ")
numero22 = int(input())

print("Digite o terceiro numero: ")
numero33 = int(input())

# Colocar os números em uma lista
numeros = [numero, numero2, numero3]

# Usar a função sum() para somar os números
soma = sum(numeros)

# Exibir o resultado da soma
print(soma)





