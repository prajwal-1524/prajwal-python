from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['ktm','pokhara','hetauda','kavre','dolakha','biratnagar']
designation=['engineer','manager','hr','supervisor','teamlead','projectmanager',]

# generate name
def get_fake_name():
    name = choice(alphabets).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alphabets)
    return name
     

def get_fake_number():
    enum='e-'
    for i in range(4):
        enum=enum+choice(digits)
    return enum
# get_fake_number()    

def get_fake_salary():
    esal=uniform(10000,50000)
    return esal
# print(get_fake_salary())    

def get_fake_city():
    ecity=choice(cities)
    return ecity
# print(get_fake_city())    

def get_fake_mbl():
    mno=choice('6789')
    for i in range(9):
        mno=mno+choice(digits)
    return mno
# print(get_fake_mbl())    

def get_fake_designation():
    # global designation
    desig = choice(designation)
    return desig
# print(get_fake_designation())

print('employ records:')
for i in range(10):
    print('name of employee:',get_fake_name()) 
    print('employe id:',get_fake_number()) 
    print(get_fake_city()) 
    print(get_fake_mbl()) 
    print('employee salary: {:.2f}'.format(get_fake_salary())) 
    print(get_fake_designation()) 
    print()
    print()