const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let output = []; // 출력값 스택
let operator_stack = []; // 연산자 임시 저장 스택
let operator = { // 연산자 우선순위 표기
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
  };

for (let char of input[0]) { // 문자 하나씩 반복문 돌리기

  if (char >= "A" && char <= "Z") { // 문자면 그대로 출력스택에 push
    output.push(char);
  } 
  else if (["+", "-", "*", "/"].includes(char)) { // 연산자인 경우,
     while (
       // 스택의 top에 있는 연산자의 우선순위가 현재 연산자의 우선순위보다 크거나 같은 경우, 
       // stack에서 pop하여 출력배열에 추가
      operator_stack.length &&
      operator[operator_stack[operator_stack.length - 1]] >= operator[char]
    ) {
      output.push(operator_stack.pop()); // 스택에서 pop해서 출력스택에 push
    }
      
    // 위 조건과 상관없이, 현재 연산자를 operator 스택에 push
    operator_stack.push(char);
  }
  else if (char === '(') { // 열린 괄호는 스택에 추가
    operator_stack.push(char)
  }
  else if (char === ')') { // 닫힌 괄호는 열린괄호가 나올때까지 operator 스택 Pop 반복
    while (operator_stack.length > 0 && operator_stack[operator_stack.length-1] !== '(' ){
      output.push(operator_stack.pop());
    }
    operator_stack.pop(); // '(' 제거
  }
  
} 

// 반복문 종료 후, operator_stack에 값이 남아있다면 하나씩 pop하여 output 스택에 추가
while (operator_stack.length > 0) {
  output.push(operator_stack.pop());
}

// 후위연산자 결과값
console.log(output.join(''));
