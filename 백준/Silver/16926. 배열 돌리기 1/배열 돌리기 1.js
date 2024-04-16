// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m, count] = input[0].split(' '); // n: 세로, m: 가로, count: 회전 횟수
let arr = [];
for ( let i = 1; i <= n; i++){  // 배열 입력
  arr.push(input[i].split(' '));  
}

function inRange(x,y,flag,n,m) {  // 범위 체크
  return x >= flag && x < flag+n && y >=flag && y < flag+m
}

let dx = [-1, 0, 1, 0] // 북 동 남 서
let dy = [0, 1, 0, -1]
let direction = 3; // 서쪽
let x = 0;
let y = 1;

let prev = 0; // 이전 값 저장
let tmp = 0; // 임시 저장
for (let i = 0; i<count; i++){
  x = 0; 
  y = 1; 
  prev = arr[x][y]; // 시작점 
  tmp = 0; // 초기화
  rotateArr(arr, n, m, 0) // 겉 테두리 반시계 회전
}

// 정답 출력
arr.forEach((array)=>{console.log(...array)})

function rotateArr(arr, n, m, flag) { // 겉 테두리 반시계 회전
  if (n<=0 || m<=0) { // n이나 m이 0이면 종료
    return arr;
  }
  for (let i = 0; i < n*m - (n-2)*(m-2); i++ ){ // n*m - (n-2)*(m-2) : 테두리의 길이
    let px = x+dx[direction];  
    let py = y+dy[direction];  
    if (!inRange(px, py, flag,n,m)) { 
      direction = (direction -1 + 4) % 4; // 반시계 방향 전환
      
    }
    x = x+dx[direction]; 
    y = y+dy[direction]; 
    tmp = arr[x][y]; // 현재 값 저장
    arr[x][y] = prev; // 현재 값에 이전 값 저장
    prev = tmp;  // 이전 값에 현재 값 저장
  }  
  // 재귀함수 실행 전, x,y,prev 초기화
  x += 1;
  y += 1; 
  prev = arr[x][y];
  flag ++; // inRange 설정위한 기준
  rotateArr(arr,n-2,m-2, flag) // 재귀함수, 그다음 겉 테두리 반시계 회전
}




