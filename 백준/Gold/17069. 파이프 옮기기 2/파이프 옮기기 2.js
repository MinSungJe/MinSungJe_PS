const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

// 입력부
const N = Number(input[0]);
const Map = input.slice(1).map(line => line.trim().split(' ').map(Number));

// 회전 정보 기록
const dx = [0, 1, 1];
const dy = [1, 1, 0];
const rotate = [[0, 1], [0, 1, 2], [1, 2]];

// DP 배열 선언
const DP = Array.from({ length: N }, () =>
    Array.from({ length: N }, () =>
        Array(3).fill(-1)
    )
);

// DFS
function DFS(X, Y, pos) {
    // 탐색 종료
    if (X === N-1 && Y === N-1) return 1;
    if (DP[X][Y][pos] !== -1) return DP[X][Y][pos]; // 메모이제이션

    // 다음 탐색
    let result = 0;
    for (let pos_ of rotate[pos]) {
        const X_ = X + dx[pos_];
        const Y_ = Y + dy[pos_];
        
        // 탐색 불가 조건
        if (X_ >= N || Y_ >= N || Map[X_][Y_] === 1) continue;
        // 대각선 이동 추가 조건
        if (pos_ === 1 && (Map[X_-1][Y_] === 1 || Map[X_][Y_-1] === 1)) continue;

        result += DFS(X_, Y_, pos_)
    }

    // 메모이제이션
    DP[X][Y][pos] = result;
    return result;
}

// 함수 호출 및 출력부
const result = DFS(0, 1, 0);
console.log(result);