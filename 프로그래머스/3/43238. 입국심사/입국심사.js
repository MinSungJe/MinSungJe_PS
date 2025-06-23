function solution(n, times) {    
    // 시간 안에 모두를 심사할 수 있는 지 확인하는 함수
    function canSimsa(maxTime) {
        return n <= times.reduce((acc, time) => acc + Math.floor(maxTime / time), 0)
    }
    
    // 이분 탐색
    let l = 0;
    let r = times.reduce((acc, time) => time > acc ? time : acc, 0) * n;
    while (l < r) {
        const mid = Math.floor((l+r)/2);
        
        // 답이 될 수 있는 경우 r을 땡김 -> 시간(중간값)이 짧아짐
        if (canSimsa(mid)) r = mid;
        // 답이 될 수 없는 경우 l을 땡김 -> 시간(중간값)이 커짐
        else l = mid+1;
    }
    
    var answer = r;
    return answer;
}