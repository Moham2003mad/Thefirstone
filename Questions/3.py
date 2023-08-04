# a = int(input()) # 123
# b=0
# end_with_zero = False
# if a%10==0:
#     end_with_zero=True

# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d
# a = b
# b=0
# while a!=0:
#     d = a%10
#     a = a//10
#     # b = b*10+d
#     print(f"{d}: ",end="")
#     i = 0
#     while i<d:
#         print(d,end="")
#         i+=1 
#     print()

# if end_with_zero:
#     print(f"0: ")
n = input()
if n[0] == "0":
    for digit in str(n):
        N = int(digit)
        print(f"{digit}: {N*digit}")
else:
    n = int(n)
    if n == 0:
        print("0:")
    else:
        i = 1
        while i <= n:
            i = i*10
        if i != n:
            i = i//10
        j = i
        while j > 0:
            digit = n // j
            n = n - (j*digit)
            j = j//10
            digit_counter = 0
            print(str(digit)+": ", end="")
            while digit_counter < digit:
                print(digit, end="")
                digit_counter += 1
            print()