function solution(money) {
    n = parseInt(money / 5500)
    w = money % 5500
    answer = [n,w]
    return answer
}