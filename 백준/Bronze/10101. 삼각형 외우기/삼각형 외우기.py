angles = [int(input()) for _ in range(3)]

def check_triangle(angles):
    if sum(angles) != 180: return 'Error'
    angle_set = set(angles)
    if len(angle_set) == 1: return 'Equilateral'
    if len(angle_set) == 2: return 'Isosceles'
    if len(angle_set) == 3: return 'Scalene'

print(check_triangle(angles))