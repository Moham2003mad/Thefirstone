# def hello():
#     print('hello world')
# hello()
print('\n===========================')
# def hello_2():
#     return 'hello world'
# s=hello_2()
# print(s)
print('\n===========================')
# def hello_3(p):
#     print(p)
# n='hello im mohammad'
# hello_3(n)
print('\n===========================')
# def add(a,b):
#     return a+b
# c=add(5,8)
# print(c)
# print(add(5,8))
print('\n===========================')
# def f(a):
#     a*=2
#     print(a)
#     return a+1
# print(f(9))
print('\n===========================')
# def max(x,y):
#     if x>y:
#         print(f'{x} is maximum')
#     elif x<y:
#         print(f'{y} is maximum')
#     else:
#         print(f'{x} equal with {y}')
# max(9,20)
print('\n==========================')
# def maxx(x,y):
#     if x>y:
#         return x
#     return y
# print(maxx(6,9))
print('\n===========================')
# def max3(x,y,z):
#     return maxx(x,maxx(y,z))
# print(max3(4,90,54))
print('\n===========================')
# def sp(r): ##### circle's area and circumference
#     Pi=3.14
#     return f'S :{Pi*r**2} ' , f'P : {Pi*2*r}'
# print(sp(4))
print('\n===========================')
# x=5
# def var():
#     global x
#     print(x)
#     x=3
#     print(x)
# var()
# print(x)
print('\n===========================')
# def f(a):
#     a[0]-=1
#     a[1]+=1
#     print(a)
# lst=[9,6]
# f(lst)
print('\n===========================')
# def dic(d):
#    d['a']-=1
#    d['b']+=1
# my_dict={'a':3, 'b':5}
# dic(my_dict)
# print(my_dict['a'])
# print(my_dict['b'])
print('\n===========================')
# def f(a,b=3,c=5):
#     print(a,b,c)
# f(1)
# f(1,4,6)
# f(4,c=7)
# f(3,b=9,c=30)
# f(b=3,c=8,a=4)
### f(2,b=3, 9)  Has an error
print('\n===========================')
# def u(*,a=3):   #### keyword only argument
#     print(a)
# u()
# u(a=5)
# u(4)   TypeError: u() takes 0 positional arguments but 1 was given
print('\n===========================')
# def f(*t):  #  var argument
#     s=0
#     for i in t:
#         s+=i
#     print(s)
# f(1,2,4,5)
print('\n===========================')
# def add(a,b,*more):
#     r=a+b+sum(more)
#     print(r)
# add(4,5,6,7,8,5)
print('\n===========================')
# def concat(*s,sep='.'):
#     return sep.join(s)
# print(concat('ali','ahmad','sara'))
# print(concat('ali','ahmad','sara',sep='/'))
print('\n===========================')
# def count_char(s):
#     d={}
#     for i in s:
#         if i in d.keys():
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(count_char('ahamad'))
print('\n===========================')
# def count_word(s):
#     d={}
#     words=s.split()
#     for i in words:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(count_word('salam salam bah bah man oomadam'))
print('\n===========================')
# def switch(a):
#     d={1:'one', 2:'two'}
#     return d.get(a,'nothing')
# print(switch(4))
# print(switch(1))
# grade_exam=[{'id':1,'m':70,'f':80} ,
#             {'id':2,'m':90,'f':50}   
#             ]
# def Ave(lst):
#     for d in lst:
#         n1=d.pop('m')
#         n2=d.pop('f')
#         d['Ave']=(n1+n2)/2
#     return lst
# print(Ave(grade_exam))
print('\n===========================')
# def Wayreverse():
#     s=input('Write a word :')
#     theword=list(s)
#     g=0
#     for i in theword:
#         g+=1
    
#     c=g-1
#     while c>=0:
#         print(theword[c] ,end='')
#         c-=1
# Wayreverse()
print('\n===========================')
# def Way2reverse(s):
#     r=''.join(reversed(s))
#     return list(r)
# print(Way2reverse('ahmad'))
print('\n===========================')
# def palindrome(s):
#     return s==s[::-1]
# print(palindrome('damad'))
# print(palindrome('nima'))
print('\n===========================')
# def deletestr(s):
#     a=list(s)
#     for i in a:
#         if a[i]==a[1]:
#             continue
#         elif a[i]==a[2]:
#             continue
#         elif a[i]==a[3]:
#             continue
#         else:
#             print(a[i])
#     return a
# print(deletestr('python'))
print('\n===========================')
# def remove_index(s,start,end):
#     if len(s)>end:
#         s=s[0:start]+s[end+1::]
#         print(s)     
# remove_index('python',1,3)
print('\n===========================')

# def remove_oddindex():
#     d=input('writer a word : ')
#     r=''
#     for i in range(len(d)):
#         if i%2==0:
#             r+=d[i]
#     return r
# print(remove_oddindex())
print('\n===========================')
# def cleanlist(s):
#     r=[]
#     for i in s:
#         if i not in r:
#             r.append(i)
#     return r
# print(cleanlist([1,2,6,6,6,3,2]))
print('\n===========================')
# def BBM(n):
#     r=[1]
#     for i in range(2 , n):
#         if (n % i) == 0:
#             r.append(i)
#     return r
# print(BBM(10))
print('\n===========================')
# def biggest(s):
#     w=''
#     lst=[]
#     for i in range(0,len(s)):
#         if (s[i]!=' '):
#            w+=s[i]
#         else:
#             lst.append(w)
#             w=''
#     m=lst[0]
#     for j in range(0,len(lst)):
#         if(len(lst[j])>len(m)):
#             m=lst[j]
#     return m
# print(biggest('salam ostadddddddddd azizz man'))
print('\n===========================')
# def pascal(n):
#     t=[1]
#     y=[0]
#     for x in range(max(n,0)):
#         print(t)
#         t=[i+j for i,j in zip(t+y,y+t)]
# pascal(5)
print('\n===========================')
# def g(s):
#     my_set=set()
#     w=s.split()
#     for i in w:
#         if i in my_set:
#             return i 
#         else:
#             my_set.add(i)
#     return 'None'
# s='ali  sara nima hamed  ali sara  hamed'
# print(g(s))
print('\n===========================')








        
  

    



    