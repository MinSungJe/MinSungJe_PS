# 입력부
N = int(input())
count = 0
canPrint = False

def hanoi(n, start, end):
    global count

    # 분할 완료
    if n == 1:
        count += 1
        if canPrint: print(start, end)
        return

    hanoi(n-1, start, 6-(start+end))
    hanoi(1, start, end)
    hanoi(n-1, 6-(start+end), end)

# 출력부
hanoi(N, 1, 3)
print(count) # (=2^N -1)
canPrint = True
hanoi(N, 1, 3)