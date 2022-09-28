from random import randint

listaD =[]
listaE =[]
for c in range(10):
    numero = randint(10,30)
    listaD.append(numero)

for s in listaD:
    listaE.insert(0,s)

print(listaD)
print(listaE)