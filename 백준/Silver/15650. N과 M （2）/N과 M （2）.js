const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 

let visited = new Array(n).fill(false); // 각 원소 false 로 초기화
let arr = [];
let answer = ""; // 정답
const dfs = (depth) => { 
  if (depth === Number(m)) {  
    arr.forEach(x => answer += `${x} `); 
    answer += "\n"
    return;
  }
  for (let i = 0; i < n; i++){
   if (!visited[i]) { 
     if (arr.length > 0) { // 이 문제는 중복순열 nCr. 배열의 이전값보다 현재 i값이 크면 넘어가는 코드 추가
        if (arr[arr.length-1] > i) continue;
      }
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
