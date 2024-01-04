# def super_func(*args, **kwargs):
#     total = 0
#     # print(kwargs)
#     for items in kwargs.values():
#         total +=items
#     return sum(args) + total

# print(super_func(1,2,3,4,5, num1 =5, num2=10))

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)

    inner()
    print("outer:", x)

outer()