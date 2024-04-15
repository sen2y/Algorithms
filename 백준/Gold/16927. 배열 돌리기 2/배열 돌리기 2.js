// 동일한 문제 16926번 에서는 dx dy로 문제 풀었으나, 시간복잡도 초과 이슈로 단순 반복문으로 변경 
// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m, r] = input[0].split(' ');
let arr = [];
// 배열 초기화 - 더 나은 방법
// let arr = input.slice(1).map(x=>x.split(' ').map(Number))
for ( let i = 1; i <= n; i++){ 
  arr.push(input[i].split(' '));  
}
function rotateMatrix(N, M, R, matrix) {
    let layers = Math.min(N, M) / 2;
    for (let layer = 0; layer < layers; layer++) {
        let temp = [];
        let firstRow = layer;
        let lastRow = N - layer - 1;
        let firstCol = layer;
        let lastCol = M - layer - 1;

        // 행렬의 레이어를 temp 배열에 저장
        for (let i = firstCol; i <= lastCol; i++) temp.push(matrix[firstRow][i]); // 상
        for (let i = firstRow + 1; i <= lastRow; i++) temp.push(matrix[i][lastCol]); // 우
        for (let i = lastCol - 1; i >= firstCol; i--) temp.push(matrix[lastRow][i]); // 하
        for (let i = lastRow - 1; i > firstRow; i--) temp.push(matrix[i][firstCol]); // 좌
        
        let size = temp.length; // n*m - (n-2)*(m-2) 와 동일. 테두리 요소의 수
        let count = R % size;  // 실제 회전 수 계산

        // 회전 처리
        // 구조 분해 할당으로 리스트 합치기 + slice(count)로 count index 부터 ~
        temp = [...temp.slice(count), ...temp.slice(0, count)];

        // 회전된 내용을 행렬에 다시 채우기
        let index = 0;
        for (let i = firstCol; i <= lastCol; i++) matrix[firstRow][i] = temp[index++]; // 상
        for (let i = firstRow + 1; i <= lastRow; i++) matrix[i][lastCol] = temp[index++]; // 우
        for (let i = lastCol - 1; i >= firstCol; i--) matrix[lastRow][i] = temp[index++]; // 하
        for (let i = lastRow - 1; i > firstRow; i--) matrix[i][firstCol] = temp[index++]; // 좌
    }

    return matrix;
}

// 함수 실행 및 결과 출력
const result = rotateMatrix(n, m, r, arr);
result.forEach(row => console.log(row.join(' ')));


