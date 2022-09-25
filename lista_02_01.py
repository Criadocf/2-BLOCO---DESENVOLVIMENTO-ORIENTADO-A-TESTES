from random import randrange

lista = []

numero_par = 0
lista_par = []

numero_impar = 0
lista_impar = []



for c in range(0,100):
  numero = randrange(0,700)
  lista.append(numero)


for d in lista:
  if d % 2 == 0:
    lista_par.append(d)
    numero_par += 1
  
  elif d % 2 != 0:
    lista_impar.append(d)
    numero_impar += 1

print(f'LISTA TOTAL ==> {lista}')
print(f'QUANTIDADE DE NUMEROS PARES ==> {numero_par}')
print(f'LISTA DE PARES ==> {lista_par}')
print(f'QUANTIDADE DE NÚMEROS ÍMPARES ==> {numero_impar}')
print(f'LISTA DE ÍMPARES ==> {lista_impar}')
