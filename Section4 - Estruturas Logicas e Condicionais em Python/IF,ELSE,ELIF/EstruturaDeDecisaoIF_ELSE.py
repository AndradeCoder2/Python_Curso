"""
Sintaxe da estrutura: 

if condição1:
    Bloco de codigo que sera execultado caso uma delas seja verdadeira.
    
    else:
        # Codigo que sera execultado quando uma delas for falsa.
    
"""

#  Exemplo estrutura de decisão IF-ELSE
produto = "celular"
preco = 200

if preco >= 300:
    print(f"Produto {produto} esta custando R$ {preco} ")
else:
    print("Você não tem saldo suficiente ")

#  Neste exemplo o temos duas variaveis 'produto' e outra 'preco'.
#  Estamos usando a estrutura de controle, para verificar caso o usuario,
#  tiver um valor maior que R$ 300, ele podera comprar o 'produto'.
# Caso o valor seja menor que R$ 300,ira aparecer a mensagem de 'saldo insuficiente'.

