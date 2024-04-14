// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m, count] = input[0].split(' ');
let arr = [];
for ( let i = 1; i <= n; i++){ 
  arr.push(input[i].split(' '));  
}

function inRange(x,y,flag,n,m) { 
  return x >= flag && x < flag+n && y >=flag && y < flag+m
}

let dx = [-1, 0, 1, 0] // 북 동 남 서
let dy = [0, 1, 0, -1]
let direction = 3;
let x = 0;
let y = 1;

let prev = 0; 
let tmp = 0;
for (let i = 0; i<count; i++){
  x = 0;
  y = 1;
  prev = arr[x][y]; 
  tmp = 0; 
  rotateArr(arr, n, m, 0)
}

// 정답 출력
arr.forEach((array)=>{console.log(...array)})

function rotateArr(arr, n, m, flag) { // 겉 테두리 반시계 회전
  if (n<=0 || m<=0) {
    return arr;
  }
  for (let i = 0; i < n*m - (n-2)*(m-2); i++ ){
    let px = x+dx[direction];
    let py = y+dy[direction];  
    if (!inRange(px, py, flag,n,m)) { 
      direction = (direction -1 + 4) % 4;
      
    }
    x = x+dx[direction];
    y = y+dy[direction]; 
    tmp = arr[x][y];
    arr[x][y] = prev;
    prev = tmp;  
  }  
  // 재귀함수 실행 전, x,y,prev 초기화
  x += 1;
  y += 1; 
  prev = arr[x][y];
  flag ++; // inRange 설정위한 기준
  rotateArr(arr,n-2,m-2, flag) // 재귀함수, 그다음 겉 테두리 반시계 회전
}


// 효율적인 버전
// const fs = require("fs"); 
// let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const [n, m, count] = input[0].split(' ').map(Number);
// let arr = input.slice(1, 1 + n).map(line => line.split(' ').map(Number));

// function inRange(x, y, layer) {
//   return x >= layer && x < n - layer && y >= layer && y < m - layer;
// }

// function rotateLayer(layer) {
//   let x = layer, y = layer;
//   let prev = arr[x][y + 1];
//   let directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]; // 동, 남, 서, 북
//   let dirIndex = 0;

//   while (true) {
//     let nx = x + directions[dirIndex][0];
//     let ny = y + directions[dirIndex][1];
//     if (!inRange(nx, ny, layer)) {
//       dirIndex = (dirIndex + 1) % 4;
//       nx = x + directions[dirIndex][0];
//       ny = y + directions[dirIndex][1];
//       if (!inRange(nx, ny, layer)) break;
//     }
//     const temp = arr[nx][ny];
//     arr[nx][ny] = prev;
//     prev = temp;
//     x = nx;
//     y = ny;
//   }
// }

// for (let i = 0; i < count; i++) {
//   for (let layer = 0; layer < Math.min(n, m) / 2; layer++) {
//     rotateLayer(layer);
//   }
// }

// 정답 출력
// arr.forEach(row => console.log(row.join(' ')));
// 코드 설명
// 입력 처리: 입력을 받아 첫 줄에서 n, m, count를 추출하고, 이어지는 줄들에서 배열 arr을 초기화합니다.
// inRange 함수: 주어진 x, y 좌표가 특정 레이어의 범위 내에 있는지 확인합니다. 이 함수는 테두리 회전시 범위를 벗어나는지 판단하는 데 사용됩니다.
// rotateLayer 함수: 특정 레이어의 테두리를 반시계 방향으로 회전합니다. 회전은 시작점에서 동쪽을 향해 시작하며, 범위를 벗어날 경우 방향을 시계방향으로 변경합니다.
// 회전 실행: count 만큼 전체 배열의 레이어들을 회전합니다. 가장 바깥쪽 레이어부터 시작하여, 가능한 모든 레이어를 회전시킵니다.
// 출력: 배열의 각 행을 공백으로 구분하여 출력합니다.
// 이 코드는 당신이 제공한 기존의 로직을 유지하되, 몇 가지 주요 개선을 통해 더욱 체계적이고 이해하기 쉽게 작성되었습니다. 테두리를 회전하는 구조는 매우 효율적이며, 각 레이어의 회전을 독립적으로 처리함으로써 코드의 복잡성을 줄였습니다.






