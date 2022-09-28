from random import randint

def gera_lista():
  listaW = []
  for c in range(10):
    y = randint(0,17)
    listaW.append(y)
  return listaW

ch1 = gera_lista()
print(ch1)

def contar_valor(ch1, y):
  repetido = ch1.count(y)
  return f'O número {y} ocorre {repetido} vez(es)!'

def position(ch1, y):
  positions = []
  for c, v in enumerate(ch1):
    if v == y:
      positions.append(c)
  return f'O número {y}, aparece nas seguintes posições: {positions}.'

y = int(input())

ch3 = contar_valor(ch1, y)
print(ch3)


ch4 = position(ch1,y)
print(ch4)
