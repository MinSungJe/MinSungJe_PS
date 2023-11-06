# 입력부
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
cmd = list(map(int, input().split()))

# 초기값 선언
result = [0 for _ in range(M)]

# 카드 크기순 정렬
cards.sort()

# 이분탐색 알고리즘
def BS(target):
    l = 0
    r = N-1
    while l <= r:
        m = (l+r)//2

        if cards[m] > target:
            r = m-1

        if cards[m] == target:
            return True
            
        if cards[m] < target:
            l = m+1
    return False

# 검사
for i in range(M):
    if BS(cmd[i]): result[i] = 1

# 출력부
print(*result)