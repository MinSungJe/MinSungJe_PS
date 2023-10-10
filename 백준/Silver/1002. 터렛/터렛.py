import math
case = int(input())
inputgroup = []

for i in range(case):
    info = input().split()
    inputgroup.append(info)

for i in range(len(inputgroup)):
    # 두 점 사이의 거리 계산
    dist = math.sqrt((int(inputgroup[i][0])-int(inputgroup[i][3]))**2 + (int(inputgroup[i][1])-int(inputgroup[i][4]))**2)
    # 만약 두 점이 같을 시
    if (inputgroup[i][0] == inputgroup[i][3]) and (inputgroup[i][1] == inputgroup[i][4]):
        if inputgroup[i][2] == inputgroup[i][5]:
            print("-1")
        else:
            print("0")
        continue
    # 원이 내접하는 경우
    if (dist + int(inputgroup[i][2]) == int(inputgroup[i][5])) or (dist + int(inputgroup[i][5]) == int(inputgroup[i][2])):
        print("1")
        continue
    # 아예 원이 들어가 있는 경우
    if (dist + int(inputgroup[i][2]) < int(inputgroup[i][5])) or (dist + int(inputgroup[i][5]) < int(inputgroup[i][2])):
        print("0")
        continue
    # 두 점 사이의 거리와 반지름 둘의 합을 비교
    if dist > (int(inputgroup[i][2])+int(inputgroup[i][5])):
        print("0")
    elif dist == (int(inputgroup[i][2])+int(inputgroup[i][5])):
        print("1")
    else:
        print("2")