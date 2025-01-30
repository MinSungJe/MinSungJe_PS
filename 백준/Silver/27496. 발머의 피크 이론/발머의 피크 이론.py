# 입력부
N, L = map(int, input().split())
alcohols = list(map(int, input().split()))

# 누적합 리스트 구하기
sum_list = [0 for _ in range(N)]
sum_list[0] = alcohols[0]
for i in range(1, N): sum_list[i] = sum_list[i-1] + alcohols[i]
sum_list = [0] + sum_list

# 슬라이딩 윈도우
result = 0
for right in range(1, N+1):
    left = max(0, right-L)
    
    # 혈중 알코올 농도 확인
    C = (sum_list[right] - sum_list[left]) * 0.001
    if C >= 0.129 and C <= 0.138: result += 1

# 출력부
print(result)