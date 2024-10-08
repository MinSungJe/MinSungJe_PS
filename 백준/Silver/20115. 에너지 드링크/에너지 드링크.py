# 입력부
N = int(input())
drinks = list(map(int, input().split()))

# 음료 정렬
drinks.sort()

# 가장 양이 많은 음료에 나머지 음료 반절 넣기
result = drinks[N-1]
for i in range(N-1): result += (drinks[i] / 2)

# 출력부
print(result)