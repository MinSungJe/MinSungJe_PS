letter = input()
record = [0 for _ in range(123)]
for l in letter:
    idx = ord(l)
    record[idx] += 1
print(*record[97:123])