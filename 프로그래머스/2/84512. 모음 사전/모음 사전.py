def solution(word):
    answer = 0
    
    # 초기값 선언
    letter = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    def DFS(word):
        # 탐색
        dictionary.append(word)
        
        # 탐색 종료
        if len(word) == 5:
            return;
        
        # 다음 탐색
        for l in letter: DFS(word+l)
    
    # 함수 호출 및 출력부
    DFS('')
    for i in range(len(dictionary)):
        if dictionary[i] == word:
            answer = i
            break
    return answer