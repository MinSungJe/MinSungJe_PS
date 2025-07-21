# TC
T = int(input())

for i in range(T):
    # 입력부
    lines = list(map(int, input().split()))

    # 정렬
    lines.sort()

    # 결과 도출 및 출력부
    answer = lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2
    print(f'Scenario #{i+1}:')
    print('yes' if answer else 'no')
    if i != T-1: print()