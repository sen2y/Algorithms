const fs = require("fs"); 
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.map((x) => x); 

let output = [];
for (str in arr) {
  const word = arr[str].slice(0, -1).split("");
  let stack = [];
  let flag = true;
  if (!arr[str].slice(0, -1).length) continue; // 입력값이 . 하나인 경우 넘어가기
  // word.forEach((x) => {
  for (let i = 0; i < word.length; i++) {
    const x = word[i]; 
    if (x == "(" || x == "[" || x == ")" || x == "]") {
     
      if (
        (!stack.length && x == ")") ||
        (!stack.length && x == "]") ||
        (stack[stack.length - 1] == "(" && x == "]") ||
        (stack[stack.length - 1] == "[" && x == ")")
      ) {
        flag = false;
        break;
        
      } else if (
        (stack[stack.length - 1] == "[" && x == "]") ||
        (stack[stack.length - 1] == "(" && x == ")")
      ) {  
        stack.pop();
      } else if (
        (stack[stack.length - 1] == "[" && x == ")") ||
        (stack[stack.length - 1] == "(" && x == "]")
      ) {
        flag = false
        break;
      } else {
        stack.push(x);
      }
    }
  }
  // });
  if (flag === false) output.push('no');
  else if (!stack.length) output.push("yes");
  else output.push("no");
}
console.log(output.join("\n"));
