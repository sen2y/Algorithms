let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, l, r] = input[0].split(" ").map(Number);
let arr = input.slice(1).map((x) => x.split(" ").map(Number));

function inRange(x, y) {
  return x >= 0 && x < n && y >= 0 && y < n;
}

function canMove(x, y, nx, ny) {
  if (!inRange(nx, ny)) return false;
  const gap = Math.abs(arr[x][y] - arr[nx][ny]);
  return gap >= l && gap <= r;
}

function movePopulation() {
  // 전체 arr 순회하며 가능한 모든 연합 찾기 + 인구 재분배 수행
  let totalMoved = false; // 인구 이동 여부, 초기값 false
  const visited = Array.from({ length: n }, () => Array(n).fill(false)); // n x n 배열, 방문 여부
  const directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ]; // 북, 동, 남, 서

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      if (visited[x][y]) continue; // 이미 방문한 경우 건너뛰기
      // 연합 찾기
      const stack = [[x, y]]; // 스택에 현재 위치 추가
      const union = []; // 연합에 속하는 칸들의 목록 저장
      let sum = 0; // 연합의 인구 수
      while (stack.length) {
        // 스택이 빌 때까지 반복
        const [cx, cy] = stack.pop(); // 스택에서 하나의 칸 꺼내기
        if (visited[cx][cy]) continue; // 이미 방문한 경우 건너뛰기
        visited[cx][cy] = true; // 방문 처리
        union.push([cx, cy]); // 연합에 추가
        sum += arr[cx][cy]; // 인구 수 더하기
        for (let dir of directions) {
          // 북동남서 이중배열로 반복문 수행
          const nx = cx + dir[0]; // 다음 x 좌표
          const ny = cy + dir[1]; // 다음 y 좌표
          if (canMove(cx, cy, nx, ny) && !visited[nx][ny]) {
            // 이동 가능하고 방문하지 않은 경우
            stack.push([nx, ny]); // 스택에 추가
          }
        }
      }
      // 인구 재분배
      if (union.length > 1) {
        // 연합이 2개 이상인 경우
        totalMoved = true; // 인구 이동 발생
        const avg = Math.floor(sum / union.length); // 연합의 평균 인구 수
        for (const [ux, uy] of union) {
          // 연합에 속하는 모든 칸에 대해 반복
          arr[ux][uy] = avg; // 인구 수 재설정
        }
      }
    }
  }
  return totalMoved; // 인구 이동 여부 반환
}

function solution() {
  let days = 0; // 인구 이동이 발생한 날짜
  while (movePopulation()) {
    days++;
  }
  return days;
}

console.log(solution());
