# 입력부
N = int(input())

# 초기값 선언
results = list()
shortcut = list()

# 단축키 찾기
for _ in range(N):
    option = input()

    # 추가됐는지 확인하는 변수
    isAdded = False

    # 1번 지정
    words = option.split()
    for i in range(len(words)):
        word = words[i]
        target = word[0].upper()

        # 단축키 추가
        if not target in shortcut:
            shortcut.append(target)
            words[i] = f"[{word[0]}]{word[1:]}"
            isAdded = True
            break
    
    # 단축키 추가된 상태라면 종료
    if isAdded:
        results.append(' '.join(words))
        continue

    # 2번 지정
    for i in range(len(option)):
        target = option[i].upper()
        if target == ' ': continue
        
        # 단축키 추가
        if not target in shortcut:
            shortcut.append(target)
            results.append(f"{option[:i]}[{option[i]}]{option[i+1:]}")
            isAdded = True
            break
    
    # 단축키가 추가되지 않은 상태라면 결과에 그대로 반영
    if not isAdded: results.append(option)

# 출력부
for result in results: print(result)