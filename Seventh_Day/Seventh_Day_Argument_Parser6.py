import argparse

class Employ:
    def __init__(self, no_of_employee):
        self.no_of_employee = no_of_employee
        print("no of employ =>",self.no_of_employee)

    def add(self, a, b):
        print("Addition Of Givrn Argument =>",a+b)

    def mult(self, a, b):
        print("Multiplecation Of Given Argument =>",a*b)

    def sub(self, a, b):
        print("Substraction Of Givrn Argument =>",a-b)

    def div(self, a, b):
        print("dividation Of Givrn Argument =>",a/b)


if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('no_of_employee', help='employee',type=int)
    parser.add_argument('a', help='employee',type=int)
    parser.add_argument('b', help='employee',type=int)
    args = parser.parse_args()

    g= Employ(args.no_of_employee)
    g.add(args.a, args.b)
    g.sub(args.a, args.b)
    g.div(args.a, args.b)
    g.mult(args.a, args.b)

