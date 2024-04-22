# 입력부
letter = input()

# 초기값 선언
result = -1
L = len(letter)

# 회문
if letter[:L//2] == letter[L-1:((L//2)-1)+(L%2):-1]: result = L-1
else: result = L

# 특수한 경우 확인
if letter == letter[0] * L: result = -1

# 출력부
print(result)