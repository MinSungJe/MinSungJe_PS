function solution(cacheSize, cities) {
    var answer = 0;
    
    // cache 선언
    let cache = [];
    
    
    for (let city of cities) {        
        // cache에 있는지 확인
        if (cache.includes(city.toUpperCase())) {
            const cacheIndex = cache.indexOf(city.toUpperCase());
            cache = [...cache.slice(0, cacheIndex), ...cache.slice(cacheIndex+1, cache.length)]
            answer += 1;
        
        }
        else answer += 5;
        
        // cache에 추가
        cache.push(city.toUpperCase());
        
        // cache에 값이 많을 경우 shift
        if (cache.length > cacheSize) cache.shift()
    }
    
    return answer;
}