# 진화시킬 수 있는 양을 구하는 함수
def getEvolveCount(K, M):
    result = 0
    while M >= K:
        result += 1
        M -= K
        M += 2
    
    return result

# 입력부
N = int(input())
sum_value = 0
result_value = 0
result_name = ''
for _ in range(N):
    P = input()
    K, M = map(int, input().split())
    value = getEvolveCount(K, M)
    sum_value += value

    # 가장 많이 진화시킬 수 있는 경우 기록
    if value > result_value:
        result_value = value
        result_name = P

# 출력부
print(sum_value)
print(result_name)