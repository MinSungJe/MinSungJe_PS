function solution(n, costs) {
    var answer = 0;
    
    // union-find
    const parents = new Array(n).fill(null).map((_, i) => i);
    function find(node) {
        if (node === parents[node]) return node;
        parents[node] = find(parents[node]); // 경로 단축
        return parents[node];
    }
    
    function union(node1, node2) {
        const parent1 = find(node1);
        const parent2 = find(node2);
        if (parent1 === parent2) return;
        if (parent1 < parent2) parents[parent2] = parent1;
        else parents[parent1] = parent2;
    }
    
    // 가장 비용이 작은 경로부터 탐색
    costs.sort((a, b) => a[2] - b[2]);
    for (let [node1, node2, cost] of costs) {
        // 만약 이미 연결되어 있으면 continue
        if (find(node1) === find(node2)) continue;
        
        // 연결
        union(node1, node2);
        answer += cost;
    }
    
    return answer;
}