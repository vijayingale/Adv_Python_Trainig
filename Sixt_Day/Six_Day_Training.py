import xml.etree.ElementTree as et
mytree = et.parse("../Eight_Day/template/example.xml")
myroot = mytree.getroot()

for price in myroot.iter('price'):
    price.text = str(float(price.text)+10)
    price.set('newprice','yes')



et.SubElement(myroot[0],"testy")
for temp in myroot.iter('tasty'):
    temp.text = str("YES")

print(myroot.remove(myroot[1]))
print(myroot[1][0].attrib.pop('name'))
mytree.write("modify.xml")


"""

import xml.etree.ElementTree as ET
mytree = ET.parse("x1.xml")
myroot = mytree.getroot()
for prices in myroot.iter('price'):
    prices.text = str(float(prices.text)+10)
    prices.set('newprices', 'yes')

for x in myroot.findall('food'):
    ET.SubElement(x, "tasty")

for temp in myroot.iter('tasty'):

    temp.text = str("YES")
# # poping the element
# print(myroot[2][0].attrib.pop('name'))
# # Delete
# print(myroot.remove(myroot[2]))
mytree.write('modified.xml')


"""