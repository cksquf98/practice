function solution(k, dungeons) {
    var answer = 0;
    const visited = Array(dungeons.length).fill(false);
    
    function dfs(currentFatigue, count) {
        if(count > answer) answer = count;

        for (let i=0; i<dungeons.length; i++) {
            if (visited[i] == false && dungeons[i][0] <= currentFatigue) {
                visited[i] = true;
                dfs(currentFatigue - dungeons[i][1], count+1)
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0)
    return answer;
}

