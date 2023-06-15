# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Escolha um número'))
sucessor = num + 1
antecessor = num - 1

print('O sucessor do', num, 'é', sucessor)
print('O antecessor de', num, 'é', antecessor)
# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número'))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'O dobro do seu numero é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz_quadrada}')

# Desenvolva um programa que leia as duas notas de um aluno e mostre a media.
nota1 = int(input('Digite a sua nota do primeiro bimestre'))
nota2 = int(input('Digite a sua nota do segundo bimestre'))
nota3 = int(input('Digite a sua nota do terceiro bimestre'))
nota4 = int(input('Digite a sua nota do quarto bimestre'))
soma = (nota1 + nota2 + nota3 + nota4) / 4

if soma >=6:
    print('Parabens, aprovado')
else:
    print('Reprovado')

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metros = int(input('Digite um numero'))
centimetros = metros * 100
milimetros = metros * 1000
print(f'Veja ele convertido: {centimetros} centimetros e {milimetros} milimetros')

# Faça um programa que leia um numero qualquer e mostre na tela a sua tabuada
numero=int(input('Digite o número que você gostaria de saber a tabuada:'))
for i in range(1,11):
    resultado=numero*i
    print(f'{numero} x {i} = {resultado}')
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar
carteira =  float(input('Quanto dinheiro você tem na carteira?'))

conversão_dolar = carteira / 4,86

print(f'com o dinheiro da sua carteira {carteira}, convertido em dolar é {conversão_dolar}')
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-las, sabendo que cada litro de tinta pinta uma area de 2m ao quadrado
altura = float (input('Digite a altura da parede'))
largura = float(input('Digite a largura'))

area = altura * largura

tinta = area / 2

# print(f'Para pintar uma area de {area} é necessario {tinta} litros de tinta')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o preço do produto'))

desconto = (preco * 5) / 100

preco_novo = preco - desconto

print(f'O preço será de {preco_novo}')
# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite o seu salario'))
aumento = (salario * 15) / 100
salario_novo = salario + aumento

print(f'Seu novo salario é {salario_novo}')

# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Quantos graus está nesse momento?'))
conversao = (celsius * 1.8) + 32
print(f'O valor em celsius convertido em Fahrenheit é {conversao}')

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = int(input('Quantos km o seu carro rodou?'))
dias = int(input('Quantos dias você alugou o carro?'))
pagamento_carro = (km * 0.15) + (dias * 60)
print(f'o valor do pagamento será R${pagamento_carro}')