Ax, Ay, Az = map(int, input().split())
Cx, Cy, Cz = map(int, input().split())

Bx = Cx - Az
By = Cy // Ay
Bz = Cz - Ax

print(Bx, By, Bz)