# 입력부
while True:
    query = input().split()

    # 종료
    if query[0] == '#': break
    sentence = ''.join(query[1:])

    # 결과 계산
    result = 0
    for letter in sentence:
        if query[0] == letter.lower(): result += 1

    # 출력부
    print(f"{query[0]} {result}")