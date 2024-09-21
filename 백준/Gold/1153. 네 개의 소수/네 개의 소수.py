# 입력부
N = int(input())

# 초기값 선언
INF = 1000001

# 에라토스테네스의 체
sosu = [True for _ in range(INF)]
sosu[0] = False
sosu[1] = False
for num in range(2, INF):
    if not sosu[num]: continue
    for i in range(2*num, INF, num): sosu[i] = False

# 결과값 도출
result = '-1'
if N >= 8:
    if N % 2 == 0:
        temp = [2, 2]
        for i in range(N-4, 1, -1):
            if sosu[i] and sosu[N-4-i]:
                temp.append(i)
                temp.append(N-4-i)
                result = ' '.join(sorted(map(str, temp)))
                break
    else:
        temp = [2, 3]
        for i in range(N-5, 1, -1):
            if sosu[i] and sosu[N-5-i]:
                temp.append(i)
                temp.append(N-5-i)
                result = ' '.join(sorted(map(str, temp)))
                break

# 출력부
print(result)