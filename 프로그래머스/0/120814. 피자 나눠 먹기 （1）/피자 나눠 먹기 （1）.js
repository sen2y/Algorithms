function solution(n) {
    if (n/7 === Math.floor(n/7)) {
        return n/7;
        } 
    return Math.floor(n/7) + 1;
}