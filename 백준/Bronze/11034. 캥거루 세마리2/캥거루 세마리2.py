# 입력부
while True:
    try:
        A, B, C = map(int, input().split())
        answer = 0

        while True:
            left, right = B-A, C-B
            if left == right and left == 1:
                print(answer)
                break
            
            if left <= right: tA, tB, tC = B, B+1, C
            else: tA, tB, tC = A, B-1, B

            answer += 1
            A, B, C = tA, tB, tC

    except:
        break