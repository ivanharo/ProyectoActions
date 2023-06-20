import xml.etree.ElementTree as ET

try:
    xml_file = open('archi.xml')         
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        componente = xml_data.findall('componente')
        for comp in componente:
            print(f"Dato: {plant.find('componente').text}")
    else:
        print(False)
except Exception as err:
    print("Error:",err)
finally:
    xml_file.close()
