# 입력부
T = int(input())

# 시간을 맞출 수 없는 경우 확인
if T % 10: print(-1)
else: print(T//300, (T%300)//60, (T%60)//10)