# 입력부
N = int(input())
juon = list(map(int, input().split()))
sajang = list(map(int, input().split()))

# 카드 정렬
juon.sort()
sajang.sort()

# 게임
threshold = int((N+1)/2)
result = 0
for i in range(threshold):
    if juon[i] < sajang[threshold-1+i]: result += 1

# 출력부
print("YES" if result >= threshold else "NO")