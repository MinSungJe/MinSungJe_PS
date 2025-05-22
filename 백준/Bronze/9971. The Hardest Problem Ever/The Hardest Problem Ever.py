# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
while True:
    start = input()
    if start == 'ENDOFINPUT': break # 종료

    message = input()
    end = input()

    # 해석
    result = ''
    for letter in message:
        value = ord(letter)
        if value < 65 or value > 90: result += letter
        elif value >= 70: result += chr(value - 5)
        else: result += chr(value + 21)
    
    # 출력부
    print(result)