# STEP 1.
def func_carac():
    caractere = (input()).upper()
    if caractere == 'S' or caractere == 'N':
        return caractere
    else:
        return 'Caractere Inválido. Digite novamente'

while True:
    try:
        numero = float(input())
        print(f'{numero ** 3}')
        print('deseja continuar?')
        
        if func_carac() == 'N':
          break
        else:
          while recebe == 'S':
            numero = float(input())
            print(f'{numero ** 3}')
            print('deseja continuar?')
            recebe = func_carac().upper()
            break


    except:
        print('DIGITE UM NÚMERO')
