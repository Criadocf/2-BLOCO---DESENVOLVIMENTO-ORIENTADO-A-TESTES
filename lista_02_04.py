from random import randrange

posicoes = []

for c in range(15):
  adicionar = randrange(-15,85)
  posicoes.append(adicionar)

def maior_lista(posicoes):
  maior = -9999
  for c in posicoes:
    if c > maior:
      maior = c
  return maior
  
def posicao_maior_func(posicoes):
  posicao_maior = posicoes.index(max(posicoes))
  return posicao_maior

def menor_lista(posicoes):
  menor = 9999
  for m in posicoes:
    if m < menor:
      menor = m
  return menor

def posicao_menor_func(posicoes):
  posicao_menor = posicoes.index(min(posicoes))
  return posicao_menor

# a)
retorno_maior = maior_lista(posicoes)
retorno_posicao_maior = posicao_maior_func(posicoes)

# b)
retorno_menor = menor_lista(posicoes)
retorno_posicao_menor = posicao_menor_func(posicoes)



print(f'LISTA==> {posicoes}')

print(f'MAIOR DA LISTA ==> {retorno_maior}')
print(f'POSIÇÃO DO MAIOR DA LISTA ==> {retorno_posicao_maior+1}')

print(f'MENOR DA LISTA ==> {retorno_menor}')
print(f'POSICAO DO MENOR DA LISTA ==> {retorno_posicao_menor+1}')
