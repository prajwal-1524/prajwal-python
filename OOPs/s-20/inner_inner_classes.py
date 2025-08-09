class Outer:
    def __init__(self):
        print('outer class')

    class Inner:
        def __init__(self):
            print(' inner class ')

        class InnerInner:
            def __init__(self):
                print('inner inner class')    

            def m(self):
                print('this is inner class method.')

# o = Outer()            
# i= o.Inner()
# ii = i.InnerInner()
# ii.m()            

            
ii = Outer().Inner().InnerInner()
ii.m()            