# 프린트 리스트를 읽는 함수
def get_print_range(x):
    return list(map(int, x.split('-')))

# TC
while True:
    N = int(input())

    # 종료
    if N == 0: break

    # 입력부
    print_list = list(map(get_print_range, input().split(',')))
    
    # 초기값 선언
    result = [0 for _ in range(N+1)]

    # 인쇄 범위 확인
    for print_range in print_list:
        # 범위가 없는 경우
        if len(print_range) == 1:
            idx = print_range[0]
            if idx > N: continue
            result[idx] = 1
            continue

        # 범위가 있는 경우
        start, end = print_range
        if start > end: continue
        for i in range(start, min(end+1, N+1)): result[i] = 1
    
    # 출력부
    print(sum(result))