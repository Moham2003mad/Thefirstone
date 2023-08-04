x = int(input())
y = int(input())
if 100<x and y<999:
    a = x % 10
    b = y % 10
    if a > b:
        print(f'{y} < {x}')
    elif b > a:
        print(f'{x} < {y}')
    elif b == a:
        n = x//10
        m = y//10
        h = n % 10
        g = m % 10
        if h > g:
            print(f'{y} < {x}')
        elif h < g:
            print(f'{x} < {y}')
        elif h == g:
            t = x//100
            u = y//100
            if t > u:
                print(f'{y} < {x}')
            elif t < u:
                print(f'{x} < {y}')
            else:
                print(f'{x} = {y}')

