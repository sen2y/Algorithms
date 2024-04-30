const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number)
const num = input[1].split(' ').map(Number).sort((a,b)=>a-b)

// 중복 O, 오름차순만 가능
let arr = []; // 현재 진행중인 배열
let answer = [];

const dfs = (depth, start) => {
  if (depth === m) {
    answer.push(arr.join(' ') )
    return
  }
  for (let i = start; i<n ; i++) {
    arr.push(num[i])
    dfs(depth+1, start++);
    arr.pop()
  }
}

dfs(0,0);
console.log(answer.join('\n'))