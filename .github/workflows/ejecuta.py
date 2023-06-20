import xml.etree.ElementTree as ET

try:
    xml_file = open('archi.xml')         
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_plants = xml_data.findall('aplicacion ')
        print(lst_plants)
        for plant in lst_plants:
            print(f"Dato: {plant.find('Componente').text}")
    else:
        print(False)
except Exception as err:
    print("Error:",err)
finally:
    xml_file.close()
