class Outer:
    def __init__(self):
        print('outer class')

    class Inner:
        def __init__(self):
            print(' inner class ')

        def m(self):
            print('this is inner class method.')

# o = Outer()
# i = o.Inner()
# i.m()
            
i=Outer().Inner()
i.m()            