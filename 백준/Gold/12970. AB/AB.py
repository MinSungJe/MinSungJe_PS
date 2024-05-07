# 입력부
N, K = map(int, input().split())

# 초기값 선언
result = -1

# A 개수 지정
for A in range(1, N):
    # 초기값 선언
    value = list()
    B = N-A # 더할 수 있는 최댓값
    temp = K

    # 충족요건 확인
    while temp:
        if temp >= B:
            temp -= B
            value.append(B)
        else:
            B = temp

        if len(value) == A:
            break
    
    # K를 충족하지 않음
    if temp: continue

    # 해 구성하기
    if not value: value.append(0)
    letter = ['B' for _ in range(N)]
    count = 0
    for gap in value[::-1]:
        idx = N-(gap+count+1)
        letter[idx] = 'A'
        count += 1
    result = ''.join(letter)
    break

# 출력부
print(result)