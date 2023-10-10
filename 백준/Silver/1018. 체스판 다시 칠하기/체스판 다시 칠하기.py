# Save inputs
r,c = map(int,input().split())
board = [input() for _ in range(r)]

# Make answer boards
aboard1 = []
aboard2 = []
for i in range(8):
    aboard1.append('WBWBWBWB' if i % 2 == 0 else 'BWBWBWBW')
    aboard2.append('BWBWBWBW' if i % 2 == 0 else 'WBWBWBWB')

# Declare components
pos1 = [[i,j] for i in range(8) for j in range(8)]
pos2 = [[i,j] for i in range(r-7) for j in range(c-7)]
defects = []

# Compare between answer boards and inputs
for i,j in pos2:
    defect1 = 0
    defect2 = 0
    for k,l in pos1:
        if board[i+k][j+l] != aboard1[k][l]:
            defect1 += 1
        if board[i+k][j+l] != aboard2[k][l]:
            defect2 += 1
    defects.append(defect1)
    defects.append(defect2)
print(min(defects))