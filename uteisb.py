from uteis import cabecalho
def arquivoExiste(nome):
  """
  -> Função que verifica a existencia de um arquivo txt
  """
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

def criarArquivo(nome):
  """
  -> Função responsavél pela criação do arquivo txt.
  """
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('Houve um ERRO na criação do arquivo')
  else:
    print('Arquivo criado com sucesso!')

def lerArquivo(nome):
  """
  -> Função que retorna se o arquivo foi lido com sucesso.
  """
  try:
    a = open(nome, 'rt')
  except:
    print('Erro ao ler arquivo')
  else:
    cabecalho('PESSOAS CADASTRADAS')
    for linha in a:
      dado = linha.split(';')
      dado[1] = dado[1].replace('\n', '')
      print(f'Nome: {dado[0]}    → {dado[1]:>15} anos')
  finally:
    a.close()


def cadastrar(arq, nome=0, idade=0):
  """
  -> Função cadastra e armazena os dados informados pelo usuário: nome e idade.
  """
  try:
    a = open(arq, 'at')
  except:
    print('Houve um ERRO na abertura do arquivo')
  else:
    try:
      a.write(f'{nome}; {idade}\n')
    except:
      print('Houve um Erro na hora de escrever os dados')
    else:
      print(f'Novo registro de {nome} adicionado')
      a.close()