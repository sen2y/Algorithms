const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input[0].split(' ').map(Number); 
const numberSort = (n1, n2) => { // 일반 sort()는 문자열기준이므로, 숫자 sort함수 구현
  return n1 - n2;
}
const num = input[1].split(' ').map(Number).sort(numberSort);  // 순열에 사용되는 입력값을 오름차순 숫자배열로 할당

let arr = []; // 현재 진행 중인 배열
let answer = ""; // 정답 문자열 -> 한 번에 정답코드 출력하기 위해. 
let visited = new Array(n).fill(false);  // 중복 방지 위해 visited 배열 사용 

const dfs = (depth) => { 
  if (depth === m) { // 깊이 m 만큼 arr 배열이 채워지면,
    arr.forEach(x => answer+= `${x} `);
    answer += '\n';
    return;
  }
  for (let i = 0; i<n; i++) { 
    if (!visited[i]) { // 방문하지 않은 배열값에서만 실행
      visited[i] = true;
      arr.push(num[i]); // 배열값 하나씩 추가 
      dfs(depth+1) // 재귀함수 실행
      visited[i] = false;
      arr.pop();
    }
  }
}

dfs(0)
console.log(answer)

