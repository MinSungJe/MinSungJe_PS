N = int(input())
for _ in range(N):
    name, score_string = input().split()
    score = int(score_string)
    
    
    if score >= 97:
        print(f"{name} A+")
        continue
    if score >= 90:
        print(f"{name} A")
        continue
    if score >= 87:
        print(f"{name} B+")
        continue
    if score >= 80:
        print(f"{name} B")
        continue
    if score >= 77:
        print(f"{name} C+")
        continue
    if score >= 70:
        print(f"{name} C")
        continue
    if score >= 67:
        print(f"{name} D+")
        continue
    if score >= 60:
        print(f"{name} D")
        continue
        
    print(f"{name} F")