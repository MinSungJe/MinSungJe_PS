// queue 구현(간단 버전)
class Queue {
    items = [];
    front = 0;
    rear = 0;
    
    push(item) {
        this.items.push(item);
        this.rear++;
    }
    
    shift() {
        return this.items[this.front++];
    }
    
    isEmpty() {
        return this.front === this.rear;
    }
}

function solution(x, y, n) {
    // 모든 탐색이 되지 않은 경우 -1
    var answer = -1;
    
    // 초기값 선언
    const queue = new Queue();
    queue.push([x, 0])
    const visited = new Array(y+1).fill(false);
    
    // BFS
    while (!queue.isEmpty()) {
        const [X, count] = queue.shift();
        
        // 탐색 불가 조건
        if (X > y) continue;
        if (visited[X]) continue;
        
        // 탐색
        if (X === y) { // y 도착
            answer = count;
            break;
        }
        visited[X] = true;
        
        // 다음 탐색
        for (let X_ of [X+n, X*2, X*3])
            queue.push([X_, count+1]);
    }
        
    return answer;
}