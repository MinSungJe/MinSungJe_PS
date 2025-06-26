function solution(strings, n) {
    var answer = [];
    
    // 문자열 정렬
    strings.sort(); // 사전순 정렬
    strings.sort((a, b) => a[n].charCodeAt() - b[n].charCodeAt()); // 문제 조건 정렬
    answer = [...strings]
    
    return answer;
}