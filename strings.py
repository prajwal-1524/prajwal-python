# s='prajwal'
# i=0
# for x in s:
#     print('index of given string in both positive and negative index:')
#     print(f'the character {x} is present at positive {i} and negative {i-len(s)} index')
#     i+=1

# slice operator of string 
# s='prajwal'
# print(s[4:0:-1])
# p='hello world this is python '
# b=reversed(s)
# for x in b:
#     print(x,end=' ')

# s='prince'
# print(s[-1:-7:-1])
# print(s[::-1])

# concatenation
# s='prajwal learning python'
# print(s.find('r'))
# print(s.index('python',3,6))


# replace string 
# a=' hello python '
# b=a.replace('python','easy')
# print(id(b))

# split the string
# a='python is easy'.split()
# print(a)
# b='2082-2-23'.split('-')
# print(b)

# join the seperate strings of list and tuple
l=['hi','i','am','learning','python']
a=''.join(l)
print(a)

# same goes for tuple 

# case change of string
# a='helloworld'
# print(a.capitalize())
# print(a.isalnum())
# print(a.isalpha())

# print('the integer is{:d}'.format(3))
print(dir(str))