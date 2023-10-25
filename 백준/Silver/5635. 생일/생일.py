# 입력부
n = int(input())

# 초기값 선언
List = []

# 리스트 채우기
for _ in range(n):
    name, day, month, year = input().split()
    List.append([int(year), int(month), int(day), name])

# 정렬
List.sort(key=lambda x:(x[0],x[1],x[2]))

# 출력부
print(List[-1][3])
print(List[0][3])