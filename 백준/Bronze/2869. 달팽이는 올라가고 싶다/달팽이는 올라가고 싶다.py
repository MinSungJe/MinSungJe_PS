numlist = list(map(int,input().split()))
print(int((numlist[2] - numlist[1]) / (numlist[0] - numlist[1])) if (numlist[2] - numlist[1]) % (numlist[0] - numlist[1]) == 0 else int(((numlist[2] - numlist[1]) // (numlist[0] - numlist[1])) + 1))
