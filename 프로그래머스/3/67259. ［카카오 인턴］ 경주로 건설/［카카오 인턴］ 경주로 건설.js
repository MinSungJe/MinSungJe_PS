function solution(board) {
    const INF = (25 * 25 * 600) + 1;
    var answer = INF;
    const N = board.length;
    
    // 전역 변수 선언
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const visited = Array.from({length: N}).map(() => Array.from({length: N}).map(() => [INF, INF]));
    
    function DFS(X, Y, isVertical, value) {
        const isVerticalIndex = isVertical ? 1 : 0;
        
        // 탐색 종료
        if (X === N-1 && Y === N-1) {
            answer = Math.min(answer, value);
            return;
        }
        
        // 탐색 불가 조건
        if (X < 0 || X >= N || Y < 0 || Y >= N) return;
        if (board[X][Y] === 1) return;
        if (visited[X][Y][isVerticalIndex] <= value) return;
        
        // 탐색
        visited[X][Y][isVerticalIndex] = value;
        
        // 다음 탐색
        for (let i=0;i<4;i++) {
            const X_ = X+dx[i];
            const Y_ = Y+dy[i];
            if (isVertical) {
                if (i == 0 || i == 1) DFS(X_, Y_, true, value+100);
                if (i == 2 || i == 3) DFS(X_, Y_, false, value+100+500);
            } else {
                if (i == 0 || i == 1) DFS(X_, Y_, true, value+100+500);
                if (i == 2 || i == 3) DFS(X_, Y_, false, value+100);
            }
        }
                
    }

    DFS(0, 0, true, 0);
    DFS(0, 0, false, 0);
    return answer;
}