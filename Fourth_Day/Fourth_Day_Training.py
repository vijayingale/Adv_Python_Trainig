# import math
#
# def validate(func):
#     def validator(*args, **kwargs):
#         if len(args)>1:
#             if args[1] == 0:
#                 print("\n\t We Expection non zero number")
#                 return None
#             else:
#                 power = func(args[0],args[1])
#                 return None
#         else:
#             print('invalid args')
#     return validator
#
#
# @validate
# def mypower(x,y):
#     return math.pow(x,y)
#
#
# mypower(10,0)
#
# def gst_calculate(func):
#     def validator(*args , **kwargs):
#         if len(args)>1:
#             if args[1]==0:
#                 print("\n\t We Except non zero number : ")
#                 return None
#             else:
#                 GST = func(args[0],args[1])
#                 print(GST)
#     return validator
#
# @gst_calculate
# def myGst(x,y):
#     fgst = (x*y)/100
#     fgst = x+fgst+fgst
#     return fgst
#
#
# myGst(100,2.5)
#
# import math
#
#
# def get_primenumber(func):
#     def validator(*args):
#         if len(args) > 1:
#             if args[1] == 0:
#                 print("\n\t Enter Non Zero Value : ")
#                 return None
#             else:
#                 prime = func(args[0])
#                 print(prime)
#
#     return validator
#
#
# def primrnum(x):
#     if x <= 1:
#         return False;
#     for i in range(2, int(math.sqrt(x))):
#         if x % i == 0:
#             return False;
#
#     return True;
#
# primrnum(7)

#
# # Passing possitional argument to decorators
#
# def accept_the_arguments(function_to_decorator):
#     def inner_function(*args, **kwargs):
#         print("\n\t Positional arguments are ", args)
#         print("\n\t the keyword arguments are", kwargs)
#         function_to_decorator(*args)
#
#     return inner_function
#
#
# @accept_the_arguments
# def function_with_args(a, b, c):
#     print(a, b, c)
#
#
# function_with_args(20, 30, 40)
def decorator_with_args(decorator_args1, decorator_args2, decorator_args3):
    def decorator(func):
        def wrapper(function_args1, function_args2, function_args3):
            print(
                "The wrapper can access all the variables\n \t from the decorator maker :\n\t{0} {1} {2}\n from the function call : \n\t{3} {4} {5}\n and pass then into decorator function ".format(
                    decorator_args1, decorator_args2, decorator_args3, function_args1, function_args2, function_args3))

            return func(function_args1, function_args2, function_args3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_with_args(pandas, "Numpy", "Sciki_learn")
def actual_function(function_args1, function_args2, function_args3):
    print("this is decorator function and it only knows about args\n\t{0}\n\t,{1}\n\t,\n\t{2}".format(function_args1, function_args2,
                                                                                      function_args3))

actual_function("john","Science","Tools")