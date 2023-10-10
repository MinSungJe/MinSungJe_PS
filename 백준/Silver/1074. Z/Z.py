def Z(r, c, length):
    global index, result
    # 분할 완료
    if length == 2:
        for i in range(4):
            if dx[i] == r and dy[i] == c:
                result = index
            index += 1
        return
    
    # 새로 X, Y, r, c 지정
    length_ = length // 2
    r_ = r // length_
    c_ = c // length_

    if r_ == 0 and c_ == 1:
        index += length_ * length_
    if r_ == 1 and c_ == 0:
        index += 2 * length_ * length_
    if r_ == 1 and c_ == 1:
        index += 3 * length_ * length_
    Z(r-(r_*length_), c-(c_*length_), length_)


N, r, c = map(int, input().split())
length = 2 ** N
index = 0
result = 0
dx = [0,0,1,1]
dy = [0,1,0,1]
Z(r,c,length)

print(result)