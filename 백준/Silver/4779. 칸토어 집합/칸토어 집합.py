# 분할 정복
def kantore(length):
    # 분할 완료
    if length == 1:
        print('-', end='')
        return

    # 분할
    kantore(length//3)
    print(' '*(length//3), end='')
    kantore(length//3)


while True:
    try:
        # 입력부
        N = int(input())
        kantore(3**N)
        print()
    except:
        break