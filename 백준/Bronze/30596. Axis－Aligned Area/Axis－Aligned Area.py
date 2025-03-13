line = [int(input()) for _ in range(4)]

# 최댓값 구하기
result = 0

result = max(result, min(line[0], line[1]) * min(line[2], line[3]))
result = max(result, min(line[0], line[2]) * min(line[1], line[3]))
result = max(result, min(line[0], line[3]) * min(line[1], line[2]))

print(result)