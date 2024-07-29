# 이분 탐색
def BS(target, note):
    start = 0
    end = len(note)
    while start < end:
        mid = (start + end) // 2

        if note[mid] == target: return True

        if note[mid] < target: start = mid+1
        if note[mid] > target: end = mid

    return False

# TC
T = int(input())
for test_case in range(T):
    # 입력부
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    # note1 정렬
    note1.sort()

    # note2의 값들이 note1에 있는지 이분탐색 / 출력부
    for i in range(M): print(1 if BS(note2[i], note1) else 0)