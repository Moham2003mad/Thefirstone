a,b=map(int,input().split())
# a=int(input()) 
# b=int(input())
if 1<=a<=10 and 1<=b<=20:
    if b>10:
        x=21-b
        t='Left'
        y=11-a
    else:
        x=b
        t='Right'
        y=11-a
print(f'{t} {y} {x}')
# target = input()
# target = target.split(" ")
# y = int(target[0])
# x = int(target[1])
# if x <= 10:
#     print("Right", (11 - y), x)
# else:
#     print("Left", (11 - y), (21 - x))


