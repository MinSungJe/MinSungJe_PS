def solution(arr):
    prev = -1
    answer = []
    for number in arr:
        if number != prev: answer.append(number)
        prev = number
    
    
    return answer