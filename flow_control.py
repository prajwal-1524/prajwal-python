#   if statement
# name = input('enter name:')
# if name=='ram':
#     print('thik xa')
# print('this is the end of program') 

# if else statements 
# name = input('enter your name:')   
# roll = eval(input('enter your roll no:'))
# if name=='prajwal' and roll==10:
#     print('true shit')
# elif name=='roshan' and roll==7:
#     print(f'{name} is slightloy true')
# else:
#     print(f'{name} is a bad guess')    
# print('this is wrong shit')    

# a=5
# b=7
# c=8
# if a>b and a>c:
#     print(f'the greatest is {a}')
# elif b>a and b>c:
#     print(f'the greatest is  {b}')
# print(f'the greatest is c i.e : {c}')        

# num = eval(input('enter the number you want to check'))
# if num%2==0:
#     print('the given number is even')
# else:
#     print('the given number is odd')    

sub = input('enter your fav sub in IT:')
match sub:
    case 'OS':
        print('operating system')
    case 'DSA':
        print('DSA')    
    case 'NM':
        print('NM')
    case _: #to set default or if no matched input value
        print('oh no ! you missed exciting subject')       