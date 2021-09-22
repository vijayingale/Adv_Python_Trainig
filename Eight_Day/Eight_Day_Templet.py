from jinja2 import Environment, FileSystemLoader
persons = [
    {"name":"andre","age":21},
    {"name":"raj","age":24},
    {"name":"rohit","age":27},
    {"name":"lucky","age":12}
]

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
templates = env.get_template("show_p1.txt")

output = templates.render(persons=persons)
print(output)