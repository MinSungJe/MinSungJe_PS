function solution(numbers, target) {    
    // DFS 함수 정의
    function DFS(idx, value) {
        // 탐색 종료(최대 깊이까지 탐색함)
        if (idx === numbers.length) {
            if (value === target) return 1;
            return 0;
        }
        
        // 다음 탐색
        let answer = 0;
        for (let multiplyer of [-1, 1]) {
            const value_ = value + multiplyer * numbers[idx];
            answer += DFS(idx+1, value_)
        }
        
        return answer;
    }
    
    // 함수 호출
    var answer = DFS(0, 0)
    
    return answer;
}