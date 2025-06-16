function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    
    // goal의 모든 내용이 없어질 때까지 확인
    while (goal.length > 0) {
        const target = goal.shift();
        
        // cards1의 맨 위에 있는지 확인
        if (target === cards1[0]) {
            cards1.shift();
            continue;
        }
        
        // cards2의 맨 위에 있는지 확인
        if (target === cards2[0]) {
            cards2.shift();
            continue;
        }
        
        // 둘 다 없을 경우 No로 바꾸고 반복문 종료
        answer = 'No';
        break;
    }
    
    return answer;
}