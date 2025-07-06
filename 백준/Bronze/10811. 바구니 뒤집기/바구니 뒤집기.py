# 입력부
N, M = map(int, input().split())

# 바구니 선언
answer = [i+1 for i in range(N)]

# 뒤집기 명령 실행
for _ in range(M):
    i, j = map(int, input().split())
    
    # 바구니 뒤집기
    length = j-i
    for d in range(0, length//2+1):
        idx = i-1+d

        # 서로 뒤집기
        temp = answer[idx]
        answer[idx] = answer[j-1-d]
        answer[j-1-d] = temp

# 출력부
print(*answer)