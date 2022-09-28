from random import randint

def lista_R():
  R = []
  for c in range(5):
    gera = randint(0,76)
    R.append(gera)
  return R

def lista_S():
  S = []
  for c in range(10):
    load = randint(0,100)
    S.append(load)
  return S

ch1 = lista_R()
print(ch1)

ch2 = lista_S()
print(ch2)

def lista_X(ch1, ch2):
  X = []
  for c in ch1:
    X.append(c)
  for d in ch2:
    X.append(d)
  return X

retorno_X = lista_X(ch1, ch2)
print(retorno_X)

  