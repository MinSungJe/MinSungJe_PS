# 모듈 불러오기
from collections import defaultdict

# 입력부
letter = input()

# 초기값 선언
a_list = defaultdict(int)

# 글자 개수 세기
for l in letter: a_list[l] += 1


# 팰린드롬이 가능한지 확인하는 함수
def canPD(l):
    result = 0
    for k in l.keys():
        if a_list[k] % 2 == 1: result += 1
    
    if result > 1: return False
    return True

# 팰린드롬 가능한지 검사
if not canPD(a_list): print("I'm Sorry Hansoo")
else:
    result = ''
    # 문자순으로 배열해서 넣기
    sorted_a_list = list(a_list.keys())
    sorted_a_list.sort()
    for a in sorted_a_list:
        for _ in range(a_list[a] // 2): result += a
    
    # 홀수인 문자 찾아서 넣기
    for k in a_list.keys():
        if a_list[k] % 2 == 1: result += k
    
    # 문자 역순으로 넣기
    sorted_a_list.sort(reverse=True)
    for a in sorted_a_list:
        for _ in range(a_list[a] // 2): result += a

    # 출력부
    print(result)