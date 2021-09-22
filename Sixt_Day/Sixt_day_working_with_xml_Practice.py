import xml.etree.ElementTree as es
# from elem.configuration import ElemConfiguration as elem
import re
mytree = es.parse('../Eight_Day/template/six_day_practice_movies.xml')
myroot = mytree.getroot()
print(myroot)

#
print(myroot.tag)
print(myroot.attrib)
print(myroot[0].tag)

#
# for x in myroot[0]:
#     print(x.tag, x.attrib)
#
#
for x in myroot[1]:
    print( x.tag ,"-->",x.text)

# for x in myroot[2]:
#     print(x.text, x.attrib)
#
# for x in myroot[3]:
#     print(x.text, x.attrib)
#
# for x in myroot[4]:
#     print(x.text, x.attrib)
#
#
#
# for x in myroot.findall('movie'):
#     item = x.find('year').text
#     price = x.find('rating').text
#     name = x.attrib
#     print( item, price, name)
#
# print([elem.tag for elem in myroot.iter()])
#
#
#
# print(es.tostring(myroot, encoding='utf8').decode('utf8'))



# for movie in myroot.iter('movie'):
#     print(movie.attrib)




# for description in myroot.iter('sescription'):
    # print(description.text)




for movie in myroot.findall("./collection/movie/[year='2004']"):
    print("iii")
    print(movie.attrib)



# for x in myroot.findall('food'):
#     calaries = x.find('calories').text
#     x.append('<v></v>')
#     print( calaries)
#
#
#
# pint(myroot[0].findtext('description'))r






mytree.write("six_day_practice_movies.xml")

mytree = es.parse('../Eight_Day/template/six_day_practice_movies.xml')
myroot = mytree.getroot()

for movie in myroot.iter('movie'):
    print(movie.attrib)






















