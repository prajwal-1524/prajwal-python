#  def __del__(self):

class Test:
    def __init__(self):
        print('this is constructor')

    def __del__(self):
        print('this is destructor')

t=Test()
del t
print('end of application')