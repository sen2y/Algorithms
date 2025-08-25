let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let arr = [];
for (let i=1; i<input.length; i++){
  arr.push(Number(input[i]));
}

arr.sort((a,b)=>a-b);

console.log(arr.join('\n'))