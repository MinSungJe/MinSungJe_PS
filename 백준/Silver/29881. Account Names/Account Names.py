# 입력부
N = int(input())

# 초기값 선언
user_info = dict()

# last name 입력받기
for _ in range(N):
    nickname, lastname = input().split()
    user_info[nickname] = [lastname]

# account name 입력받기
for _ in range(N):
    nickname, account_name = input().split()
    user_info[nickname].append(account_name)

# 출력부
for lastname, account_name in user_info.values(): print(lastname, account_name)