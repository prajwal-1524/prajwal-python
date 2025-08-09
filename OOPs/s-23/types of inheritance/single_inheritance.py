class P:
    def m1(self):
        print('this is class p method m1')
class C(P):
    def m2(self):
        print('child class method m2')        

c=C()
c.m1()    
c.m2()