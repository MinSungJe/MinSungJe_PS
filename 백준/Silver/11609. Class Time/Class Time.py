# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
students = [input().split() for _ in range(n)]

# 학생 정렬
students.sort(key=lambda x: (x[1], x[0]))

# 출력부
for studentList in students: print(' '.join(studentList))