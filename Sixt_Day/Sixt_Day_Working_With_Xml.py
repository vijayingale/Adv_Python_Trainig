import xml.etree.ElementTree as et

mytree = et.parse('../Eight_Day/template/example.xml')
myroot =mytree.getroot()
print(myroot)

print(myroot.tag)
print(myroot.attrib)
print(myroot[0].tag)

for x in myroot[0]:
    print(x.tag,x.attrib)

for x in myroot[4]:
    print(x.text)


# try to create asall xml file and read it in same way

for x in myroot.findall('food'):
    item = x.find('item').text
    price = x.find('price').text
    print(item,price)


print(myroot[0].findtext('description'))