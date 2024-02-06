# 입력부
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 층에 블럭이 있는지 확인하는 함수
def checkRow(floor):
    result = [0 for _ in range(W)]
    for i in range(W):
        if blocks[i] >= floor: result[i] = 1
    
    return result

# 아래층부터 확인
result = 0
for i in range(1, H+1):
    row = checkRow(i)
    isWall = False
    water = 0
    for j in range(W):
        if isWall:
            if row[j] == 0: water += 1
            if row[j] == 1:
                result += water
                water = 0
        else:
            if row[j] == 1: isWall = True

# 출력부
print(result)