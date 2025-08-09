# a=[2,5,6,3,6,10]
# print(a)
# for x in a:
#     print(x)

# l=list(range(20,30))
# print(l)
# l=[10,20,40,5,0,50]
# print(l[-1:-6:-2])

# l.append(50)
# print(l)
# l.remove(5)
# print(l)
# l.insert(2,'prajwal')
# print(l)
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# for x in l:
#     print(x)

# print(len(l))
# print(l.count(4))

# to add the numbers only divisible by 10
# l=[]
# for i in range(101):
#     if i%10==0:
#         l.append(i)
#         if i==20:
#             l.remove(i)    
# print(l)      

# aliasing and clonig
# x=[2,4,5]
# y=x
# y.insert(2,3)
# print(y)
# print(x)

# l=[]
# for x in range(5,20):
#     l.append(x)
# print(l)

# l=[i*i for i in range(1,11)]
# print(l)

# words=['prajwal','prince','romeo']
# l=[w[0] for w in words if w=='romeo']
# print(l)

# s='the quick brown fox jumps over the lazy dog'
# s='the quick brown fox jumps over the lazy dog'.split()
# l=[[i.upper(),len(i)] for i in s]
# print(l)

def add(a,b):
    print("list ko sum",a+b)