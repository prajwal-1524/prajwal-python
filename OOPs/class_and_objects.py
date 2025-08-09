# class A:
#     '''this class is demo class and does nothing'''
#     # a=5
#     # print('this is class a')

# print(A.__doc__)

# class Student:
#     '''this is class for student info:'''
#     def __init__(self):
#         self.name='prajwal'
#         self.roll=50
#         self.marks=98

#     def talk(self):
#         print('hello my name is',self.name)
#         print('hello my roll is',self.roll)
#         print('hello my marks is',self.marks)    

# s=Student()
# print(s.name)

# class A:
#     def __init__(self):
#         print(id(self))

# s=A()
# print(id(s))    

class Student:
    '''this is class for student info:'''
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def info(self):
        print('hello my name is',self.name)
        print('hello my roll is',self.roll)
        print('hello my marks is',self.marks)    

# s=Student('prajwal',10,99)
# s1=Student('prince',9,100)
# s.talk(89) 
# s1.talk(00)  

list_of_std= []

while True:
    name=input("enter the name:")
    age=eval(input("enter the age:"))
    marks=eval(input('enter the marks:'))
    s=Student(name,age,marks)
    list_of_std.append(s)

    print('students info is added')
    option= input('do you want to continue adding students? [yes/no]')
    if option.lower()=='no':
        break   #out of loop

print("all students info are:")
for s in list_of_std:
    s.info()
    print()
    print()
    
    
# print('value of x:)