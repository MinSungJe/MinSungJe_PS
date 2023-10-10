letter = input().upper()
dic = {}

for i in letter:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

count = 0
result = ''
for i in dic:
    if dic[i] > count:
        result = i
        count = dic[i]
        
    elif dic[i] == count:
        result = '?'

print(result)