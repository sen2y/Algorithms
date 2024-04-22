const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim()

class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0; // 제일 앞부분 인덱스
    this.tailIndex = 0; // 제일 마지막 인덱스 +1
  }

  enqueue(item) { // push 연산
    this.items[this.tailIndex] = item; // 꼬리에 삽입 
    this.tailIndex++;
  }

  dequeue() { // pop 연산
    if (!(this.tailIndex - this.headIndex)) {return -1;}
    const item = this.items[this.headIndex];
    // 머리 메모리 삭제
    delete this.items[this.headIndex];
    this.headIndex++;
    return item; // 삭제된 머리 출력
  }
  empty() {
    return (this.tailIndex - this.headIndex) ? 0 : 1
  }
}

const queue = new Queue();
for (let i = 0; i<input; i++){
  queue.enqueue(i+1);
}
 
while (!queue.empty()) {
  const del = queue.dequeue();
  const top = queue.dequeue();
  if (top == -1) {
    return console.log(del)
  } 
  queue.enqueue(top);
}
  