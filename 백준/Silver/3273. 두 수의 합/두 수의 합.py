# 입력부
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

# 숫자 정렬
numbers.sort()

# 투 포인터
result = 0
l, r = 0, n-1
while l < r:
    value = numbers[l]+numbers[r]
    
    # 값이 큰 경우, r을 한칸 땡김
    if value > x:
        r -= 1
        continue
    
    # 값이 같은 경우, result 추가함
    if value == x:
        result += 1
    
    # 크지않은 경우 l을 한칸 땡김
    l += 1

# 출력부
print(result)