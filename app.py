# Gerador de Senhas Simples
# MesaqueNexus
# UTF-8
# Python 3

import random
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
              '%', '&', '*', '(', ')', '-', '_', '+', '=', '§', '/',
              '?', '[', ']', '{', '}', 'ç', 'Ç', '|']
def loading():
  from time import sleep as s
  print('Carregando', end='')
  for p in ('.', '.', '.'):
    print(f'{p}', end='', flush=True)
    s(0.5)

def gerarSenha(tamanho_da_senha):
  senha = []
  i = tamanho_da_senha
  while i > 0:
    x = random.choice(caracteres)
    senha.append(x)
    i -= 1
  loading()
  print('\nSenha: ', end='')
  for caractere in senha:
    print(f"{caractere}", end='')

while True:
  try:
    x = int(input('Quantos caracteres deseja em sua senha? '))
    if x > 0 and x <= 8:
      print('---> Para uma maior segurança sugerimos que sua senha seja maior que 8 caracteres!')
      y = input('Deseja aumentar a quantidade de caracteres? ').upper()
      if y in ('S', 'SIM'):
        continue
      gerarSenha(x)
    else:
      gerarSenha(x)
    break
  except ValueError:
    print('''
    +------------------- ERROR ---------------------+
    | Entrada Inválida - entre com um valor inteiro |
    +-----------------------------------------------+
    ''')
