const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.slice(1); 
const output = []; 

class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0; // 제일 앞부분 인덱스
    this.tailIndex = 0; // 제일 마지막 인덱스
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

  findHead() {
    if (!(this.tailIndex - this.headIndex)) {return -1;} 
    return this.items[this.headIndex];
  }

  findTail() {
    if (!(this.tailIndex - this.headIndex)) {return -1;}
    return this.items[this.tailIndex-1];
  }

  size() {
    const size = this.tailIndex - this.headIndex;
    return size;
  }

  empty() {
    return (this.tailIndex - this.headIndex) ? 0 : 1
  }
}
const queue = new Queue();
arr.forEach((x) => {
  
  switch (x) {
    case 'pop' : 
      output.push(queue.dequeue());
      break;
    case 'size' :
      output.push(queue.size());
      break;
    case 'empty' :
      output.push(queue.empty());
      break;
    case 'front' :
      output.push(queue.findHead());
      break;
    case 'back' :
      output.push(queue.findTail());
      break;
    default : 
      const [push, num] = x.split(' ')
      queue.enqueue(Number(num));
      break;
      
  }
})
console.log(output.join('\n'))