// readline 모듈보다는 fs를 이용해 파일 전체를 읽어 들여 처리하기
let fs = require("fs"); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m, count] = input[0].split(' ');
let arr = [];
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
        
        let size = temp.length;
        let shift = R % size;  // 실제 회전 수 계산

        // 회전 처리
        temp = [...temp.slice(shift), ...temp.slice(0, shift)];

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
const result = rotateMatrix(n, m, count, arr);
result.forEach(row => console.log(row.join(' ')));


