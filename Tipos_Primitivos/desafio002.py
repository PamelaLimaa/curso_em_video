# Faça um programa que leia dois números e faça a soma.
n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))
s = n1 + n2
print(s)
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele
a = input('digite algo')

print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?', a.isspace())
print('Só tem número?', a.isnumeric())
print('Só tem alfabetico?', a.isalpha())
print('Só tem alfanumerico?', a.isalnum())
print('Só tem maiuscula?', a.isupper())
print('Só tem minusculo?', a.islower())
print('é capitalizada?', a.istitle())
