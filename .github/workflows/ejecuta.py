for renglon in open('archi.xml'):
  aux = []
  partes = renglon.split()
  if partes[0] == '<Componente':
    print(renglon.split()[1]renglon.split()[2]renglon.split()[3])
  else: 
    print('no se encontro')
