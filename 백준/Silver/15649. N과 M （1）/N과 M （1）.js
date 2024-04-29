const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ');

let visited = new Array(n).fill(false); // 각 원소 false 로 초기화
let arr = [];
let answer = ""; // 정답
const dfs = (depth) => { 
  for (let i = 0; i < n; i++){ 
    if (depth === Number(m)) { 
      arr.forEach(x => answer += `${x} `); 
      answer += "\n"
      return;
    }
    else if (!visited[i]) { 
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
