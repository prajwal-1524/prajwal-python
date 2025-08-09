class Student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name # object call hune bittikai __str__ call hunxa and then instead it returns string we override as return self.name
s=Student('prajwal')
print(s)