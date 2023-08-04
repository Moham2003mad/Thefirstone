# a=int(input())
# b=int(input())
# if b>=a:
#     b,a=a,b
# while b<=a:
#     i=1
#     n=0 
#     while i<=b:
#         if b % i==0:
#             n+=1
#             i+=1
#         else:
#             i+=1
#     if n==2:
#         print(b)
#         b+=1
#     else:
#         b+=1




a=int(input())
b=int(input())
if a>b:
    a,b=b,a
n=a
while n<=b:
    i=2
    p=True
    while i<n:
        if n % i==0:
            p=False
        i+=1
    if p:
        print(n)
    n+=1
            