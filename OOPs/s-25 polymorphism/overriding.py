class Test:
    def m1(self):
        print('hello class 1')
class best(Test):
    def m1(self):
        print(' child class')
b=best()
b.m1()                