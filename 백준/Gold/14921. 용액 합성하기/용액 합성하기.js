const fs = require('fs');

// 입력부
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
const A = input[1].split(' ').map(Number);

// 초기값 선언
const INF = 200000001;
let l = 0;
let r = N-1;

// 투 포인터
let min_value = INF;
let result = INF;
while (l < r) {
    const value = A[l] + A[r];
    
    // 0과 가까운 값 최신화
    if (Math.abs(value) < min_value) {
        result = value;
        min_value = Math.abs(value);
    }

    if (value < 0) l += 1;
    if (value == 0) break;
    if (value > 0) r -= 1;
}

// 출력부
console.log(result);