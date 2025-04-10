# 입력부
burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
drink1 = int(input())
drink2 = int(input())

# 가장 싼 세트 찾기
result = 4001
result = min(result, burger1 + drink1)
result = min(result, burger2 + drink1)
result = min(result, burger3 + drink1)
result = min(result, burger1 + drink2)
result = min(result, burger2 + drink2)
result = min(result, burger3 + drink2)

# 출력부
print(result-50)