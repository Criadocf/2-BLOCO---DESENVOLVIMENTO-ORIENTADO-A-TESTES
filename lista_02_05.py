A = list()
B = list()
C = list()

for c in range(3):
  numero = float(input('DIGITE UM NÚMERO: '))
  A.append(numero)

for d in range(3):
  numero2 = float(input('DIGITE OUTRO NÚMERO: '))
  B.append(numero)

for g in range(3):
  C.append(A[g])
  C.append(B[g])

print (f'{A}\n{B}\n{C}')


