
# global variables
# a=5
# def hello():
#     global b
#     b=6
#     print(a)
# hello()
# print(b)

a=5
def hello():
    a=6
    print(a)
    print(globals()['a'])
hello()
