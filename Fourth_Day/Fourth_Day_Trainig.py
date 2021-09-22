emp_info = {}

while True:
    print("\n\t1.Create Employ Record")
    print("\n\t2.Update the emplyee details")
    print("\n\t3. Delete employ record")
    print("\n\t4.Display")
    print("\n\t5Exit")
    ch = int(input("\n\t Enter your choice[1-5] :"))
    emp_info = {}
    if ch == 1:
        name = input("\t\nEnter the employ name:")
        emp_id = int(input("\t\nEnter the employ id :"))
        ph = input("\n\tEnter The Phone Number ")
        tech = input("\n\t Technologies [coma seprated eg: C++, Python ,.net]")
        emp_info[emp_id] = {"name": name, "phone": ph, "tech": tech.split(',')}
    elif ch == 2:
        who = int(input("\n\t Whoes Details you want to update ? , Please enter the emp_id"))
        rec = emp_info[who]
        for field, value in rec.items():
            new = input('{}{{}}'.format(field, value))
            emp_info[who][field] = value if new == '' else new
    elif ch == 3:
        pass
    elif ch == 4:
        print(emp_info)
    else:
        break