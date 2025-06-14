function solution(k, m, score) {
    var answer = 0;
    
    // 점수 정렬
    score.sort((a, b) => a - b);
    
    // 사과 박스 나누기
    while (true) {
        // 종료
        if (score.length < m) break;
        
        // 사과박스 나누기
        const box = []
        for (let i=0; i<m; i++) 
            box.push(score.pop())
        
        // 사과박스 이익 더하기
        answer += Math.min(...box) * m
    }
    
    return answer;
}