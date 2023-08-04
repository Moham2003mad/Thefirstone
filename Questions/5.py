n=int(input())
b=0
m=n
while m!=0:
    d=m%10
    m=m//10
    b=b*10+d
if b==n:
    print('YES')
else:
    print('NO')
    

