while True:
    a,b,c = map(int,input().split())

    if a**2 == b**2 + c**2:
        result = "right"
    elif b**2 == a**2 + c**2:
        result = "right"
    elif c**2 == a**2 + b**2:
        result = "right"
    else:
        result = "wrong"

    if a == 0 and b == 0 and c == 0:
        break
    print(result)