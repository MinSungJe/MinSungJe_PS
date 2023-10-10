T = int(input())
for tc in range(1,T+1):
    R,S = input().split()
    for letter in S:
        print(letter * int(R), end = '')
    print('')