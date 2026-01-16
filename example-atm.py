opcao = ''
cedulas = [100, 50, 20, 10, 5, 2, 1]

while True:
  opcao = input('digite o valor a sacar (SAIR para sair): ')

  if str(opcao).lower() == 'sair':
    break
  
  valor = int(opcao)
  notas = []

  while valor > 0:
    for cedula in cedulas:
      if cedula <= valor:
        notas.append(cedula)
        valor -= cedula

  print(f'notas: {notas.sort()}')
