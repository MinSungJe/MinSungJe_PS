# 푼 문제 데이터
data = [
    [],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'I', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'I', 'L', 'M'],
    ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M'],
    ['A', 'B', 'C', 'F', 'G', 'H', 'L', 'M'],
]

# 입력부
N = int(input())

# 출력부
print(len(data[N]))
print(*data[N])