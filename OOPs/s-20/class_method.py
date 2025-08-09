# class ACEM:
#     department = 4
#     @classmethod  #decorator
#     def work(cls,name):

#         print(f"ACEM has {cls.department} department")
# ACEM.work('computer')

# to count number of object created 
class Test:
    count = 0

    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def noofobject(cls):
        print('the number of object created for test class,', cls.count)

t1=Test()
Test.noofobject()
