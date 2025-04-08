# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 중간값 모두 구하기
result = list()
middle_idx = N // 2
for i in range(N):
    Map[i].sort()
    result.append(Map[i][middle_idx])

# 결과 도출 및 출력부
result.sort()
print(result[middle_idx])