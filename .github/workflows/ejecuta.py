import xml.etree.ElementTree as ET
  
for renglon in open('archi.xml'):
  aux = []
 partes = renglon.split()[0]
  if partes[0] == '<Componente':
    print(renglon.split()[1])
  else 
    print('no se encontro')
