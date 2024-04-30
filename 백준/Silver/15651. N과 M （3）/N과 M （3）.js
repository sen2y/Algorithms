const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 

let arr = [];
let answer = "";

const dfs = depth => {
  if (depth === m) {
    arr.forEach(x => answer += `${x} `);
    answer += "\n"
    return
  }
  for (let i=0; i<n; i++){
    arr.push(i+1)
    dfs(depth+1);
    arr.pop();
  }
}

dfs(0)
console.log(answer)
