function solution(n, m, section) {
    var answer = 0;
    let index = 0;
    let last_paint = -1;
    
    for (let tile = 1; tile <= n; tile++) {
        if (index == section.length || section[index] != tile) continue;
        if (last_paint == -1 || last_paint + m <= tile) {
            answer += 1
            last_paint = tile
        }
        index += 1
    }
    
    return answer;
}