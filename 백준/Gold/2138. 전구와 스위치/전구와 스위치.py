# 입력부
N = int(input())
before = list(map(int, list(input())))
before_2 = before[:]
after = list(map(int, list(input())))

# 초기값 선언
INF = 100001
result = INF
dx = (0, -1, 1)

# 배열 만들기
for i in (0, 1):
    before_2[i] = 1-before_2[i]

# 처음 스위치를 누른 경우와 누르지 않은 경우 고려
for B in (before[:], before_2[:]):
    count = 0 if before[0] == B[0] else 1
    # 모든 버튼에 대하여 확인
    for i in range(1, N):
        # 이전 버튼의 값이 같지 않다면 버튼을 누른다
        if B[i-1] != after[i-1]:
            for d in range(3):
                i_ = i+dx[d]
                if i_ < 0 or i_ >= N: continue
                B[i_] = 1 - B[i_]
            count += 1
    # 마지막 버튼의 값 확인
    if B[N-1] == after[N-1]: result = min(result, count)

# 출력부
print(result if result < INF else -1)