def volume(raio):
  if type(raio) == str or type(raio) == bool or raio <= 0:
      return Exception
  return round(4/3 * 3.14 * raio**3, 2)

assert volume(-1) == Exception
assert volume('abc') == Exception
assert volume('*') == Exception
assert volume(True) == Exception
assert volume(False) == Exception
assert volume(1.0) == 4.19
assert volume(1) == 4.19
assert volume(10) == 4186.67
assert volume('$') == Exception
assert volume('@') == Exception
print('Todos os testes FILÉ!')

