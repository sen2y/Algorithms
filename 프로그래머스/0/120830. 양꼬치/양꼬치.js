function solution(n, k) {
    service = parseInt(n/10)
    return n*12000 + (k-service)*2000
}