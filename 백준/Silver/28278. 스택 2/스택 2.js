const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = input.slice(1).map(x=> x.split(' '))
// arr
// [
//   [ '4' ],[ '1', '3' ],[ '1', '5' ],[ '3' ],[ '2' ],[ '5' ],[ '2' ],[ '2' ],[ '5' ]
// ]

//매 출력에 console.log를 사용하는 것은 대용량 출력을 처리할 때 비효율적이다. 
//대신 출력을 배열로 저장하고 마지막에 한꺼번에 출력하면 성능이 크게 향상
let stack = [];
let output = []; // 출력값
arr.forEach(x=>{ 
  switch (Number(x[0])) {
    case (1) : 
      stack.push(Number(x[1]));
      break;
    case (2) :  
      if (stack.length) output.push(stack.pop());
      else output.push(-1);
      break;
    case (3) : 
      output.push(stack.length);
      break;
    case (4) :
      if (!stack.length) output.push(1);
      else output.push(0);
      break;
    case (5): 
      if (stack.length) output.push(stack[stack.length-1]);
      else output.push(-1);
      break;
  }
})
console.log(output.join('\n'))

// 시간 초과된 코드
//let stack = [];
// arr.forEach(x=>{ 
//   switch (Number(x[0])) {
//     case (1) : 
//       stack.push(Number(x[1]));
//       break;
//     case (2) :  
//       if (stack.length) console.log(stack.pop());
//       else console.log(-1);
//       break;
//     case (3) : 
//       console.log(stack.length);
//       break;
//     case (4) :
//       if (!stack.length) console.log(1);
//       else console.log(0);
//       break;
//     case (5): 
//       if (stack.length) console.log(stack[stack.length-1]);
//       else console.log(-1);
//       break;
//   }
// })


