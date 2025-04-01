const fs = require('fs');

// 입력부
const N = Number(fs.readFileSync(0).toString());

// 초기값 선언
const INF = 1000000007

// DP 배열 선언
const DP = Array.from({length: N+1}).map(number => -1)

// DFS
function DFS(idx) {
    if (idx > N) return 1
    if (DP[idx] !== -1) return DP[idx]

    // 결과값 구하기
    let result = 0
    result = (result+2*DFS(idx+1)) % INF
    result = (result+DFS(idx+1)) % INF

    result %= INF
    DP[idx] = result // 메모이제이션
    return result
}

// 함수 호출 및 출력부
const result = DFS(1) - 1
console.log(result)