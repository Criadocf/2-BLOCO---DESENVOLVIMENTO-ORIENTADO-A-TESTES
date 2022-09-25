A = [10, 15, 17, 12, 9, 22, 5, 9, 0, 10, 22, 34, 73, 12, 9, 3, 12, 3, 5, 31]
B = [1.34, 3.41, 4.99, 1.34, 12.30, 7.80, 7.54, 10.91, 7.98, 8.54, 3.12, 4.12, 5.12, 5.54, 2.12, 4.32, 9.23, 4.21, 4.23, 4.67]

def faturamento_produto(lista1, lista2):
  for c in range(20):
    faturamento = lista1[c] * lista2[c]
    print(f' PRODUTO {c+1}: R$ {faturamento:.2f}')

def faturamento_total(lista1, lista2):
  faturamento_bruto = 0
  for d in range(20):
    calculando = lista1[d] * lista2[d]
    faturamento_bruto += calculando
  return f'FATURAMENTO TOTAL ==> R$ {faturamento_bruto:.2f}'

def faturamento_medio_func(lista1, lista2):
  faturamento_medio = 0
  for e in range(20):
    vento = lista1[e] * lista2[e]
    faturamento_medio += vento
  return f'{faturamento_medio/20:.2f}'

def faturamento_abaixo_media(lista1, lista2):
  print('FATURAMENTOS ABAIXO DA MEDIA')
  print(" ")
  for f in range(20):
    ver_valor = lista1[f] * lista2[f]
    if ver_valor < faturamento_medio_func(A, B):
      print(f'PRODUTO {f+1}: R$ {ver_valor:.2f}')

ch = faturamento_abaixo_media(A, B)