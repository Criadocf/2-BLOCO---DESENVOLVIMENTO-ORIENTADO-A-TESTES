nota1 = float(input())
nota2 = float(input())

def media(a, b):
  media_notas = (nota1+nota2)/2
  if media_notas >= 6:
    return f'Parabéns! Você foi aprovado! sua média foi de {media_notas}'
  else:
    return media_notas

ch = media(nota1,nota2)
print(ch)