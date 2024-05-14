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

const bfs = () => { 
    const queue = new Queue(); // 새로운 큐 인스턴스 생성
    let visited = Array.from(Array(N), () => Array(M).fill(-1)); // 방문 여부 및 거리 추적을 위한 2차원 배열 초기화
    let maxDist = 0; // 최대 거리 저장 변수

    // 아기 상어 위치를 큐에 추가
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (arr[i][j] === 1) {
                queue.enqueue([i, j]); // 상어 위치를 큐에 추가
                visited[i][j] = 0; // 상어 위치의 방문 거리를 0으로 설정
            }
        }
    }

    while (queue.getLength() > 0) { // 큐가 빌 때까지 반복
        const [x, y] = queue.dequeue(); // 큐에서 위치 정보를 하나 가져옴
        for (let i = 0; i < 8; i++) { // 모든 이동 가능한 방향을 검사
            const nx = x + dx[i]; // 다음 위치의 x좌표
            const ny = y + dy[i]; // 다음 위치의 y좌표
            if (inRange(nx, ny) && visited[nx][ny] === -1) { // 범위 내이고 방문하지 않은 경우
                visited[nx][ny] = visited[x][y] + 1; // 거리를 업데이트
                queue.enqueue([nx, ny]); // 새 위치를 큐에 추가
                maxDist = Math.max(maxDist, visited[nx][ny]); // 최대 거리 업데이트
            }
        }
    }

    return maxDist; // 계산된 최대 거리 반환
};


// 상어 위치를 찾고 BFS 실행하여 결과를 출력
console.log(bfs());