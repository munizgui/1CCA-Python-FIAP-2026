# OPERADORES DE ATRIBUIÇÃO
num = 15
print(num)

num += 2
print(num)

#OPERADORES RELACIONAIS
print()
print(6 >= 6)

idade = 20
print(idade == 20)

maior_idade = idade >= 18

#OPERADOR LÓGICO
#LOGICA E (and)
print()

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print('Entrar no programa')

print()

#NOTAS....


nota_final = 3

if nota_final < 4:
    print('REPROVADO')

elif nota_final < 6:
    print('RECUPERAÇÂO')

else:
    print('APROVADO')

print('FIM')
