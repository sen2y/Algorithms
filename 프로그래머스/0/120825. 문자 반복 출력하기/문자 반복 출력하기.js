function solution(my_string, n) {
    let stack = []
    for (i of my_string){
        stack.push(i.repeat(n))
    }
    return(stack.join(''))
}