class Student:
    def setName(self,name):
        self.name = name
    
    def setMarks(self,marks):
        self.marks = marks

    def getName(self):
        return self.name 

    def getMarks(self):
        return self.marks

n=int(input('enter number of students'))
for i in range(n):
        s=Student()
        name = input('enter your name:')
        s.setName(name)
        marks = int(input('enter your marks:'))
        s.setMarks(marks)
        print('hi',s.getName())
        print('hi your marks is', s.getMarks())

