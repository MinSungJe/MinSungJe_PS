# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
p, m = map(int, input().split())
room = list()
for _ in range(p):
    p, n = input().split()
    p = int(p)
    isEnter = False

    # 방 탐색
    for i in range(len(room)):
        # 입장 불가 조건
        if len(room[i]) == m: continue
        if room[i][0][0] > p+10: continue
        if room[i][0][0] < p-10: continue

        # 입장
        room[i].append((p, n))
        isEnter = True
        break
    
    # 새로운 방 만들기
    if not isEnter: room.append([(p, n)])

# 출력부
for i in range(len(room)):
    # 대기 여부 출력
    print("Started!" if len(room[i]) == m else "Waiting!")
    room[i].sort(key=lambda x:x[1]) # 닉네임 순으로 정렬
    for j in range(len(room[i])): print(*room[i][j]) # 유저 출력