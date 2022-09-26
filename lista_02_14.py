listaC = []

for c in range(10):
  numero = int(input())
  listaC.append(numero)

for d in range(len(listaC)):
    if listaC[d] < 0:
      listaC[d] = 0
print(listaC)