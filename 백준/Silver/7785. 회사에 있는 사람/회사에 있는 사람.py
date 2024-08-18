# 빠른 입력 및 모듈 불러오기
from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
enter_list = defaultdict(bool)

# 출입 기록
for _ in range(n):
    name, status = input().split()

    if status == 'enter': enter_list[name] = True
    if status == 'leave': enter_list[name] = False

# 출력부
idx = list(enter_list.keys())
idx.sort(reverse=True)
for name in idx:
    if enter_list[name]: print(name)