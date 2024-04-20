const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.slice(1).map(x=> Number(x.split(' ')))

let stack = [];
arr.forEach(x => {
  if (x==0) {
    stack.pop()
  }
  else {
    stack.push(x)
  } 
})

if (!stack.length) console.log(0);
else console.log(stack.reduce((a, b) => a+b));
