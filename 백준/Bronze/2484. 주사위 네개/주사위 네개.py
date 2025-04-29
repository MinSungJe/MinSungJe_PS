# 입력부
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

# 점수 확인
result = 0
for a, b, c, d in dices:
    record = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    record[a] += 1
    record[b] += 1
    record[c] += 1
    record[d] += 1

    # 값 중 최댓값과 겹친 값 구하기
    max_value = max(record.values())
    length = len(set([a,b,c,d]))

    # 경우의 수 구하기
    if max_value == 4:
        for index in (a, b, c, d):
            if record[index] == max_value: result = max(result, 50000+(index * 5000))
    if max_value == 3:
        for index in (a, b, c, d):
            if record[index] == max_value: result = max(result, 10000+(index * 1000))
    if max_value == 2:
        if length == 2:
            value = 0
            for index in (a, b, c, d):
                value += 500 * index
            result = max(result, 2000 + value // 2)
        if length == 3:
            for index in (a, b, c, d):
                if record[index] == max_value: result = max(result, 1000+(index * 100))
    if max_value == 1: result = max(result, max(a, b, c, d) * 100)

# 출력부
print(result)