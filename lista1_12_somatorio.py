def somatorio_func(a):
  somatorio = 0
  for c in range(1, a+1):
    somatorio += c
  return somatorio

while True:
  try:
      y = int(input())
      if y > 0:
        print(f'{somatorio_func(y)}')
        break
      else:
        print('DIGITE UM VALOR VÁLIDO')
        y = int(input())
        if y > 0:
          print(f'{somatorio_func(y)}')
          break
        else:
          while type(int) != type(y):
            y = int(input())
            print(f'{somatorio_func(y)}')
            break
  except:
    print('DIGITE UM VALOR VÁLIDO')


