let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [rows, columns] = input[0].split(' ').map(Number); // 각자 숫자로 형변환
const  arr = Array.from(new Array(rows), () => new Array(columns).fill(0));

function inRange(x,y) { // 범위 체크 함수
  return x>=0 && x <rows && y>=0 && y<columns;
}

const dx = [-1, 0, 1, 0]; // 북 동 남 서
const dy = [0, 1, 0, -1];

let x=0;
let y=0;
let direction = 1; // 기본 방향
let count=0; // 제출 값
arr[0][0] = 1;

for (let i=2; i<=columns*rows; i++){
  let nx = x+dx[direction];
  let ny = y+dy[direction];
  
  if ( !inRange(nx,ny)|| arr[nx][ny] !== 0) {  // 범위 밖이거나, 이미 들른 곳인 경우
    direction = (direction+1) % 4; // 방향 전환
    count++; // 제출 값 ++
  }
  x = x+dx[direction];
  y = y+dy[direction]; 
  arr[x][y] = i; 
} 

console.log(count)
