# 모듈 불러오기
from collections import defaultdict

# TC
T = int(input())
for test_case in range(T):
    # 입력부
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    # default dict 만들기
    note_dict = defaultdict(int)

    # note1 입력
    for i in range(N): note_dict[note1[i]] = 1

    # note2 값 확인 및 출력부
    for i in range(M): print(1 if note_dict[note2[i]] else 0)