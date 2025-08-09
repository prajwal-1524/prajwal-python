class Engiene:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('car object using engiene object ')        

class Car:
    def __init__(self,):
        self.engiene = Engiene() #Engiene ko object lai nai car class vitra lyaye paxi sabai variables haru aaye
        #Engiene class ko object insider car class banako ho

    def m2(self):
        print('car object using engiene object ')
        print(self.engiene.a)
        self.engiene.m1()
        # accessing engiene class members through car

c=Car() 