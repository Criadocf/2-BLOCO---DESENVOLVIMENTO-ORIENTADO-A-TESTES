lados = int(input('DIGITE O NÚMERO DE LADOS: '))
cm = float(input())
if lados == 3 or lados == 4 or lados == 5:
  if lados == 3:
    perimetro = cm*3
    print('TRIÂNGULO')
    print(f'Seu perímetro é igual a {perimetro} centímetros')
  
  elif lados == 4:
    area = cm**2
    print('QUADRADO')
    print(f'A área do quadrado é de {area:.1f}cm²')
  
  elif lados == 5:
    print('PENTÁGONO')

else:
  print('Digite um valor válido')

