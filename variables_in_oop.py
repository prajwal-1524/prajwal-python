# instance  variable/object level variable
# class student:
#     # static variable
#     collegename='BMC'

#     def hello(self):
#         self.name='prajwal'
#         self.roll='prince'

#     @classmethod
#     def getcollegename(cls):
#         print('collegename is:',cls.collegename)
    
#     def call(self):
#         print('name is:',self.name)
#         print('roll no is',self.roll)

# s=student()
# s.hello()
# s.call()
# s.getcollegename()

# static variable 
class A:
    a=5
    def hello(self):
        
        pass

    def __init__(self):  # static variable inside the constructor
        A.b=20
        print(A.b)
        self.instantvar=599

    #static variable insider the class method cls.c i.e class level ko c ma 5 assign garne vaneko ho 
    @classmethod
    def hello2(cls):
        cls.c=5


obj=A()
print(obj.__dict__)  #this will give instant variables dictionay
print(A.__dict__)   #this will give static variables dictionary









