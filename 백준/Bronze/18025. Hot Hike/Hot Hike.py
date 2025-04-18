# 입력부
N = int(input())
T = list(map(int, input().split()))

# 초기값 선언
d, t = 0, 41

# 하이킹 날이 가장 온도가 낮은 날 찾기
for i in range(N-2):
    hiking_temperature = max(T[i], T[i+2])
    if hiking_temperature < t:
        d = i+1
        t = hiking_temperature

# 출력부
print(d, t)