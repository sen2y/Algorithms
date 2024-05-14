const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M, V] = input[0].split(' ').map(Number);
let graph = [];
for (let i=1; i<=N; i++) graph[i] = [];
for (let i=1; i<=M; i++){
  let [x,y] = input[i].split(' ').map(Number); 
  graph[x].push(y);
  graph[y].push(x);
}

for (let i=1; i <= N; i++) {
  graph[i].sort((a,b) => a - b);
} 

let visitedD = new Array(N+1).fill(false);

const arrDfs = [];
const arrBfs = [];
const dfs = x => {
    visitedD[x] = true; 
    arrDfs.push(x)
    for (y of graph[x]) {
        if (!visitedD[y]) {
            dfs(y);
        }
    }
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
// 각 노드가 방문된 정보를 표현
let visitedB = Array(9).fill(false);
function bfs(graph, start, visited) {
  const queue = new Queue();
  queue.enqueue(start);
  // 현재 노드를 방문 처리
  visited[start] = true;
  // 큐가 빌 때까지 반복
  while (queue.getLength() != 0) {
    // 큐에서 하나의 원소를 뽑아 출력하기
    const v = queue.dequeue();
    // console.log(v);
    arrBfs.push(v);
    // 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for (i of graph[v]) { 
        // graph 배열의 v번째 요소, 노드 v와 직접 연결된 노드들의 목록을 포함. 
        // 예를 들어, graph[1] = [2, 3, 4]일 때, 
        // for (i of graph[1])는 i가 순서대로 2, 3, 4 값을 가지게 된다.
        // i는 인덱스가 아닌 요소의 값
      if (!visited[i]) {
        queue.enqueue(i);
        visited[i] = true;
       
      }
    }
  }
}

// 정의된 DFS 함수 호출
dfs(V);
console.log(arrDfs.join(" "))
// 정의된 BFS 함수 호출
bfs(graph, V, visitedB);
console.log(arrBfs.join(" "))
