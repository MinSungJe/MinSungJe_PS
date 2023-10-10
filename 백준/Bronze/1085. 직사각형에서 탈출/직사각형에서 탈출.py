x,y,w,h = map(int,input().split())
distances = [x,y]
distances.append(w-x)
distances.append(h-y)
print(min(distances))