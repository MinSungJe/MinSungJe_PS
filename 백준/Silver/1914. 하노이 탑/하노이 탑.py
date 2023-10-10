# 입력부
N = int(input())
def hanoi(n, start, end):

    # 분할 완료
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, 6-(start+end))
    hanoi(1, start, end)
    hanoi(n-1, 6-(start+end), end)

# 출력부
print(2**N - 1) # (=2^N -1)
if not N > 20: hanoi(N, 1, 3)