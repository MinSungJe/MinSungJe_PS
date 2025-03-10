# 입력부
N = int(input())
books = list(map(int, input().split()))

# LIS(nlogn): 이분탐색 이용
DP = list()

# 이분 탐색(lower-bound)
def binarySearch(left, right, target):
    l = left
    r = right
    result = r
    while l < r:
        mid = (l+r) // 2

        if DP[mid] < target:
            l = mid+1
        if DP[mid] >= target:
            r = mid
            result = mid
    
    return result

# 책 위치 넣기
for book in books:
    if not DP or DP[-1] < book:
        DP.append(book)
        continue

    idx = binarySearch(0, len(DP)-1, book)
    DP[idx] = book

# 출력부
result = N - len(DP)
print(result)