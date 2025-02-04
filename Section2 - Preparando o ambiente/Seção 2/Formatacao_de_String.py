# Formatação de String com '+' e .format()
nome = "Paulo" 
idade = 20
data = "2023-04-27"

print("Meu nome e {} tenho {} anos, e nasci em {}".format(nome, idade, data))
'''
# Removendo uma substring
string = "Hello World"
substring = string[:3]
print(substring)
'''
# Usando o metodo replace()
String = "Paulo Cesar"
substring = "Cesar"
new_string = String.replace(substring, "Python")
print(new_string)

# Length: Usamos para obter o numero de carcateres.
string = "Paulo Cesar" 
print(len(string))

# Usando slice()
string = "Paulo Cesar" 
substring = slice(1,4) 
print(string[substring])