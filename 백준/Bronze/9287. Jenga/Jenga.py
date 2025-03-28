# 무너지지 않는 row인지 확인
def isStanding(row):
    if row == "000": return False
    if row == "001": return False
    if row == "100": return False

    return True

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    height = int(input())
    blocks = [str(input()) for _ in range(height)]

    # 무너지지 않는 젠가인지 확인
    result = True
    for row in blocks:
        if not isStanding(row): result = False
    
    # 출력부
    print(f"Case {test_case}: {'Standing' if result else 'Fallen'}")