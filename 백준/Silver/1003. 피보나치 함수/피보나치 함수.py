# N이 40까지이므로 41까지 list를 만들어둬야 한다!
a = [0] * 41
z = [0] * 41
o = [0] * 41
outputs = []

# Dynamic Programming : 이미 계산한 것들을 다시 계산하지 말자!
def fibo(num):
    if num == 0:
        z[num] = 1
        o[num] = 0
        return 0
    if num == 1:
        z[num] = 0
        o[num] = 1
        return 1
    
    # 계산을 한번 한 경우, 그냥 넘기고
    if a[num] != 0:
        return a[num]
    # 안했으면 계산해서 값을 채워넣는다
    else:
        a[num] = fibo(num-1) + fibo(num-2)
        z[num] = z[num-1] + z[num-2]
        o[num] = o[num-1] + o[num-2]
        return a[num]

# 입력
case = int(input())
for i in range(case):
    num = int(input())
    fibo(num)
    outputs.append([z[num],o[num]])

# 출력
for i in range(len(outputs)):
    print(outputs[i][0],outputs[i][1])
