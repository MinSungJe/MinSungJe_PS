# 입력부
GCM, LCD = map(int, input().split())

# 최대공약수 구하기
def getGCM(A, B):
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B

    return B

# 초기값 선언
INF = 2000000001
ab = LCD // GCM # 두 서로소의 곱 구하기
a, b = 0, 0
min_value = INF

# 합이 최소인 서로소 구하기
for i in range(1, int(ab**(1/2))+1):
    if ab % i != 0: continue
    a_, b_ = i, ab//i
    if getGCM(a_, b_) != 1: continue
    if a_+b_ < min_value:
        a, b = a_, b_
        min_value = a_+b_

# 출력부
print(f"{a*GCM} {b*GCM}")