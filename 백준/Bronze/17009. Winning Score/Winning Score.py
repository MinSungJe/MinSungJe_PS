appleResult = 0
bananaResult = 0

for m in (3,2,1):
    appleResult += m*int(input())
for m in (3,2,1):
    bananaResult += m*int(input())

if appleResult > bananaResult: print('A')
if appleResult < bananaResult: print('B')
if appleResult == bananaResult: print('T')