const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M, R] = input[0].split(' ').map(Number)

let graph = [];
for (let i = 1; i <= N; i++) graph[i] = [];
for (let i = 1; i <= M; i++) {
  let [x, y] = input[i].split(' ').map(Number); 
  graph[x].push(y);
  graph[y].push(x);
}

for (let i = 1; i <= N; i++) {
  graph[i].sort((a, b) => b - a); // 내림차순으로 정렬
}

let visited = new Array(N + 1).fill(0);
let cnt = 1; 
const dfs = (x) => { 
  visited[x] = cnt; 
  cnt++; // 각 정점을 방문할 때마다 cnt 증가
  for (let y of graph[x]) { 
    if (!visited[y]) {
      dfs(y); 
    }
  }
}

dfs(R);
console.log(visited.slice(1).join('\n'))
