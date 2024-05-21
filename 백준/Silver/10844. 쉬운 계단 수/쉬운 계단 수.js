const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
let d = Array.from(Array(N+1), ()=> new Array(10).fill(0)) 

d[1][0] = 0;
for (let j = 1; j <= 9; j++){
    d[1][j] = 1;
} 
for (let i = 2; i <= N; i++){ 
    for (let j = 0; j <= 9; j++){
        if (j>0) d[i][j] += d[i-1][j-1];
        if (j<9) d[i][j] += d[i-1][j+1];
        d[i][j] %= Number(1e9);
    }
} 

let result = 0;
for (let j=0; j<=9; j++){
    result += d[N][j];
    result %= Number(1e9);
}
console.log(result)