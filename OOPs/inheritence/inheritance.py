# class P:
#     def m(self):
#         print('this is m method of class P')

# class C(P):
#     def m1(self):
#         print('this is m1 method of class C')      

# c=C()
# c.m()
# c.m1() 

# class P:
#     a=5
#     def __init__(self):
#         self.b=10
#     def m1(self):
#         print('this is instance method')   
    
#     @classmethod
#     def m2(cls):
#         print('this is class method')   

#     @staticmethod
#     def m3():
#         print('this is static method')

# class C(P):

#     pass
# c=C()
# c.m1()
# print(c.a)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#     def eat(self):
#         print('person can eat momo') 
    
# class Employee(Person): #person is an employee
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
        
#         self.eno=eno
#         self.esal=esal
#     def work(self):
#         print('employee can work')
#     def empinfo(self):
        # print('employee name:',self.name)    
        # print('employee age:',self.age)    
        # print('employee number:',self.eno)    
        # print('employee salary:',self.esal)    
    
# e=Employee('ram',47,'e45',50000)    
# e.work()
# e.empinfo()

class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print(f'car name: {self.name} \n car model:{self.model} \n color: {self.color}')    

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
        # employee has a car object : so has a relationship

    def work(self):
        print('employee can work ')
    def empinfo(self):
        print('employee name:',self.name)    
        print('employee age:',self.age)    
        print('employee number:',self.eno)    
        print('employee salary:',self.esal)    

c=Car('tesla','v2','black')            
e=Employee('prajwal',20,'e1',500000,c)  
e.empinfo()
