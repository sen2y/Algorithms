function solution(hp) {
    five = parseInt(hp/5)
    while (true) {
        n = hp - five*5
        if (n%3===0){
            return five+ n/3
        }
        five--;
    }
}