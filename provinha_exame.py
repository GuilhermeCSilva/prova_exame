from random import randint

#gero um numero randomico de 0-100
number = randint(0, 100)


if (number % 2):
    print(f'É Impar: {number}')
else:
    print(f'É Par: {number}')


fat = 1
i = 2

while i <= number:
    fat = fat*i
    i = i + 1

print("O valor de %d! eh =" %number, fat)

difference100 = 100 - number
difference0 = 0 + number

print(f"A diferença de {number} para 100 é de {difference100}")
print(f"A diferença de {number} para 0 é de {difference0}")

####################################################################################
#Lista
numbers = ['1', '2', '3', '4', '5']

#Tupla
#Tupla é semelhante a uma lista, porém, é imutavel, ou seja não é alteravel.
players = ('Ahri', 'Teemo')

#Dicionário
#Dicionários representam coleções de dados que contém na sua estrutura um conjunto de pares chave/valor
customer = {
    'name': 'Guilherme',
    'adrress': 'Seila',
    'phone': '11123123'
}

#Todos possuem métodos em cada um dos tipos.