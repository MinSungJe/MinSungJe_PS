# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
words = [input() for _ in range(N)]

# 그룹 단어인지 체크하는 함수
def check_is_group_word(idx, prev):
    if idx == len(word): return True

    # 초기값 선언
    letter = ord(word[idx])

    # 다음 탐색
    result = True if not visited[letter] or letter == prev else False
    visited[letter] = True # 탐색
    result *= check_is_group_word(idx+1, letter)

    return result
    
# 단어 별 확인
answer = 0
for word in words:
    visited = [False for _ in range(123)]
    if check_is_group_word(0, ''): answer += 1


# 출력부
print(answer)