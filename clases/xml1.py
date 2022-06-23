import xml.etree.ElementTree as ET

data = '''<person>
<name>jota</name>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)