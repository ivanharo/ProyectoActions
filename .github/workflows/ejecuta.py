for renglon in open('archi.xml'):
  aux = []
  partes = renglon.split()
  if partes[0] == '<Componente':
    print(renglon.split()[1][2][3][4])
  else: 
    print('no se encontro')
