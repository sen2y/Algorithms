const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); 
const N = Number(input[0]);

let graph = new Array(N).fill([]); 
let maxHeight = 0;
for (let y in graph) {
    graph[y] = input[Number(y) + 1].split(' ').map(Number);
    maxHeight = Math.max(maxHeight, Math.max(...graph[y]));
}

const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

const inRange = (x, y, height) => {
    return x >= 0 && x < N && y >= 0 && y < N && graph[x][y] > height;
};

const dfs = (x, y, height, visited) => {  
    visited[x][y] = true; 
    for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (inRange(nx, ny, height) && !visited[nx][ny]) {
            dfs(nx, ny, height, visited);
        }
    }
};

let maxCnt = 0; // 최댓값
for (let h = 0; h <= maxHeight; h++) {
    let visited = new Array(N).fill(false).map(() => new Array(N).fill(false)); 
    let cnt = 0;
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (!visited[i][j] && graph[i][j] > h) {
                dfs(i, j, h, visited); 
                cnt++;
            }
        }
    }
    maxCnt = Math.max(maxCnt, cnt);
}

console.log(maxCnt);