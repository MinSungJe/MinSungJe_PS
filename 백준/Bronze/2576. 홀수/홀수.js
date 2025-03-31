const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const odd = input.filter(number => number % 2 == 1)
if (odd.length === 0) {
    console.log(-1)
} else {
    console.log(odd.reduce((acc, cur) => acc + cur, 0))
    odd.sort((a, b) => a - b)
    console.log(odd[0])
}