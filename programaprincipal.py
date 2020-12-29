'''Vamos criar um menu em Python, usando modularização.'''
from uteis import leiaInt, menu, cabecalho
from uteisb import arquivoExiste ,lerArquivo, criarArquivo, cadastrar
from time import sleep

"""
                      PROGRAMA PRINCIPAL
-> Sistema para cadastro de pessoas, e visualizações.
  O programa se utiliza de 2 módulos internos, um para leitura e formatação
  do sistema.
  O outro módulo ler e cria o arquivo txt para armazenamento dos nomes e idades.
"""
arq = 'cursodePython.txt'
if not arquivoExiste(arq):
  criarArquivo(arq)

while True:
  resp = menu(['Ver Pessoas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
  if resp == 1:
    #Opção de listar pessoas cadastradas 
    lerArquivo(arq)
  elif resp == 2:
    #Opção de cadastrar uma nova pessoa
    cabecalho('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    cadastrar(arq, nome, idade)
  elif resp == 3:
    print('\033[35mFinalizando o programa, até logo!\033[m')
    break
  else:
    print('ERRO! Opção inválidade, tente novamente.')
  sleep(2)
