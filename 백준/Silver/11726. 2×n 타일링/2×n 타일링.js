const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
let d = new Array(N+1).fill(0);
d[0] = 1;
d[1] = 1;
for (let i = 2; i <= N; i++){ 
    d[i] = (d[i-1] + d[i-2])%10007 ;
} 
console.log(d[N]);