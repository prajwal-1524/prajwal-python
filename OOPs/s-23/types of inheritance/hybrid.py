# class A:
#     def m1(self):
#         print('A class method')
# class B(A):
#     def m2(self):
#         print('Bclass method')
# class C(A):
#     def m1(self):
#         print('class c method') 
# class D(B,C):
#     def m3(self):
#         print('class D method')  
# d=D()
# d.m1()

# example 2
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('Bclass method')
class C(A):
    def m1(self):
        print('class c method') 
class X(A,B):
    def m1(self):
        print('class X method') 
class Y(B,C):
    def m1(self):
        print('class Y method') 

class P(X,Y,C):
    def m1(self):
        print('class P method') 


