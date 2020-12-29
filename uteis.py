def leiaInt(msg):
  """
  -> Função que ler os dados pelo teclado e válida as informações.
  """
  while True:
    try:
      n = int(input(msg))
    except (ValueError):
      print('\033[33mDado inválido, por favor tente novamente\033[m')
      continue
    except (KeyboardInterrupt):
      print('\033[31mO usuario interrompeu o programa\033[m')
      return 0
    else:
      return n


def linha(tam=42):
  return '-'*tam

def cabecalho(txt):
  """
  -> Função que da corpo a todo o programa.
  """
  print(linha())
  print(txt.center(42))
  print(linha())

def menu(lista):
  cabecalho(f'\033[1;33mMENU PRINCIPAL\033[m')
  c = 1
  for iteem in lista:
    print(f'\033[33m{c}\033[m    → \033[34m  {iteem}\033[m')
    c += 1
  print(linha())
  opc = leiaInt(f'\033[32mSua opção: \033[m')
  return opc


#Dicionario de cores
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'laranja':'\033[33m',
'verde':'\033[32m',
'rosa':'\033[31m',
'lilas':'\033[35m',
'mar':'\033[36m',
';;;':'\033[37m',
'pretobranco':'\033[7;30m'} 