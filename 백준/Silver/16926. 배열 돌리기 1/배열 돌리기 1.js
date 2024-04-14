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

