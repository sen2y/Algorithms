const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
let arr = [];

for (let i = 1; i <= N; i++){
    arr.push(input[i].split(" ").map(Number));
} 

const inRange = (x, y) => x >= 0 && x < N && y >= 0 && y < M;

const dx = [-1, -1, 0, 1, 1, 1, 0, -1];
const dy = [0, 1, 1, 1, 0, -1, -1, -1];

const bfs = (starts) => { 
    let queue = starts.slice(); // 복사하여 사용
    let maxDist = 0;
    let visited = Array.from(Array(N), () => Array(M).fill(-1));

    starts.forEach(([x, y]) => {
        visited[x][y] = 0; // 상어 위치는 거리 0
    });

    while (queue.length > 0) {
        const [x, y] = queue.shift();
        for (let i = 0; i < 8; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            if (inRange(nx, ny) && visited[nx][ny] === -1) {
                visited[nx][ny] = visited[x][y] + 1;
                queue.push([nx, ny]);
                maxDist = Math.max(maxDist, visited[nx][ny]);
            }
        }
    }
    return maxDist;
};

// 상어 위치 찾기
const starts = [];
for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (arr[i][j] === 1) starts.push([i, j]);
    }
}

console.log(bfs(starts));
