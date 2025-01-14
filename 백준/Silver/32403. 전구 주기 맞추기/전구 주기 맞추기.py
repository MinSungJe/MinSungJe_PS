# 입력부
N, T = map(int, input().split())
a = list(map(int, input().split()))

# 이분 탐색을 위한 정렬
a.sort()

# 약수 리스트 구하는 함수
def findYaksu(number):
    result = list()

    for i in range(1, number+1):
        if number % i == 0: result.append(i)

    return result

# 이분탐색 함수
def BS(number):
    start = 0
    end = len(yaksu)-1
    result = 0

    while start < end:
        mid = (start+end+1) // 2

        if yaksu[mid] <= number:
            result = mid
            start = mid
        else:
            end = mid-1
    
    return result

# 약수 리스트 구하기
yaksu = findYaksu(T)

# 결과 구하기
result = 0
for i in range(N):
    target = a[i]
    target_idx = BS(target)

    # 양 옆 수 중 가까운 차이값 더하기
    if target_idx == len(yaksu)-1: result += target-yaksu[target_idx]
    else: result += min(target-yaksu[target_idx], yaksu[target_idx+1]-target)

# 출력부
print(result)