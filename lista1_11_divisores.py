def num_divisores(a):
  divisores = 0
  for c in range(1, a+1):
    if a % c == 0:
      divisores += 1
      
  return divisores

while True:
  try:
    numero = int(input('DIGITE O VALOR '))
    if numero > 0:
      ch = num_divisores(numero)
      print(ch)
      break
      while numero != type(int):
        print('DIGITE UM VALOR VÁLIDO')
        numero = int(input('DIGITE UM VALOR VÁLIDO '))
        ch = num_divisores(numero)
        print(ch)
        break
  except:
    print('DIGITE UM VALOR VÁLIDO')
      