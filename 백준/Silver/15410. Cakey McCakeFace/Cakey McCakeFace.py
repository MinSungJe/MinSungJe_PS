# 입력부
N = int(input())
M = int(input())
entry_detector = list(map(int, input().split()))
exit_detector = list(map(int, input().split()))

# 초기값 선언
gap_count = dict()

# N과 M 사이 차이값 후보 구하기
for entry_time in entry_detector:
    for exit_time in exit_detector:
        if entry_time > exit_time: continue
        gap = exit_time - entry_time
        if gap in gap_count.keys(): gap_count[gap] += 1
        else: gap_count[gap] = 1

# 결과값 구하기
result = 0
max_value = 0
for key, value in gap_count.items():
    if value < max_value: continue
    if max_value == value and result < key: continue
    
    # 갱신
    max_value = value
    result = key

# 출력부
print(result)