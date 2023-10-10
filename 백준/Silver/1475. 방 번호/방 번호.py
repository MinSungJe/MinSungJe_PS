# 입력부
N = input()

# 초기 배열 선언
nums = [0 for _ in range(10)]

# 배열에 값 채우기
for num in N:
    nums[int(num)] += 1

# nums 재정립 (6이랑 9는 같은 숫자임)
if (nums[6] + nums[9]) % 2 == 0:
    nums[6] = ((nums[6] + nums.pop()) // 2)
else:
    nums[6] = ((nums[6] + nums.pop()) // 2) + 1

# 출력부
print(max(nums))