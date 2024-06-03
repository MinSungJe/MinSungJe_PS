# 입력 형식 바꾸기
import sys
def input(): return sys.stdin.read() # sys.stdin.read()는 입력이 끝날 때까지 입력받음

# 입력부
N, *numbers = input().split()

# 거꾸로 뒤집기
for i in range(int(N)): numbers[i] = int(numbers[i][::-1])

# 오름차순 정렬
numbers.sort()

# 출력부
for i in range(int(N)): print(numbers[i])