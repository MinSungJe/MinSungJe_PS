# 입력부
n = int(input())
sticks = list(map(int, input().split()))

# 쇠막대 긴 순으로 정렬
sticks.sort(reverse=True)

# 결과 도출
result = 0
stick = sum(sticks)
for m in sticks:
    stick -= m
    result += stick*m

# 출력부
print(result)