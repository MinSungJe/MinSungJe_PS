# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 앵무새 정보 입력
parrot = list()
state = [0 for _ in range(N)]
max_state = list()
for _ in range(N):
    temp = input().split()
    parrot.append(temp)
    max_state.append(len(temp))

# 앵무새의 문장 확인
result = 'Possible'
sentence = input().split()
for i in range(len(sentence)):
    speak = False
    for j in range(N):
        if state[j] == max_state[j]: continue
        if sentence[i] == parrot[j][state[j]]:
            speak = True
            state[j] += 1
            break
    
    if not speak:
        result = 'Impossible'
        break

# 출력부
print(result if sum(state) == sum(max_state) else 'Impossible')