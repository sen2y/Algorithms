const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 
const numberSort = (n1, n2) => {
  return n1 - n2;
}
const num = input[1].split(' ').map(Number).sort(numberSort)

let arr = []; // 현재 진행 중인 배열
let answer = ""; // 정답 문자열 -> 한 번에 정답코드 출력하기 위해. 
let visited = new Array(n).fill(false);  // 중복 방지 위해 visited 배열 사용 

const dfs = (depth , start) => { 
  if (depth === m) { // 깊이 m 만큼 arr 배열이 채워지면,
    arr.forEach(x => answer+= `${x} `);
    answer += '\n'; 
    return;
  }
  for (let i = start; i<n; i++) { 
    if (!visited[i]) { // 방문하지 않은 배열값에서만 실행
      visited[i] = true; 
      arr.push(num[i]); // 배열값 하나씩 추가 
      dfs(depth+1, start+1) // 재귀함수 실행
      visited[i] = false;
      arr.pop();
      start+=1; // 추가 (앞자리수 바뀔 때 start 인덱스 값 증가)
    }
  }
}

dfs(0, 0)
console.log(answer)