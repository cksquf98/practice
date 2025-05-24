function solution(n, computers) {
    var answer = 0;
    let visited = Array(n).fill(false);
    
    function dfs(computer, idx) {
        visited[idx] = true;
        for (let i=0; i<n; i++) {
            if(!visited[i] && computer[i] == 1) {
                dfs(computers[i],i)
            }
        }
    }
    
    for (let i=0; i < n; i++) {
        if (!visited[i]) {
            dfs(computers[i], i)
            answer ++;
        }
    }
    
    return answer;
} 