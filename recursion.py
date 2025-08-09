# count=0
# def fact(n):
#     global count
#     count=count+1
#     if n<=1:
#         result=n
#     else:
#         result= n*fact(n-1)
#     return result
    
# n=eval(input('enter number of factorial you want'))
# a=fact(n)
# print(a)
# print(count) 

# anonymous functions lambda
# s=lambda n:n*n
# print(s(5))
# print(s(9))

# s=lambda a,b:a+b
# print('sum',s(5,6))


# l=[1,2,3,4,5,6,7,8,9,10,11,12,14,15]
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l1=[]
# for n in l:
#     if iseven(n)==True:
#         l1.append(n)
# print(l1)            
# 
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
# l=[1,2,3,4,5,6,7,8,9,10,11,12,14,15]
# l1=list(filter(iseven,l))
# print(l1)

# s=['prajwal','prashant','pooja']
# std=list(filter(lambda x:x[0]=='p',s))
# print(std)

# map ()

# reduce()
# l=[1,2,3,4,5]
# result = reduce( x,y:x+y,l)

def outer():
    print('this is outer function :')
    def inner():
        print('this is inner function:')
    
    print('outer functino calling inner function')
    inner()

outer()