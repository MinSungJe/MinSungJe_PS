# 입력부
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# x좌표 구하기
if t <= w-p: p += t
else:
    rest_t = t - (w-p)
    if (rest_t // w) % 2 == 0: p = w - (rest_t % w)
    else: p = (rest_t % w)

# y좌표 구하기
if t <= h-q: q += t
else:
    rest_t = t - (h-q)
    if (rest_t // h) % 2 == 0: q = h - (rest_t % h)
    else: q = (rest_t % h)

# 출력부
print(p, q)