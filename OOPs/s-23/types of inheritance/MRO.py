# upto level two it works fine or normally we do not have problem calling the same method with same name in multiple class in the multipath inheritance but after level two we encounter the problem
class A:
    def m1(self):
        print('A class method')
class B:
    def m1(self):
        print('Bclass method')
class C:
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
print(P.mro()) 