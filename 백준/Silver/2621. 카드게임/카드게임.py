# 입력부
def divide_type(letter):
    try: return int(letter)
    except: return letter
cards = [list(map(divide_type, input().split())) for _ in range(5)]

# 플러시 체크
def check_flush():
    return len(set([card[0] for card in cards])) == 1

# 스트레이트 체크
def check_straight():
    numbers = [card[1] for card in cards]
    numbers.sort()
    prev = numbers[0]
    result = True
    for i in range(1, 5):
        number = numbers[i]
        if prev+1 != number: result = False
        prev = number
    
    return result

# 같은 카드 정보 얻기
def get_same():
    result = [0 for _ in range(10)]
    numbers = [card[1] for card in cards]
    for number in numbers: result[number] += 1
    return result

# 스트레이트 플러쉬 점수 얻기
def get_straight_flush():
    result = 0
    if check_flush() and check_straight(): result = max([card[1] for card in cards]) + 900
    return result

# 포카드 점수 얻기
def get_four_cards():
    result = 0
    info = get_same()
    if max(info) == 4:
        for number in range(10):
            if info[number] == 4: result = 800 + number
    return result

# 풀하우스 점수 얻기
def get_full_house():
    result = 0
    info = get_same()
    if 3 in set(info) and 2 in set(info):
        for number in range(10):
            if info[number] == 3: result += 10 * number
            if info[number] == 2: result += 700 + number
    return result

# 플러쉬 점수 얻기
def get_flush():
    result = 0
    if check_flush(): result = max([card[1] for card in cards]) + 600
    return result

# 스트레이트 점수 얻기
def get_straight():
    result = 0
    if check_straight(): result = max([card[1] for card in cards]) + 500
    return result

# 트리플 점수 얻기
def get_triple():
    result = 0
    info = get_same()
    if max(info) == 3:
        for number in range(10):
            if info[number] == 3: result = 400 + number
    return result

# 페어 관련 점수 얻기
def get_pairs():
    result = 0
    info = get_same()
    if max(info) == 2:
        pair_index = list()
        for number in range(10):
            if info[number] == 2: pair_index.append(number)
        
        # 투페어
        if len(pair_index) == 2:
            result += max(pair_index) * 10
            result += min(pair_index) + 300

        # 원페어
        if len(pair_index) == 1:
            result = pair_index[0] + 200
                    
    return result

# 탑 카드 점수 얻기
def get_top_card():
    result = 0
    info = get_same()
    if max(info) == 1:
        for number in range(9, -1, -1):
            if info[number] == 1:
                result = 100 + number
                break
    return result

# 함수 호출 및 출력부
result = max(get_straight_flush(), get_four_cards(), get_full_house(), get_flush(), get_straight(), get_triple(), get_pairs(), get_top_card())
print(result)