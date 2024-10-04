function solution(n) {
    return [...n.toString()].reduce((a,b)=>a+b*1,0)
}