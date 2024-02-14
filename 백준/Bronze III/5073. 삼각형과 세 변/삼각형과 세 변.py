# 입력부
while True:
    lines = list(map(int, input().split()))
    lines.sort()

    if not sum(lines): break # 종료

    # Invaild 조건 확인
    if lines[2] >= lines[0] + lines[1]:
        print("Invalid")
        continue
    
    # 나머지 조건 확인
    if len(set(lines)) == 1: print("Equilateral")
    if len(set(lines)) == 2: print("Isosceles")
    if len(set(lines)) == 3: print("Scalene")