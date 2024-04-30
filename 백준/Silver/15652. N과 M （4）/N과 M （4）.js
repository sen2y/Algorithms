const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 

let arr = [];
let answer = "";

const dfs = (depth, start) => {
  if (depth === m) {
    arr.forEach(x => answer+= `${x} `);
    answer += '\n';
    return;
  }
  for (let i = start; i<n; i++) { 
    arr.push(i+1);
    dfs(depth+1, start++) // start+1 로 하면 다른 결과가 나온다.
    arr.pop();
  }
}

dfs(0,0)
console.log(answer)
