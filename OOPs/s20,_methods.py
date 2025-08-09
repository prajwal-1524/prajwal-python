class Student :
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    
    def display(self):
        print('hi this is',self.name)
        print('hi the marks obtained is',self.marks)

    def grade(self):
        if self.marks >= 60:
            print('you got first division')
        elif self.marks >= 50:
            print('you got second division')
        elif self.marks >= 80:
            print('you got distinction') 
        else :
            print('you are failed')

for i in range(2):

    name=input('enter your name:')            
    marks=int(input('enter your marks:')) 

    s=Student(name,marks)
    s.display()
    s.grade()
    print('thankyou for viewing the result')