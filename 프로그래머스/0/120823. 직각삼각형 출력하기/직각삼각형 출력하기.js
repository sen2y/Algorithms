const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () { 
    const num = Number(input[0])
    makeTree(num)
});

function makeTree(num){
    for (let i=0; i<num; i++){
        console.log('*'.repeat(i+1))
    }
}

