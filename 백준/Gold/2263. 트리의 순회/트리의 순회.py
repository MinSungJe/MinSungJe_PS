# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
preOrder = list()

# 위치 정보 기록
position = [0 for _ in range(n+1)]
for i in range(n):
    position[inOrder[i]] = i

# 분할 정복
def sol(inLeft, inRight, postLeft, postRight):
    # 루트 노드, 인덱스 찾기
    root = postOrder[postRight-1]
    rootIdx = position[root]

    # preOrder: 탐색
    preOrder.append(root)

    # 분할되는 크기 구하기
    leftSize = rootIdx - inLeft
    rightSize = inRight - (rootIdx+1)

    if leftSize > 0: sol(inLeft, inLeft+leftSize, postLeft, postLeft+leftSize)
    if rightSize > 0: sol(inRight-rightSize, inRight, (postRight-1)-rightSize, postRight-1)

# 함수 호출
sol(0, n, 0, n)

# 출력부
print(*preOrder)