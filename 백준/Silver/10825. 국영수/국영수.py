# 입력 변환하기
def parse_integer(letter):
    if letter.isdigit(): return int(letter)
    return letter

# 입력부
N = int(input())
students = [list(map(parse_integer, input().split())) for _ in range(N)]

# 정렬
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력부
for student in students: print(student[0])