from random import randint

def load_list():
  listaX = []
  for c in range(10):
    cria = randint(0,100)
    listaX.append(cria)
  return listaX


def index(a):
  listaY = []
  for c,v in enumerate(range(len(a))):
      if c%2 == 0:
          listaY.append(a[c]/2)
      else:
          listaY.append(a[c]*3)
  return listaY

ch = load_list()
ch1 = index(ch)

print(f'{ch}\n{ch1}')