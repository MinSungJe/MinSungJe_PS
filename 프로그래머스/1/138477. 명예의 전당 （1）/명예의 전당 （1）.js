function solution(k, score) {
    var answer = [];
    
    // 발표된 가수의 점수를 담는 배열 선언
    const current = [];
    
    // 가수 점수 넣으면서 확인
    for (let oneScore of score) {
        current.push(oneScore);
        
        // 정렬
        current.sort((a, b) => b - a);
        
        // 명예의 전당 목록
        const specialList = current.slice(0,k);
        
        // 최하위 점수 넣기
        answer.push(specialList[specialList.length - 1]);
    }
    
    return answer;
}