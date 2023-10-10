def ucild(a,b):
    if a >= b:
        if a % b == 0:
            return b
        else:
            return ucild(b, a%b)
    else:
        if b % a == 0:
            return a
        else:
            return ucild(a, b%a)

a,b = map(int,input().split())
print(ucild(a,b))
print(int(a*b / ucild(a,b)))