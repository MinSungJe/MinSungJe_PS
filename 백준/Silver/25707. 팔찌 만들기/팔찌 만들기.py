N = int(input())
marble = list(map(int, input().split()))
print(2 * (max(marble) - min(marble)))