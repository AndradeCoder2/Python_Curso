#  Exemplo estrutura de decisão IF-ELIF-ELSE
idade = 10
anoDeNascimento = 1999

if idade >= 18 or anoDeNascimento >= 2000:
    print("Você ja e maior de idade! ") 
elif idade < 18 or anoDeNascimento < 2000:
    print("Você e considerado menor de idade! ")
else:
    print("Opção invalida! ")