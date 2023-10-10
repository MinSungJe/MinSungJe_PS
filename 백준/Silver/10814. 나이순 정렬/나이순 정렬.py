T = int(input())
member = []
for tc in range(1,T+1):
    member.append(list(input().split()))

member.sort(key=lambda x:int(x[0]))
   
for i in range(len(member)):
    print(*member[i])