function solution(number) {
    var answer = 0;
    
    // 삼총사 지정
    for (let i=0; i<number.length-2; i++) {
        for (let j=i+1; j<number.length-1; j++) {
            for (let k=j+1; k<number.length; k++) {
                // 합쳐서 0인지 확인
                if (number[i] + number[j] + number[k] === 0) answer += 1
            }
        }
    }
    
    return answer;
}