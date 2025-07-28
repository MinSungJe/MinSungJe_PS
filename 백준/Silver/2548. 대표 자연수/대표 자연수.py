# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 정렬
numbers.sort()

# 출력부
answer = numbers[(N+1)//2 - 1]
print(answer)