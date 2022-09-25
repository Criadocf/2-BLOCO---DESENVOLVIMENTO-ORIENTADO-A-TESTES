from random import uniform

lista1 = []
qtd_negativos = 0
soma_positivos = 0

for c in range(0,10):
  numero = uniform(-50, 50)
  numero_2_casa = numero.__round__(2)
  lista1.append(numero_2_casa)

for d in lista1:
  if d < 0:
    qtd_negativos += 1
  elif d > 0:
    soma_positivos += d

  
print(f'{lista1}')

print(qtd_negativos)

print(f'{soma_positivos:.2f}')

