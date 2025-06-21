function solution(triangle) {    
    // 초기값 선언
    const maxRow = triangle.length;
    
    // DP 배열 선언(기록용)
    const DP = new Array(maxRow).fill(null).map(() => new Array(maxRow).fill(-1));
    
    // DFS(+DP)
    function DFS(row, idx) {
        // 탐색 종료
        if (row === maxRow) return 0;
        
        // DP 배열에 이미 기록된 경우 해당 값 반환
        if (DP[row][idx] !== -1) return DP[row][idx];
        
        // 다음 탐색
        let result = 0;
        for (let idx_ of [idx, idx+1])
            result = Math.max(result, triangle[row][idx] + DFS(row+1, idx_))
        
        DP[row][idx] = result; // 메모이제이션(DP배열에 기록)
        return result;
    }
    
    // 함수 호출
    var answer = DFS(0, 0);
    
    return answer;
}