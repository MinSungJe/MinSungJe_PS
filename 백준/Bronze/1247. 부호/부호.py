import sys
def input(): return sys.stdin.readline().rstrip()

for _ in range(3):
    N = int(input())
    S = 0
    for _ in range(N):
        number = input()
        if number[0] == '-': S -= int(number[1:])
        else: S += int(number)
    
    answer = 0
    if S < 0: answer = '-'
    if S > 0: answer = '+'

    print(answer)