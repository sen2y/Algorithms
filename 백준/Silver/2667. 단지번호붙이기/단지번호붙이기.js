const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); 
const N = Number(input[0]);

// 이차원 배열 생성
let graph = new Array(N).fill(null).map(() => Array(N).fill(0));
for (let y in graph) {
    graph[y] = input[Number(y) + 1].split('').map(Number);
}

const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

const inRange = (x, y) => {
    return x >= 0 && x < N && y >= 0 && y < N && graph[x][y] === 1;
};

const dfs = (x, y, visited) => {
    visited[x][y] = true;
    let cnt = 1; // 각 영역의 카운트를 새로 초기화
    for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (inRange(nx, ny) && !visited[nx][ny]) {
            cnt += dfs(nx, ny, visited); // 재귀 호출 결과를 합산
        }
    }
    return cnt; // 영역의 카운트 반환
};

let counts = [];
let visited = new Array(N).fill(false).map(() => new Array(N).fill(false));
let totalcnt = 0;
for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (!visited[i][j] && graph[i][j] === 1) {
            const cnt = dfs(i, j, visited);
            counts.push(cnt); // 각 영역의 카운트를 push
            totalcnt++;
        }
    }
}

console.log(totalcnt)
console.log(counts.sort((a,b)=>a-b).join('\n'));
