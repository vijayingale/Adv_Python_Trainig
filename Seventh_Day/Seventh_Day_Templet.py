from jinja2 import Template

name = input("Enter name")
tn = Template("hello {{ name }}")
msg = tn.render(name=name)

print(msg)




name = "john"

age =  25

tn = Template("my name is {{name}} and I am {{age}}")

mag1 = tn.render(name = name ,age=age)

print(mag1)
