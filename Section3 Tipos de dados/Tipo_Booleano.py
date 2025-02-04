"""
Tipo Booleano
Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Flaso

OBS: Sempre com a inicial maiuscula

Errado:
true, false

Certo:
True, False
"""

# Podemos utilizar para verificarmos se o usuario esta ativo no sistema.
ativo1 = False
print(ativo1)

#  Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado sera falso,
se for falso o resultado sera verdadeiro. Ou seja, sempre ao contrario.
"""
ativo2 = True
print(not ativo2)

print("===================================")

#  Operador (and)
"""
O operador #and retorna `True` se ambas as expressões em cada lado do operador forem verdadeiras. 
Caso contrario, retornam `False` 
"""
verdadeiro = True
falso = False
print(verdadeiro and verdadeiro) # Saida: True
print(verdadeiro and falso) # Saida: False

print("===================================")

#  Operador Ou (or)
"""
* O operador `or` retorna `True` se pelo menos uma das expressões em cada lado do operador for verdadeiro.
* Se ambas forem `falsas`, retorna `False`.
"""
verdadeiro = True
falso = False
print(verdadeiro or falso) #  Retorna: True.
print(verdadeiro or falso) #  Retorna: False.

print("===================================")

#  Usando operadores Booleanos com condições.
"""
Os operadores booleanos são frequentemente usados em conjunto com instruções condicionais, como *if*, *elif* e *else*.
Utilizamos condicionais para executarmos diferentes tipos de códigos, com base nas condições especificadas.
"""
idade = 18
if idade >= 18 and idade < 60:
    print("Você ja pode emitir sua Habilitação")
elif idade >= 60:
    print("Voê precisa renovar sua Habilitação")
elif idade < 18:
    print("Menor de idade")
else:
    print("Não existe")

intervalo = 10
if intervalo > 9:
    print("Hora do intervalo!")
else:
    print("Estamos em horario de aula")

print("===================================")

# Combinação de Operadores.
"""
Podemos combinar múltiplos operadores booleanos, 
em uma expressão complexa para verificar condições mais elaboradas.
"""
tem_cartao = True 
tem_saldoConta = False

if tem_cartao or tem_saldoConta:
    print("Pode fazer a compra")
else:
    print("Não pode realizar a compra")




