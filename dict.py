# key value pair

# d={100:'prajwal',200:'ram',300:'sam',}
# print(d)
# accessing dictionary 
# print(d[100])

# l=[(100,'prajwal'),(200,'sam'),(300,'luther')]
# d=dict(l)
# print(type(d))

# d=eval(input('enter dictionary:'))
# print(type(d))

# d={}
# n=eval(input('enter the total number of the student:'))
# i=1
# while i<=n:
#     name=input('enter the name of student:')
#     marks=eval(input('enter marks :'))
#     d[name]=marks
#     i+=1
# for x in d:
#     print(x,d[x])

s={10:'ram'}
d={20:'sam'}
# print(s+d) invalid operator
# print(s*3)
print(d.get(800,'not found! error'))
# print(d.keys('ram'))
for x in d.keys():
    print(x)