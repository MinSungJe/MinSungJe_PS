# 모듈 불러오기
import bisect

# 입력부
N = int(input())
crains = sorted(list(map(int, input().split())))
M = int(input())
boxes = sorted(list(map(int, input().split())))

# 초기값 선언
result = 0

if crains[-1] < boxes[-1]: print(-1) # 만약 크레인으로 옮길 수 없는 박스가 있다면, -1 출력
else:
    while boxes: # 박스가 없어질 때까지 반복문 실행
        result += 1
        for crain in crains: # 크레인마다 반복
            if not boxes: break # 박스가 없다면 종료
            # 박스를 크레인으로 옮길 수 있을때만 박스 제거
            if crain >= boxes[bisect.bisect_right(boxes, crain)-1]: del boxes[bisect.bisect_right(boxes, crain)-1]
    
    # 출력부
    print(result)