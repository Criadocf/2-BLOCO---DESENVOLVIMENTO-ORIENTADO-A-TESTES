from random import randrange, uniform

lista = []
lista_inversa = []

for c in range(randrange(1,6)):
  numero = uniform(-30,30)
  numero_2_casa = numero.__round__(1)
  lista.append(numero_2_casa)

  lista_inversa.insert(0, numero_2_casa)


print(lista)

print(lista_inversa)