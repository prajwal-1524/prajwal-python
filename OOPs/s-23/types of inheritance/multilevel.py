# multiple level bata inherit vako 
# a->b->c

class P:
    def m1(Self):
        print('parent class')
class C(P):
    def m2(self):
        print('child method')
class CC(C):
    def m3(self):
        print('child child class')

cc=CC()
cc.m1()
cc.m2()
cc.m3()

