def celsius_func(temperatura_fah):
  celsius = ((temperatura_fah-32)/9)*5
  return celsius.__round__(4)

while True:
  try:
    temperatura_fah = float(input())
    print(celsius_func(temperatura_fah))
    break
  except:
    print('Temperatura inválida! Tente novamente!')