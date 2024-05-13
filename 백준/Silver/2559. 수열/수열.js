const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); 

const [N, K] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number); 
let dp = [arr[0]];
for (let i = 1; i < N; i++) { 
    dp.push(arr[i] + dp[i - 1]);
} 
let maxSum = dp[K-1];
for (let i = K; i < N; i++){ 
    maxSum = Math.max(maxSum, dp[i] - dp[i-K]);
}

console.log(maxSum)
