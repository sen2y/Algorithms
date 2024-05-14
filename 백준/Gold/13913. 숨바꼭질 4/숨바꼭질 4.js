const fs = require("fs"); 
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, K] = input[0].split(' ').map(Number);  // N: 현재 위치, K: 동생 위치
const MAX = 1000001;
// 방문배열 초기화
let visited = new Array(MAX).fill(0); //  각 위치까지의 최단 시간
// 최단 경로의 이전 좌표 저장하는 stack
let stack = new Array(MAX).fill(0); 

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
const bfs = x => { 
    const queue = new Queue(); 
    queue.enqueue(x); 
    while(queue.getLength() != 0) { 
        let v = queue.dequeue();    
        if (v === K) {
            return visited[v];
        }  
        for (let nx of [v+1, v-1, v*2] ) {  // of 대신 in을 사용해서 자꾸 인덱스에 접근했었다. 
            if (visited[nx] === 0){
                queue.enqueue(nx); 
                visited[nx] = visited[v] + 1; 
                stack[nx] = v; 
                
            } 
        } 
    }
}
// 정의된 BFS 함수 호출 
console.log(bfs(N))
let i = K;
const result = [K];
while(i !== N){ 
    result.push(stack[i])
    i = stack[i]
} 
console.log(result.reverse().join(" "));