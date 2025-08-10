# 유클리드 호제법
def GCD(A, B):
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B
    return B

first = list(map(int, input().split()))
second = list(map(int, input().split()))

win_count = 0
for i in first:
    for j in second:
        if i > j: win_count += 1

gcd = GCD(win_count, 36)
answer = f"{win_count // gcd}/{36 // gcd}"
print(answer)