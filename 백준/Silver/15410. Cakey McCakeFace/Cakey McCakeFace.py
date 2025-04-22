from collections import Counter

N = int(input())
M = int(input())
entry_detector = list(map(int, input().split()))
exit_detector = list(map(int, input().split()))

gap_counter = Counter()

exit_set = set(exit_detector)

# 모든 가능한 gap의 빈도를 계산
for entry_time in entry_detector:
    for exit_time in exit_detector:
        if entry_time <= exit_time:
            gap = exit_time - entry_time
            gap_counter[gap] += 1

# 최댓값 가지는 gap 찾기
result = 0
max_value = 0
for gap, count in gap_counter.items():
    if count > max_value or (count == max_value and gap < result):
        max_value = count
        result = gap

print(result)