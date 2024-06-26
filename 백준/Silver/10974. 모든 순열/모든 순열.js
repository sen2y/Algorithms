
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n] = input[0].split(' ').map(Number); 

let visited = new Array(n).fill(false); // 각 원소 false 로 초기화
let arr = [];
let answer = ""; // 정답
const dfs = (depth) => { 
  if (depth === n) {  
    arr.forEach(x => answer += `${x} `); 
    answer += "\n"
    return;
  }
  for (let i = 0; i < n; i++){
   if (!visited[i]) { 
      visited[i] = true;
      arr.push(i+1);
      dfs(depth+1);
      visited[i] = false;
      arr.pop();
    }
  }


}

dfs(0);
console.log(answer)