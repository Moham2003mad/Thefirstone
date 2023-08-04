# T=int(input())
# if T>100:
#     print('Steam')
# else:
#     if T<0:
#         print('Ice')
#     else:
#         print('Water')
print('===============================')
# T=int(input())
# if T>100:
#     print('Steam')
# elif T<0:
#     print('Ice')
# else:
#     print('Water')
print('===============================')
# Ave=float(input('enter your Average : '))
# if 18<Ave<=20:
#     print('Great')
# elif 15<Ave<=18:
#     print('Good')
# elif 10<Ave<=15:
#     print('Almost bad')
# elif 0< Ave<=10:
#     print('Very bad')
# else:
#     print('Enter a right number')
print('===============================')
# i=0
# while i<=20:
#     print(i)
#     i+=2
print('===============================')
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
print('===============================')
# n = int(input("pleas enter a number : "))
# b = 0
# while n != 0:
#     d = n % 10
#     n = n//10
#     b = b*10+d
# print(b)
# print(b*2)
print('===============================')
# n = int(input("pleas enter a number : "))
# b = 0
# while n != 0:
#     d = n % 10
#     n = n//10
#     b = b*10+d

# n=b
# b=0
# while n!=0:
#     d=n%10
#     n=n//10
#     b=b*10+d
#     print(f'{d}:',end="")
#     i=0
#     while i<d:
#         print(d,end='')
#         i+=1
#     print()
print('===============================')
# 123
# 321
# 456789123
# 321987654

# a = 123
# d = a%10
# c = a//10
# c%10


# a = int(input()) # 123
# b=0
# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d

# print(b)
print('==============================')
# n=int(input('enter a number'))
# if n >=0:
#     print(n)
# else :
#     n=-n
#     print(n)
print('==============================')
# a=int(input('enter a number : '))
# b=int(input('enter another number : '))
# n=0
# while b<=a:
#     if a % b ==0:
#         n+=1
#     print(b)
#     b+=1
# if n==0:
#     print("the number is prime")
# else :
#   print("the number is not prime")
print('==============================')
# n = int(input())
# i = 2
# p = True
# while i < n:
#     if n % i == 0:
#         p = False
#     i += 1
# print(p)
print('==============================')
# a = int(input())
# b = int(input())
# i=2
# n=0
# while i<b<=a:
#     if b % i == 0 :
#             n+=1            # [2,3,5,7,9]
        
print('==============================')
a=int(input('enter a number : '))
b=int(input('enter a number : '))
if b>=a:
    b,a=a,b
else:
    b=b
while b<=a:
    i=1
    n=0 
    while i<=b:
        if b % i==0:
            n+=1
            i+=1
        else:
            i+=1
    if n==2:
        print(b)
        b+=1
    else:
        b+=1
    
