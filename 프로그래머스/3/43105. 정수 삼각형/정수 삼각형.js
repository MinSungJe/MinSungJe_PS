function solution(triangle) {    
    // 초기값 선언
    const maxRow = triangle.length;
    
    // DP 배열 선언
    const DP = new Array(maxRow).fill(null).map(() => new Array(maxRow).fill(-1));
    
    // Bottom-Up DP
    for (let row=maxRow-1; row>=0; row--) {        
        for (let idx=0; idx<=row; idx++) {
            // 맨 아랫줄인 경우 자기 자신값만 기록
            if (row === maxRow-1) {
                DP[row][idx] = triangle[row][idx];
                continue;
            }
            
            // 그렇지 않으면 계산
            let result = 0;
            for (let idx_ of [idx, idx+1]) {
                result = Math.max(result, triangle[row][idx]+DP[row+1][idx_])
            }
            DP[row][idx] = result;
        }
    }

    // DP 배열로 답을 얻어냄
    var answer = DP[0][0];
    
    return answer;
}