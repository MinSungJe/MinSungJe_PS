function solution(numbers, hand) {
    var answer = '';
    
    // 중간 번호 거리 구하는 함수
    function getDistance(current, target) {
        if (target === 2) {
            if (current === -1) return 4;
            if (current === -2) return 4;
            if (current === 0) return 3;
            if (current === 1) return 1;
            if (current === 2) return 0;
            if (current === 3) return 1;
            if (current === 4) return 2;
            if (current === 5) return 1;
            if (current === 6) return 2;
            if (current === 7) return 3;
            if (current === 8) return 2;
            if (current === 9) return 3;
        }
        
        if (target === 5) {
            if (current === -1) return 3;
            if (current === -2) return 3;
            if (current === 0) return 2;
            if (current === 1) return 2;
            if (current === 2) return 1;
            if (current === 3) return 2;
            if (current === 4) return 1;
            if (current === 5) return 0;
            if (current === 6) return 1;
            if (current === 7) return 2;
            if (current === 8) return 1;
            if (current === 9) return 2;
        }
        
        if (target === 8) {
            if (current === -1) return 2;
            if (current === -2) return 2;
            if (current === 0) return 1;
            if (current === 1) return 3;
            if (current === 2) return 2;
            if (current === 3) return 3;
            if (current === 4) return 2;
            if (current === 5) return 1;
            if (current === 6) return 2;
            if (current === 7) return 1;
            if (current === 8) return 0;
            if (current === 9) return 1;
        }
        
        if (target === 0) {
            if (current === -1) return 1;
            if (current === -2) return 1;
            if (current === 0) return 0;
            if (current === 1) return 4;
            if (current === 2) return 3;
            if (current === 3) return 4;
            if (current === 4) return 3;
            if (current === 5) return 2;
            if (current === 6) return 3;
            if (current === 7) return 2;
            if (current === 8) return 1;
            if (current === 9) return 2;
        }
    }
    
    // 손 위치 저장
    let left = -1;
    let right = -2;
    
    // 손 이동
    for (let number of numbers) {
        // 숫자를 누르는 손가락이 정해진 경우
        if (number === 1 || number === 4 || number === 7) {
            left = number;
            answer += 'L';
            continue;
        }
        
        if (number === 3 || number === 6 || number === 9) {
            right = number;
            answer += 'R';
            continue;
        }
        
        // 숫자를 누르는 손가락이 정해지지 않은 경우
        const leftDistance = getDistance(left, number);
        const rightDistance = getDistance(right, number);
        
        if (leftDistance === rightDistance) {
            if (hand === 'left') {
                answer += 'L';
                left = number;
            }
            if (hand === 'right') {
                answer += 'R';
                right = number;
            }
            continue;
        }
        
        if (leftDistance < rightDistance) {
            answer += 'L';
            left = number;
        }
        
        if (rightDistance < leftDistance) {
            answer += 'R';
            right = number;
        }
        
    }
    
    return answer;
}