# class P:
#     def m1(self):
#         print('this is parent method')
# class C(P):
#     def m1(self):
#         super().m1()
#         print('this is child method ')
# c=C()
# c.m1()        

# class P:
#     a=10
#     def __init__(self):
#         self.b=20
#         print('parent constructor is called.')
#     def m1(self):
#         print('parent class instance method')

#     @classmethod
#     def m2(cls):
#         print('parent class class method is called')

#     @staticmethod
#     def m3():
#         print('this is parent class satic method')
# class C(P):
#     a=555
#     def __init__(self):
#         self.b=666
#         print('child constructor is called')
#         super().__init__()
#         super().m1()
#         super().m2()
        

# c=C()  
# print(c.a)                 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def display(self):
        print('name:',self.name)
        print('age:',self.age)
class Student(Person):
    def __init__(self,name,age,roll,mark):
        super().__init__(name,age)
        self.roll=roll
        self.mark=mark
        self.display()
        super().display()
s=Student('prajwal',20,1,90)  
