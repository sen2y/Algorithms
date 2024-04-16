let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const [n, l, r] = input[0].split(' ').map(Number);
let grid = input.slice(1).map(x => x.split(' ').map(Number));

function inRange(x, y) {
    return x >= 0 && x < n && y >= 0 && y < n;
}

function canMove(x, y, nx, ny) {
    if (!inRange(nx, ny)) return false;
    const diff = Math.abs(grid[x][y] - grid[nx][ny]);
    return diff >= l && diff <= r;
}

function movePopulation() {
    let totalMoved = false;
    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]; // 북, 동, 남, 서

    for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
            if (visited[x][y]) continue;
            // 연합 찾기
            const stack = [[x, y]];
            const union = [];
            let sum = 0;
            while (stack.length) {
                const [cx, cy] = stack.pop();
                if (visited[cx][cy]) continue;
                visited[cx][cy] = true;
                union.push([cx, cy]);
                sum += grid[cx][cy];
                for (let dir of directions) {
                    const nx = cx + dir[0];
                    const ny = cy + dir[1];
                    if (canMove(cx, cy, nx, ny) && !visited[nx][ny]) {
                        stack.push([nx, ny]);
                    }
                }
            }
            // 인구 재분배
            if (union.length > 1) {
                totalMoved = true;
                const avg = Math.floor(sum / union.length);
                for (const [ux, uy] of union) {
                    grid[ux][uy] = avg;
                }
            }
        }
    }
    return totalMoved;
}

function simulate() {
    let days = 0;
    while (movePopulation()) {
        days++;
    }
    return days;
}

console.log(simulate());
