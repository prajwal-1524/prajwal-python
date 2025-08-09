class Test:
    def m(self):
        def calc(a,b):
            print('sum', a+b)
            print('mul',a*b)

        calc(10,20)
        calc(100,200)  
        
t=Test()
t.m()        