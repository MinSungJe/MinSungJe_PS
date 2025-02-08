# 입력부
N = int(input())
letter = input()

# 해당 idx가 로또에 당첨됐는지 확인하는 함수
def checkIsWinning(letter, idx):
    # 처음 문자 코드 저장
    prev = ord(letter[idx])

    # 다음 4번동안 확인
    for i in range(1, 5):
        # 5개를 검사할 수 없음
        if idx+i >= len(letter): return False

        # 인접한 문자인지 확인
        current = ord(letter[idx+i])
        if abs(prev-current) != 1: return False
        prev = current
        
    return True


# 함수 호출 및 출력부
result = 0
for i in range(N):
    if checkIsWinning(letter, i): result += 1
print("YES" if result else "NO")