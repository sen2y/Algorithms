const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 
const numberSort = (n1, n2) => {
  return n1 - n2;
}
const num = input[1].split(' ').map(Number).sort(numberSort)

let arr = []; // 현재 진행 중인 배열
let answer = ""; // 정답 문자열 -> 한 번에 정답코드 출력하기 위해.   

const dfs = (depth) => { 
  if (depth === m) { // 깊이 m 만큼 arr 배열이 채워지면,
    arr.forEach(x => answer+= `${x} `);
    answer += '\n'; 
    return;
  }
  for (let i = 0; i<n; i++) {   
      arr.push(num[i]); // 배열값 하나씩 추가 
      dfs(depth+1) // 재귀함수 실행 
      arr.pop(); 
    
  }
}

dfs(0)
console.log(answer)
