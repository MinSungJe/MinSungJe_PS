# 입력부
N = int(input())
tips = [int(input()) for _ in range(N)]

# 팁 정렬
tips.sort(reverse=True)

# 결과 도출 및 출력부
answer = 0
for i in range(N): answer += max(0, tips[i] - i)
print(answer)