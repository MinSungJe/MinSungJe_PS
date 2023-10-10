a,b = input().split()
a2 = a[::-1]
b2 = b[::-1]
print(a2 if int(a2)>int(b2) else b2)