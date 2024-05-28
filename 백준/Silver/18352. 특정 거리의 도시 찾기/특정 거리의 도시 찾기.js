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
const [N,M,K,X] = input[0].split(" ").map(Number);
// let graph = new Array(N+1).fill([]); //  new Array(N+1).fill([])는 동일한 빈 배열을 각 요소에 할당하므로, 하나의 배열을 수정하면 모든 요소가 영향을 받습니다.
let graph = new Array(N + 1).fill(null).map(() => []);

for (let i = 1; i <= M; i++){
    const [a,b] = input[i].split(" ").map(Number);
    graph[a].push(b);
} 

let distance = new Array(N+1).fill(null).map(()=>-1);
let start = X;
let queue = new Queue();
function bfs() {
    queue.enqueue(start);
    distance[start] = 0; // 시작노드 거리는 0 
    while (queue.getLength() > 0){
        let node = queue.dequeue(); 
        for (i of graph[node]){ 
            if (distance[i] == -1){ 
                queue.enqueue(i);
                distance[i] = distance[node] + 1;
            }
        }
    }
} 
bfs();
let check = false;
for (let i = 1; i < N+1; i++){
    if (distance[i] == K) {
        console.log(i);
        check = true;
    }
}
if (!check) console.log(-1)