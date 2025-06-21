function solution(d, budget) {
    var answer = 0;
    
    // 신청한 금액이 적은 순으로 나열
    d.sort((a, b) => a - b);
    
    // 예산 최대한 나눠주기
    for (let price of d) {
        budget -= price;
        
        // 예산이 부족하면 종료
        if (budget < 0) break;
        
        // 예산을 준 경우 기록
        answer += 1;
    }
    
    return answer;
}