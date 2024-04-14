// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const flag = Number(input[1]); 
let arr= [];
for (let i =0; i<n; i++){
  arr[i] = new Array(n)
  for (let j=0; j<n; j++){
    arr[i][j] = 0;
  }
} 

function inRange(x,y) {
  return x >= 0 && x < n && y >=0 && y < n
}

// 시작 위치
let start = (n-1)/2
arr[start][start] = 1;


let x = start;
let y = start; 
// dx dy
const dx = [-1, 0, 1, 0]; // 북 동 남 서
const dy = [0, 1, 0, -1];
let direction = 3;

for (let i = 2; i<= n*n; i++){ 
  direction = (direction+1) % 4 
  let nx = x+dx[direction];
  let ny = y+dy[direction];  
  if (arr[nx][ny] !== 0) { // 이미 지나간 곳
    direction = (direction -1 + 4) % 4;
  } 

  x += dx[direction];
  y += dy[direction]; 
  arr[x][y] = i;  
}
  
arr.forEach((array)=> {  
  console.log(...array)
})
// 위치 찾기
let index = [];
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (arr[i][j] === flag) {
            index = [i + 1, j + 1]; // 1-based index로 출력
            break;
        }
    }
    if (index.length > 0) break;
}

console.log(...index);