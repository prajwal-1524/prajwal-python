# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages + other.pages
# b1=Book(100)        
# b2=Book(200)
# # print(b1+b2)  
# print(b1+b2)      
        
# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def __gt__(self,other):
#         return self.mark > other.mark

# s1=Student('prajwal',90)
# s2=Student('bashyal',100)   
# print(s1>s2)

# class Employee:
#     def __init__(self,name,salary):
#         self.salary =salary
#         self.name = name
#     def __mul__(self,other):
#         return self.salary * other.days
# class Attendencesheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
# e=Employee('prajwal',15)
# t=Attendencesheet('prince',10)
# print(e*t)  #e*t vaye compulsory magic method e class ma huna parxa i.e first ma aune object ko class vitra                

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        # return self.pages + other.pages
        return Book(self.pages + other.pages)
    def __str__(self):
        return f"total pages is: {self.pages}"    
b1=Book(100)        
b2=Book(200)
b3=Book(50) 
print(b1+b2+b3) 