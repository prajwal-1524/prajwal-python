# # '''import keyword
# # print(keyword.kwlist) '''

# # # a= 10.5
# # print(type(a))

# # '''b=1.2e3
# # print(b)'''

# # """a=5+2j
# # b=4+6j
# # print(a*b)
# # print(a.imag)"""

# # """'''bool type'''
# # a=5
# # b=6
# # print(a>b)
# # """

# # a="apple"
# # a='my name is "prajwal" bashyal and i am good'
# # b='a'
# # c='apple'
# # print(a)   for comment ctrl + /

# # slicing of the strings 
# # a = 'hello'
# # print(a[-2])
# # print(a[1:4:])

# # tuple 
# # a=(2,3,4,3)
# # print(a)
# # s={20,10,30}
# # print(type(s))
# # fs=frozenset(s)
# # print(type(fs))

# # dictionary
# # d={10:'prajwal', 20:'surose'}
# # d[20]= 'ananta'
# # print(d)
# # print(type(d))

# # r=range(10,200)
# # print(r[5])
# # print(r[3:6])
# # # for i in r:
# #     print(r)
# # print(r)
# # print(type(r))

# # bytes
# # b=[10,20,30]
# # b=bytes(b)
# # # print(b)
# # for i in b:
# #     print(i)

# # operators
# print(45/5)
# print(50//6)

# a=5
# b=6
# # print(a%b)
# # print("hello"+ " "+"prajwal")
# # a='prajwal'
# # print(a*5)
# # print(a+str(20))
# # print(a>=b)
# # print('ram'=='Ram')
# # print(not True)
# # print(10 and 20)

# # username = input("enter your username")
# # password = input(" enter your password")
# # if username == 'prajwal' and password == 'pass':
# #     print("correct inputdata")
# # else:    
# #     print('wrong username and the password')

# # print(4&5)
# # print(10<<2)

# # ternary operator 
# # a=10
# # b=20
# # x=10 if a<b else 20
# # print(x)
# # x= int(input('enter first number'))
# # y= int(input('enter second number'))
# # min=x if x>y else y
# # print(min)
# # print(type(min))


# def add(a,b):
#     a=10
#     b=20
#     return(a+b)

#     print(a+b)

# import mymath 
# print(mymath.a)
# d=mymath.add(40,30)

# import math 
# r=2
# print('area of circle is:',math.pi*r**2)
# print(math.gcd(100,200))
# print(dir(math)) 

# from math import sqrt
# print(sqrt(16))

# from math import *
# print(gcd(200,300))

# python input and output
# roll =int(input('enter your rollno:'))
# marks=float(input('enter your marks:'))
# name=input('enter your name:')
# # ispass=bool(input('enter True for pass and False for fail:'))
# ispass=eval(input('enter True for pass and False for fail:'))
# print('these are the students information:')
# print('students roll numb:',roll)
# print('students marks:',marks)
# print('students roll name:',name)
# print('students result:',ispass)

# multiple inputs at once 
# a=input('enter two numbers:')
# print(a) 
# takes two numbers as a single string

# we have to split those two numbers as:
# b=a.split()
# now the two inputs are seperated but still the numbers are represented or indicated as the strings so that to make these inputs int type we use following command 

# c=[int(x) for x in b]
# x,y=c
# print('the sum is',x+y)


# a,b=[int(x) for x in input('enter two numbers:').split() ]
# print('the sum is',a+b)

# x=eval(input('enter anything:'))
# print(type(x))

# a=5 
# b=6
# print('the values are:',a,b,sep=',')

# name='prince'
# age=10
# print('my name is:',name,'and my age is:',age)