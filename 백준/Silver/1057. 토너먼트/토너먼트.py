# 입력부
N, A, B = map(int, input().split())

# 결과 계산
result = 0

# 다음 라운드 진출
while A != B:
    A = ((A-1)//2)+1
    B = ((B-1)//2)+1

    result += 1

# 출력부
print(result)