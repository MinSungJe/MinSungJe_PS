w, h, d = map(int, input().split())

width = (w-2*d)
height = (h-2*d)
result = width * height

print(result if width > 0 and height > 0 else 0)