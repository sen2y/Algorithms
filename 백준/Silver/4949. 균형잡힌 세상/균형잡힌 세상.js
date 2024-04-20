const fs = require("fs"); 
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.map((x) => x); 

let output = [];
for (str in arr) {
  const word = arr[str].slice(0, -1).split("");
  let stack = [];
  let flag = true;
  if (!arr[str].slice(0, -1).length) continue; // 입력값이 . 하나인 경우 넘어가기
  // word.forEach((x) => { // forEach문에서 break문 사용 불가. for문으로 변경
  for (let i = 0; i < word.length; i++) {
    const x = word[i]; 
    if (x == "(" || x == "[" || x == ")" || x == "]") { // 입력값이 대/소괄호인 경우에만 조건문으로
     
      if (
        (!stack.length && x == ")") || // 빈배열에 닫힌 괄호 들어오면 for문 탈출
        (!stack.length && x == "]")
      ) {
        flag = false;
        break; // for문 탈출
        
        
      } else if (
        (stack[stack.length - 1] == "[" && x == "]") ||
        (stack[stack.length - 1] == "(" && x == ")")
      ) {  
        stack.pop();
      } else if ( 
        // 입력이 닫는 괄호인데 직전 괄호가 다른 종류의 열린 괄호일때 for문 탈출
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
