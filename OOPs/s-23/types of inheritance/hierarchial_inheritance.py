class P:
    def m1(self):
        print('parent class')
class C1(P):
    def m2(self):
        print('1st child class')
class C2(P):
    def m3(self):
        print('this is 2nd class')
c=C1()
c.m1()
c.m2()
# c.m3()    paudena 

cc=C2()
cc.m1()
cc.m3()