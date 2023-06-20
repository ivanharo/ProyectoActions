import xml.etree.ElementTree as ET

try:
    xml_file = open('archi.xml')         
    if xml_file.readable():
        print(True)
    else:
        print(False)
except Exception as err:
    print("Error:",err)
finally:
    xml_file.close()
