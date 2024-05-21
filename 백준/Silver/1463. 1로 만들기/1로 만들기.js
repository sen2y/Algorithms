const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
let d = new Array(1000001).fill(0);

for (let i = 2; i <= N; i++){ 
    d[i] = d[i-1] + 1;
    if (i%2 === 0){ 
        d[i] = Math.min(d[i], d[i/2] + 1);
    }
    if (i%3 === 0){ 
        d[i] = Math.min(d[i], d[i/3] + 1); 
        
    }
} 
console.log(d[N])