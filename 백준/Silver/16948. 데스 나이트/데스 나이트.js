const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
let [x, y, x2, y2] = input[1].split(" ").map(Number); 

// 범위 체크 함수
const inRange = (x,y) => {
    return x >= 0 && x < N && y >= 0 && y < N;
}

// 이동 방향 정의
dx = [-2, -2, 0, 2, 2, 0];
dy = [-1, 1, 2, 1, -1, -2];

let visited = [];
// 방문배열 초기화
for (let i = 0; i < N; i++ ) {
    visited.push(new Array(N).fill(0));
}

// 큐 정의
class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0;
    this.tailIndex = 0;
  }
  enqueue(item) {
    this.items[this.tailIndex] = item;
    this.tailIndex++;
  }
  dequeue() {
    const item = this.items[this.headIndex];
    delete this.items[this.headIndex];
    this.headIndex++;
    return item;
  }
  peek() {
    return this.items[this.headIndex];
  }
  getLength() {
    return this.tailIndex - this.headIndex;
  }
}

// BFS 메서드 정의 
const bfs = (x, y) => { 
    const queue = new Queue(); 
    queue.enqueue([x,y]); 
    visited[x][y] = 1;
    while (queue.getLength() != 0) {
        let cur = queue.dequeue();
        x = cur[0];
        y = cur[1];
        if(x === x2 && y === y2) { 
            return visited[x][y] -1
        }
        for (let i = 0; i < 6; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            if (inRange(nx,ny) && !visited[nx][ny]){
                visited[nx][ny] = visited[x][y] + 1;
                queue.enqueue([nx, ny])
            }
        }
    }
    return -1;
}
// 정의된 BFS 함수 호출 
console.log(bfs(x,y))  