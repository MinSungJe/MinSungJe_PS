TC = int(input())

def getGCD(a, b):
    A = a
    B = b
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B
    
    return B

def getLCM(a, b):
    return (a*b) // getGCD(a, b)

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    s = input().split()
    t = input().split()
    Q = int(input())
    
    result = []
    LCM = getLCM(N, M)
    
    keyword = ['' for _ in range(LCM)]
    for i in range(LCM):
        sIdx = i % N
        tIdx = i % M
        keyword[i] = s[sIdx]+t[tIdx]
   
    for _ in range(Q):
        Y = int(input())
        idx = (Y-1) % LCM
        result.append(keyword[idx])
        
    print(f"#{test_case} {' '.join(result)}")
    